import scrapy
from ..items import TrustpilotReviewsItem


class TrustpReviewSpider(scrapy.Spider):
    '''
    spider to obtain company reviews and average rating from trustpilot
    for a list of companies, if they have trustpilot profile
    '''
    name = 'trustpilot'
    allowed_domains = ['trustpilot.com']
    start_urls = ['https://uk.trustpilot.com/review/www.centralautopoint.com']

    def parse(self, response):
        review = TrustpilotReviewsItem()
        # company_name = ideally this will iterate through json file to get company name
        company_name = response.xpath('//h1/span/text()').extract_first()
        summary = response.xpath('//p/text()').extract_first()
        review["company_name"] = company_name
        review["summary"] = summary
        
        print(f'WHAT DOES MY ITEM RETURN{review}')
        
        yield review