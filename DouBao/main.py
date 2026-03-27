from fastapi import FastAPI, WebSocket, WebSocketDisconnect, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from typing import Dict, List, Tuple

app = FastAPI()

# 模板引擎配置
templates = Jinja2Templates(directory="templates")

# 核心数据结构
active_connections: Dict[str, WebSocket] = {}  # 在线用户连接池
message_history: List[Tuple[str, str]] = []  # 消息历史：[(发送者, 消息内容), ...]


@app.get("/", response_class=HTMLResponse)
async def get_chat_page(request: Request):
    """返回聊天页面"""
    return templates.TemplateResponse("chat.html", {"request": request})


@app.websocket("/ws/{username}")
async def websocket_endpoint(websocket: WebSocket, username: str):
    """WebSocket端点，处理用户连接、消息收发、历史消息推送"""
    # 接受WebSocket连接
    await websocket.accept()

    # 检查用户名是否已存在
    if username in active_connections:
        await websocket.send_text(f"错误：用户名 {username} 已被占用！")
        await websocket.close()
        return

    # 将新用户加入连接池
    active_connections[username] = websocket
    print(f"用户 {username} 上线，当前在线人数：{len(active_connections)}")

    # 【新增】推送历史消息给新用户
    await send_history_messages(websocket)

    # 广播用户上线消息
    system_msg = f"系统提示：{username} 加入了聊天"
    await broadcast_message(system_msg, "系统")
    # 【新增】上线消息存入历史
    message_history.append(("系统", system_msg))

    try:
        while True:
            # 接收客户端发送的消息
            data = await websocket.receive_text()

            # 支持点对点消息：格式为 "用户名: 消息内容"
            if ":" in data:
                target_user, msg_content = data.split(":", 1)
                target_user = target_user.strip()
                msg_content = msg_content.strip()

                # 发送点对点消息
                if target_user in active_connections:
                    private_msg_to_target = f"[{username}(私聊)]: {msg_content}"
                    private_msg_to_self = f"[我->{target_user}]: {msg_content}"
                    # 给目标用户发消息
                    await active_connections[target_user].send_text(private_msg_to_target)
                    # 给自己发提示
                    await websocket.send_text(private_msg_to_self)
                    # 【新增】私聊消息存入历史（仅双方可见，这里简化为存到公共历史，可优化）
                    message_history.append((username, f"(私聊给{target_user}) {msg_content}"))
                else:
                    error_msg = f"错误：用户 {target_user} 不在线！"
                    await websocket.send_text(error_msg)
            else:
                # 广播群消息
                await broadcast_message(data, username)
                # 【新增】群消息存入历史
                message_history.append((username, data))

    except WebSocketDisconnect:
        # 用户断开连接
        del active_connections[username]
        print(f"用户 {username} 下线，当前在线人数：{len(active_connections)}")
        # 广播用户下线消息
        system_msg = f"系统提示：{username} 离开了聊天"
        await broadcast_message(system_msg, "系统")
        # 【新增】下线消息存入历史
        message_history.append(("系统", system_msg))


async def broadcast_message(message: str, sender: str):
    """广播消息给所有在线用户"""
    formatted_msg = f"[{sender}]: {message}"
    for connection in active_connections.values():
        await connection.send_text(formatted_msg)


async def send_history_messages(websocket: WebSocket):
    """给新连接的用户推送历史消息"""
    if not message_history:
        await websocket.send_text("[系统]: 暂无历史消息")
        return
    # 先发送历史消息提示
    await websocket.send_text("[系统]: 以下是历史消息：")
    # 遍历历史消息，逐条推送
    for sender, content in message_history:
        formatted_msg = f"[{sender}]: {content}"
        await websocket.send_text(formatted_msg)


# 启动服务
if __name__ == "__main__":
    import uvicorn

    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)