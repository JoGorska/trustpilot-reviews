# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
import sqlite3

class TrustpilotReviewsPipeline:
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


    def process_item(self, review, spider):
        self.store_db(review)
        return review

    def store_db(self, review):
        self.curr.execute("""insert into trustpilot_tb values (?,?,?,?,?,?,?,?)""",(
            review["company_name"],
            review["summary"],
            review["one_header"],
            review["one_content"],
            review["two_header"],
            review["two_content"],
            review["three_header"],
            review["three_content"]
        ))
        self.conn.commit()
