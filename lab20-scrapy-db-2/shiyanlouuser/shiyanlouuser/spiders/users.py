# -*- coding: utf-8 -*-
import scrapy
from shiyanlouuser.items import UserItem


class UsersSpider(scrapy.Spider):
    name = 'users'
    allowed_domains = ['shiyanlou.com']


    @property
    def start_urls(self):

        return ('https://www.shiyanlou.com/user/{}/'.format(i) for i in range(425000, 424800, -10))




    def parse(self, response):


        yield UserItem({
            'name': response.css('span.username::text').extract_first(),
            'type': response.css('img.user-icon::attr(title)').extract_first(default="normal user"),
            'join_date': response.css('span.join-date::text').extract_first(),
            'level': response.css('span.user-level::text').extract_first(),
            'status': response.css('div.userinfo-banner-status span::text').extract_first(),
            'job': response.xpath('//div[@class="userinfo-banner-status"]/span[2]/text()').extract_first(),
            'school': response.css('div.userinfo-banner-status a::text').extract_first(),
            'learn_courses_num': response.css('span.latest-learn-num::text').extract_first()
            })
