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
        company_name = response.xpath('//h1/span/text()').extract_first()
        summary = response.xpath('//p/text()').extract_first()
        review["company_name"] = company_name
        review["summary"] = summary
        article_container = response.xpath('//article').extract()
        print(len(article_container))
        containers_list = []
        if len(article_container) >= 3:
            containers_list = [article_container[0], article_container[1], article_container[2]]
        elif len(article_container) == 2:
            containers_list = [article_container[0], article_container[1]]
        elif len(article_container) == 0:
            containers_list = [article_container[0]]
        print(f'LIST OF CONTAINERS {len(containers_list)}')

        # print(first_three)
        # one_header = response.xpath('//')
        
        # print(f'WHAT DOES MY ITEM RETURN{review}')
        
        yield review