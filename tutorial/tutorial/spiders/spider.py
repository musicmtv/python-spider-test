import scrapy

class StackOverflowSpider(scrapy.Spider):
	name = "stackoverflow"
	start_urls=["http://stackoverflow.com/questions?sort=votes"]
	def parse(self,response):
		for href in response.css('.question-summary h3 a::attr(href)'):
			full_url = response.urljoin(href.extract())
			print(full_url)