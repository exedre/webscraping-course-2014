# Scrapy settings for wine project
#
# For simplicity, this file contains only the most important settings by
# default. All the other settings are documented here:
#
#     http://doc.scrapy.org/topics/settings.html
#

BOT_NAME = 'wine'

SPIDER_MODULES = ['wine.spiders']
NEWSPIDER_MODULE = 'wine.spiders'

# Crawl responsibly by identifying yourself (and your website) on the user-agent
#USER_AGENT = 'wine (+http://www.yourdomain.com)'
