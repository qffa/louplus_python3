# -*- coding: utf-8 -*-
import scrapy
from shiyanlougithub.items import RepositoryItem


class RepositorySpider(scrapy.Spider):
    name = 'repository'
    allowed_domains = ['github.com']


    @property
    def start_urls(self):

        url_tmpl = 'https://github.com/shiyanlou?tab=repositories&page={}'
        
        return (url_tmpl.format(i) for i in range(1,5))


    def parse(self, response):

        repositories = response.css('div#user-repositories-list li')
        for repository in repositories:
            item = RepositoryItem({
                'name': repository.css('h3 a::text').re_first('[\s]*(.*)'),
                'update_time': repository.css('relative-time::attr(datetime)').extract_first()
                })

            yield item
