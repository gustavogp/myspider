import scrapy

class BlogSpider(scrapy.Spider):
  name = 'blogspider'
  start_urls = ['https://blog.scrapinghub.com']

  def parse(self, response):
    for url in response.css('ul li a::attr("href")').re('.*/category/.*'):
      yield scrapy.Request(url, self.parse_titles)

  def parse_titles(seld, response):
    for post_title in response.css('div.entries > ul > li a::text').extract():
      yield {'title': post_title}
