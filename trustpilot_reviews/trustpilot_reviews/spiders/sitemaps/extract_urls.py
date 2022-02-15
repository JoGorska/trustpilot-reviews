from xml.dom.minidom import parse
import xml.dom.minidom

# https://www.tutorialexample.com/python-parse-xml-sitemap-to-extract-urls-a-simple-guide-python-tutorial/

def extract_urls():
    '''
    takes list of all sitemap files and extracts urls into a list
    '''
    all_sitemaps = [
    r'domains0_en-gb.xml',
    r'domains1_en-gb.xml',
    r'domains2_en-gb.xml',
    r'domains3_en-gb.xml',
    r'domains4_en-gb.xml',
    r'domains5_en-gb.xml',
    r'domains6_en-gb.xml',
    r'domains7_en-gb.xml',
    r'domains8_en-gb.xml',
    r'domains9_en-gb.xml']

    all_review_urls = []
    for file in all_sitemaps:

        xml_file = file
        DOMTree = xml.dom.minidom.parse(xml_file)
        root_node = DOMTree.documentElement
        loc_nodes = root_node.getElementsByTagName("loc")

        for loc in loc_nodes:
            all_review_urls.append(loc.childNodes[0].data)

        return(all_review_urls)


def extract_company_domains(urls_list):
    '''
    takes list of review urls and extracts company domains from each item
    '''
    only_urls = []
    for review_url in urls_list:
        to_remove = "https://uk.trustpilot.com/review/"

        one_url = review_url.replace(to_remove, "")
        only_urls.append(one_url)
    return(only_urls)


def trustpilot_urls_and_company_domains_dictionary(urls):
    '''
    takes list of trustpilot urls, uses function to extract company domains
    and returns a dictionary with both trustpilot urls as keys and 
    company_domains as values
    '''
    domains = extract_company_domains(urls)
    url_and_domain_dictionary = dict(zip(urls, domains))
    return url_and_domain_dictionary

# example = ['https://uk.trustpilot.com/review/www.solidsheds.com', 'https://uk.trustpilot.com/review/holidays.transavia.fr', 'https://uk.trustpilot.com/review/www.mtechcomms.co.uk', 'https://uk.trustpilot.com/review/www.knightsplc.com', 'https://uk.trustpilot.com/review/book2wheel.com', 'https://uk.trustpilot.com/review/www.unik-svejs.dk', 'https://uk.trustpilot.com/review/nestfs.co.uk', 'https://uk.trustpilot.com/review/musicstreamingawards.com', 'https://uk.trustpilot.com/review/enroutejewelry.com', 'https://uk.trustpilot.com/review/www.seas-nve.dk', 'https://uk.trustpilot.com/review/www.reachpharmacy.com', 'https://uk.trustpilot.com/review/askboosters.com', 'https://uk.trustpilot.com/review/papawaldis.com']
# test_me = return_urls_and_domains_dictionary(example)
# print(test_me)