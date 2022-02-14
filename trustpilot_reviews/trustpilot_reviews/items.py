# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class TrustpilotReviewsItem(scrapy.Item):
    '''
    Item containing data collected 
    from page sumarising company rating
    '''
    company_name = scrapy.Field()
    summary = scrapy.Field()

    one_header = scrapy.Field()
    one_content = scrapy.Field()

    two_header = scrapy.Field()
    two_content = scrapy.Field()

    three_header = scrapy.Field()
    three_content = scrapy.Field()
