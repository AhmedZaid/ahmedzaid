from scrapy import cmdline
cmdline.execute("scrapy crawl table_quotes".split())
cmdline.execute("scrapy crawl scroll_quotes".split())