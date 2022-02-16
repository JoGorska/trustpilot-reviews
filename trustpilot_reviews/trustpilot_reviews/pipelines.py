# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
import sqlite3

class TrustpilotReviewsPipeline(object):
    def __init__(self):
        self.create_connection()
        self.create_table()
    
    def create_connection(self):
        self.conn = sqlite3.connect("trustpilot.db")
        self.curr = self.conn.cursor()
    
    def create_table(self):
        self.curr.execute("""DROP TABLE IF EXISTS trustpilot_tb""")
        self.curr.execute("""CREATE TABLE trustpilot_tb(
            company_name text,
            summary text,

            one_header text,
            one_content text,

            two_header text,
            two_content text,

            three_header text,
            three_content text,
        )""")


    def process_item(self, item, spider):
        self.store_db(item)
        return item

    def store_db(self, item):
        self.curr.execute("""insert into trustpilot_tb values (?,?,?,?,?,?,?,?)""",(
            item["company_name"],
            item["summary"],
            item["one_header"],
            item["one_content"],
            item["two_header"],
            item["two_content"],
            item["three_header"],
            item["three_content"]
        ))
        self.conn.commit()
