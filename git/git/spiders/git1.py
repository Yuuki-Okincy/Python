import scrapy


class Git1Spider(scrapy.Spider):
    name = "git1"
    allowed_domains = ["github.com"]
    start_urls = ["https://github.com/Yuuki-Okincy"]

    def start_requests(self):
        url = self.start_urls[0]
        temp = ('_octo=GH1.1.990585513.1735205940; '
                '_device_id=969ccc1ba697ad19c1131f9561559d6b;'
                ' MicrosoftApplicationsTelemetryDeviceId=b28e3693-ed27-4f18-97a2-609ca66a1377; '
                'MSFPC=GUID=776f19d2eb1741439c105a224350c8cb&HASH=776f&LV=202501&V=4&LU=1737380256605;'
                ' cpu_bucket=xlg; preferred_color_mode=light; tz=Asia%2FShanghai; '
                'saved_user_sessions=120643672%3ACsuFQIfDMDhsv7SU40CjeeO6okMG1n0ysCv8Gd3FPnUfPkS4;'
                ' user_session=CsuFQIfDMDhsv7SU40CjeeO6okMG1n0ysCv8Gd3FPnUfPkS4; '
                '__Host-user_session_same_site=CsuFQIfDMDhsv7SU40CjeeO6okMG1n0ysCv8Gd3FPnUfPkS4;'
                ' tz=Asia%2FShanghai; '
                'color_mode=%7B%22color_mode%22%3A%22auto%22%2C%22light_theme%22%3A%7B%22name%22%3A%22light%22%2C%22color_mode%22%3A%22light%22%7D%2C%22dark_theme%22%3A%7B%22name%22%3A%22dark%22%2C%22color_mode%22%3A%22dark%22%7D%7D;'
                ' logged_in=yes;'
                ' dotcom_user=Yuuki-Okincy;'
                ' _gh_sess=8dzSuY8t2cm0yqSTpPLlSZbEQMuypjjKBJMuKUnc2KGNJ8sQao%2BkbUxb%2BLIb%2BO2w7Ac4p5TyYM8LL5z82MvtN6Ur1XWk64xGGMaCYft7tljuAtZPrrtk4uGiylxmVAI3R2PBYvMtLKororOl0Xg1IBuHUBc9kProvgmFl4E1Jaa2Blh15IknGHmzIWOwg1pYXapuZv3hsxGiFnvvdK2K9kd2CmdkIdcWK%2BY4G%2B%2F%2Bdu3akMpusW5O1fvZoDsXUJeZHTe%2BK7eRIEsEdzejL4vroLgHLeRl%2FdaRjsnRhU8uszqJgxlb7v5fktyafNeF6ifH06XHLNBazldV91jGAuZKe0f0zm%2F6GxAO8rkz7yW%2B7OvVRPkpklcGARkN0V6W4lE%2FsNN1B9nKfbT5KhXuKR25%2F3vLYnGSYLihPlZ6kehuiGh2OXzuZjioLSG%2BjRDfYDpJNZFI1AIZajl7U43PGImJLygmfW1FLdZE1%2FIScCc8HuhSw4ptvIBdtNtT6bsQ8byL2KlBUA5IgDtLZu5CAcBoR5gXMnFFeilsHcwhxmlFG5XiKnDhsMDSQL9QUzcBiWo2b3A67PV2xZHTH94ciN4oX9%2BCozlHGyFznSnRpTouxsp4vvpshKxsJDutgmckgszvvHGmQJN%2FX3TQ4DOF1gqKgsbXUs2vzVlUcbDH3gG8TvUhdcltRLbVOaqlN9kZMoELvAjGxy846nae%2BwJSdj5EJNV9pnGDDM6%2BSFH02t4czn8uwgEbLx1Bx%2F%2BfyWpEfZiSR8dWb5xWgiPvXayqonY5kHcYkMI1RQ0zzqUgIxmNM3UEj2d9qj%2FGYWFvUgcfzFcbLMCDifaunbiQwxvrGqxrQDMKkHe8SGB5QgXPENkXZKEjzjeVZjvjqBnda9pUZXq8fwzA5nC222fgx9XOJ2ijvh9kZgPY%2BAisNJbrybl0PrAoVStVH01Hnpnqt6%2FwUYzJt%2Bkxh1VbgELJQpDQH%2Bsg7GG8Sv%2F1dHq%2BBXW%2B7pg9Qx4NDx%2BjXgD7xbENSXRsurML%2Fp5MH8E6QNWwbpDI%2BR5EMA%3D%3D--pIxVEXkAq%2FFsoZr0--Pa787gQtlx9B3kL77A%2BMYQ%3D%3D')
        cookies =  {data.split('=')[0]:data.split('=')[-1] for data  in temp.split('; ')}
        yield scrapy.Request(url=url,
                             callback=self.parse,
                             cookies=cookies)
    def parse(self, response):
       print(response.xpath('/html/head/title/text()').get())
