import re

import scrapy

from scrapy.loader import ItemLoader
from ..items import CreditofondiarioItem
from itemloaders.processors import TakeFirst


class CreditofondiarioSpider(scrapy.Spider):
	name = 'creditofondiario'
	start_urls = ['https://www.creditofondiario.eu/press-media/news/']

	def parse(self, response):
		post_links = response.xpath('//div[@class="gdlr-core-blog-grid "]')
		for post in post_links:
			url = post.xpath('.//h3/a/@href').get()
			date = post.xpath('./div/div/span/a/text()').get()
			yield response.follow(url, self.parse_post, cb_kwargs=dict(date=date))

		next_page = response.xpath('//a[@class="next page-numbers"]/@href').getall()
		yield from response.follow_all(next_page, self.parse)


	def parse_post(self, response, date):
		title = response.xpath('(//span[@property="itemListElement"]/a/span[@property="name"]/font/font/text())[last()]').get()
		description = response.xpath('//div[@class="financity-single-article-content"]//text()[normalize-space()]').getall()
		description = [p.strip() for p in description]
		description = ' '.join(description).strip()

		item = ItemLoader(item=CreditofondiarioItem(), response=response)
		item.default_output_processor = TakeFirst()
		item.add_value('title', title)
		item.add_value('description', description)
		item.add_value('date', date)

		return item.load_item()
