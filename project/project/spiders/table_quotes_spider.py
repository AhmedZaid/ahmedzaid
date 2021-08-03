import json
import logging
import time

import psycopg2
import scrapy
from bs4 import BeautifulSoup

from project.service import create_quotes
# you can change this to parse as much as you want
from scrapy_redis.spiders import RedisSpider

Pages = 5


class TableQuotesSpider(RedisSpider):
    name = "table_quotes"

    #start_urls = ['http://quotes.toscrape.com/tableful/']
    redis_key = 'table_quotes:start_urls'

    def __init__(self, *args, **kwargs):
        # Modify the class name here to the current class name
        super(TableQuotesSpider, self).__init__(*args, **kwargs)



    def parse(self, response):
        soup = BeautifulSoup(response.body, "lxml")
        table = soup.find("table")
        conn = psycopg2.connect("dbname=postgres user=postgres password=postgres")
        cur = conn.cursor()

        for row in table.find_all("tr")[1:-1:2]:
            data = row.contents[1].next.split("Author:")
            create_quotes(cur, data[0].replace("'", "''"), data[1].replace("'", "''"), "")
        logging.info("TableQuote. Adding quotes")
        conn.commit()
        # To avoid hit the website to much. Also I added CONCURRENT_REQUESTS_PER_DOMAIN in settings
        time.sleep(3)

