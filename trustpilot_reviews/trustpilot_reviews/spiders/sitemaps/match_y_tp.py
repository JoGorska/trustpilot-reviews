from .extract_urls import extract_urls, trustpilot_urls_and_company_domains_dictionary, extract_company_domains
import json


def get_yell_company_websites_list():
    '''
    takes the json file copied from find_company repository containing all companies searched by
    "garage" and "northamptonshire" and makes a list of company websites
    '''

    with open('../match/yell_nthshire.json') as json_file:

        data = json.load(json_file)
        yell_company_websites = []
        for item in data:
            website = item["company_website"]
            yell_company_websites.append(website)
        return yell_company_websites

# trustpilot_dictionary = trustpilot_urls_and_company_domains_dictionary()

# yell_list = get_yell_company_websites_list()
# urls = extract_urls()
# tp_list = extract_company_domains(urls)


def get_tp_review_urls_to_scrap():
    urls_list = []
    for tp_domain in tp_list:
        for y_domain in yell_list:
            if y_domain:
                if tp_domain in y_domain:
                    urls_list.append(urls[tp_list.index(tp_domain)])
    # print(f'BEFORE CLEANING {urls_list}')
    # to_remove = ["https://uk.trustpilot.com/review/t.co", "https://uk.trustpilot.com/review/www.facebook.com"]
    # for dirty_url in urls_list:
    #     if dirty_url=="https://uk.trustpilot.com/review/t.co":
    #         urls_list.remove(dirty_url)
    # print(f'AFTER CLEANING {urls_list}')
 
    return urls_list

# tp_review_urls_to_scrap_list = get_tp_review_urls_to_scrap()
