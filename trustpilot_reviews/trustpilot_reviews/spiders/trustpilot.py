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
        print(f'LIST OF CONTAINERS LENGTH {len(containers_list)}')

        all_headers = response.xpath('//h2/a/text()').extract()
        all_content = response.xpath('//div[@class="styles_reviewContent__0Q2Tg"]/p/text()').extract()
        print(f'ALL CONTENT LIST {all_content}')
        if len(all_headers) >= 3:
            one_header = all_headers[0]
            one_content = all_content[0]

            two_header = all_headers[1]
            two_content = all_content[1]

            three_header = all_headers[2]
            three_content = all_content[2]
            review["one_header"] = one_header
            review["one_content"] = one_content
            review["two_header"] = two_header
            review["two_content"] = two_content
            review["three_header"] = three_header
            review["three_content"] = three_content
        elif len(all_headers) == 2:
            one_header = all_headers[0]
            one_content = all_content[0]

            two_header = all_headers[1]
            two_content = all_content[1]

            review["one_header"] = one_header
            review["one_content"] = one_content
            review["two_header"] = two_header
            review["two_content"] = two_content
        elif len(all_headers) == 0:
            one_header = all_headers[0]
            one_content = all_content[0]

            review["one_header"] = one_header
            review["one_content"] = one_content
        
        # print(f'ONE HEADER FROM EACH ARTICLE {one_header}')

        # print(first_three)
        # one_header = response.xpath('//')
        
        # print(f'WHAT DOES MY ITEM RETURN{review}')
        
        yield review