# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy

class GeojsonPointItem(scrapy.Item):
    ref = scrapy.Field()
    lat = scrapy.Field()
    lon = scrapy.Field()
    name = scrapy.Field()
    addr_full = scrapy.Field()
    housenumber = scrapy.Field()
    street = scrapy.Field()
    city = scrapy.Field()
    state = scrapy.Field()
    postcode = scrapy.Field()
    country = scrapy.Field()
    phone = scrapy.Field()
    website = scrapy.Field()
    store_url = scrapy.Field()
    email = scrapy.Field()
    opening_hours = scrapy.Field()
    brand = scrapy.Field()
    chain_id = scrapy.Field()
    chain_name = scrapy.Field()
    categories = scrapy.Field()
    brand_wikidata = scrapy.Field()
    extras = scrapy.Field()
    services = scrapy.Field()
