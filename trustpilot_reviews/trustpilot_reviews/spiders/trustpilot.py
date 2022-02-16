import scrapy
from ..items import TrustpilotReviewsItem
from .sitemaps.extract_urls import trustpilot_urls_and_company_domains_dictionary
from .sitemaps.match_y_tp import get_tp_review_urls_to_scrap

class TrustpReviewSpider(scrapy.Spider):
    '''
    spider to obtain company reviews and average rating from trustpilot
    for a list of companies, if they have trustpilot profile
    '''
    name = 'trustpilot'
    allowed_domains = ['trustpilot.com']
    start_urls = ['https://uk.trustpilot.com/review/www.centralautopoint.com']
    
    # list obtained by running match_y_tp.py inside stiemaps directory

    def parse(self, response):
        item = TrustpilotReviewsItem()
        company_name = response.xpath('//h1/span/text()').extract_first()
        summary = response.xpath('//p/text()').extract_first()
        item["company_name"] = company_name
        item["summary"] = summary
        article_container = response.xpath('//article').extract()
        print(len(article_container))

        all_headers_with_commas = response.xpath('//h2/a/text()').extract()
        all_headers = []
        for header_item in all_headers_with_commas:
            new_header_item = header_item.replace(",", "")
            all_headers.append(new_header_item)
        all_content_with_commas = response.xpath('//div[@class="styles_reviewContent__0Q2Tg"]/p/text()').extract()
        all_content = []
        for content_item in all_content_with_commas:
            new_content_item = content_item.replace(",", "")
            all_content.append(new_content_item)
        if len(all_headers) >= 3:
            one_header = all_headers[1]
            one_content = all_content[0]

            two_header = all_headers[2]
            two_content = all_content[1]

            three_header = all_headers[3]
            three_content = all_content[2]
            item["one_header"] = one_header
            item["one_content"] = one_content
            item["two_header"] = two_header
            item["two_content"] = two_content
            item["three_header"] = three_header
            item["three_content"] = three_content
        elif len(all_headers) == 2:
            one_header = all_headers[1]
            one_content = all_content[0]

            two_header = all_headers[2]
            two_content = all_content[1]

            item["one_header"] = one_header
            item["one_content"] = one_content
            item["two_header"] = two_header
            item["two_content"] = two_content
        elif len(all_headers) == 0:
            one_header = all_headers[1]
            one_content = all_content[0]

            item["one_header"] = one_header
            item["one_content"] = one_content
        yield item
        # test_url = 'https://uk.trustpilot.com/review/garolla.co.uk'
        truspilot_domains_list = ['https://uk.trustpilot.com/review/t.co', 'https://uk.trustpilot.com/review/t.co', 'https://uk.trustpilot.com/review/t.co', 'https://uk.trustpilot.com/review/t.co', 'https://uk.trustpilot.com/review/t.co', 'https://uk.trustpilot.com/review/t.co', 'https://uk.trustpilot.com/review/t.co', 'https://uk.trustpilot.com/review/t.co', 'https://uk.trustpilot.com/review/t.co', 'https://uk.trustpilot.com/review/t.co', 'https://uk.trustpilot.com/review/ring.com', 'https://uk.trustpilot.com/review/inoautocentres.co.uk', 'https://uk.trustpilot.com/review/inoautocentres.co.uk', 'https://uk.trustpilot.com/review/garolla.co.uk', 'https://uk.trustpilot.com/review/etyres.co.uk', 'https://uk.trustpilot.com/review/etyres.co.uk', 'https://uk.trustpilot.com/review/www.facebook.com', 'https://uk.trustpilot.com/review/www.facebook.com', 'https://uk.trustpilot.com/review/www.facebook.com', 'https://uk.trustpilot.com/review/www.facebook.com', 'https://uk.trustpilot.com/review/www.facebook.com', 'https://uk.trustpilot.com/review/www.facebook.com', 'https://uk.trustpilot.com/review/www.facebook.com', 'https://uk.trustpilot.com/review/www.facebook.com', 'https://uk.trustpilot.com/review/www.facebook.com', 'https://uk.trustpilot.com/review/www.facebook.com', 'https://uk.trustpilot.com/review/www.facebook.com', 'https://uk.trustpilot.com/review/www.facebook.com', 'https://uk.trustpilot.com/review/www.facebook.com', 'https://uk.trustpilot.com/review/www.facebook.com', 'https://uk.trustpilot.com/review/www.facebook.com', 'https://uk.trustpilot.com/review/www.facebook.com', 'https://uk.trustpilot.com/review/www.facebook.com', 'https://uk.trustpilot.com/review/www.facebook.com', 'https://uk.trustpilot.com/review/www.ratedpeople.com', 'https://uk.trustpilot.com/review/www.national.co.uk', 'https://uk.trustpilot.com/review/www.national.co.uk', 'https://uk.trustpilot.com/review/www.national.co.uk', 'https://uk.trustpilot.com/review/ring.co.uk', 'https://uk.trustpilot.com/review/ring.co.uk', 'https://uk.trustpilot.com/review/sheds.co.uk', 'https://uk.trustpilot.com/review/ge.com', 'https://uk.trustpilot.com/review/ge.com', 'https://uk.trustpilot.com/review/thegaragedoorcentre.co.uk', 'https://uk.trustpilot.com/review/www.mrclutch.com', 'https://uk.trustpilot.com/review/eon.com', 'https://uk.trustpilot.com/review/www.centralautopoint.com']

        for url in truspilot_domains_list:
            if url is not None:
                yield scrapy.Request(url, callback=self.parse)
                   