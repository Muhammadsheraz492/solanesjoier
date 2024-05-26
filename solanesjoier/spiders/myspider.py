import scrapy


class MyspiderSpider(scrapy.Spider):
    name = "myspider"
    # allowed_domains = ["X"]
    start_urls = ["https://www.solanesjoier.com/13-anillos-compromiso?resultsPerPage=120"]

    def parse(self, response):
        hrefs = response.xpath('//div[@class="w-full overflow-hidden product-cover product-wrapper"]/a/@href').getall()
        print(len(hrefs))
        for href in hrefs:
            yield scrapy.Request(href, callback=self.details)

    def details(self,response):
        url=response.url
        data={}
        title = response.xpath('//h1[@class="my-2" and @itemprop="name"]/text()').get()
        price = response.xpath('//span[@itemprop="price"]/text()').get()
        reference_number = response.xpath(
            '//div[@class="product-reference flex items-center mb-2"]/span[@class="mb-0 font-body font-normal text-xs text-gray-800"]/text()').get()
        img_url = response.xpath('//img[@class="js-qv-product-cover"]/@src').get()

        data['image_url'] = img_url
        data['title'] = title
        data['price'] =price

        data['reference_number'] = reference_number
        data['url']=url
        yield data