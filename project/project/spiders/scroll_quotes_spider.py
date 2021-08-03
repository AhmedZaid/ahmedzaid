import json
import logging
import time

import psycopg2
import scrapy

from project.service import create_quotes
from scrapy_redis.spiders import RedisSpider


class ScrollQuotesSpider(RedisSpider):
    name = "scroll_quotes"

    #start_urls = ['http://quotes.toscrape.com/api/quotes?page=%d' % n for n in range(1, Pages)]
    redis_key = 'scroll_quotes:start_urls'

    def __init__(self, *args, **kwargs):
        # Modify the class name here to the current class name
        super(ScrollQuotesSpider, self).__init__(*args, **kwargs)

    def parse(self, response):
        response = json.loads(response.body.decode())
        logging.info("Start ScrollQuotes")
        conn = psycopg2.connect("dbname=postgres user=postgres password=postgres")
        cur = conn.cursor()
        for quote in response['quotes']:
            create_quotes(cur, quote['text'].replace("'", "''"), quote['author']['name'], json.dumps(quote['tags']))
        logging.info(f"ScrollQuotes. Adding {len(response['quotes'])} quotes")
        conn.commit()
        # To avoid hit the website to much. Also I added CONCURRENT_REQUESTS_PER_DOMAIN in settings
        time.sleep(3)

