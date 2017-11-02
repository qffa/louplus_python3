import scrapy


class ShiyanlouGithubSpider(scrapy.Spider):

    name = 'shiyanlou-repo'



    def start_requests(self):
        url_tmpl = "https://github.com/shiyanlou?tab=repositories&page={}"

        urls = (url_tmpl.format(i) for i in range(1, 5))

        for url in urls:
            yield scrapy.Request(url = url, callback = self.parse)




    def parse(self,response):

        for repo in response.css('div#user-repositories-list ul li'):
            yield {
                    "name": repo.css('div.d-inline-block h3 a::text').extract_first(),
                    "update_time": repo.css('relative-time::attr(datetime)').extract_first()
             }

