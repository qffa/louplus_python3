# -*- coding: utf-8 -*-
import scrapy
from courseimage.items import CourseImageItem


class CourseImageSpider(scrapy.Spider):
    name = 'course_image'
    allowed_domains = ['shiyanlou.com/courses']
#    start_urls = ['http://www.shiyanlou.com/courses/']


    @property
    def start_urls(self):
       return ('https://www.shiyanlou.com/courses?page={}'.format(i) for i in range(1, 24))

    def parse(self, response):
        item = CourseImageItem()

        item['image_urls'] = response.xpath('//div[@class = "course-img"]/img/@src').extract()

        yield item
