# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class FitnessItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    exercisename = scrapy.Field()
    gif = scrapy.Field()
    video = scrapy.Field()
    preparation = scrapy.Field()
    execution = scrapy.Field()
    comments = scrapy.Field()
    utility = scrapy.Field()
    mechanics = scrapy.Field()
    force = scrapy.Field()
    target = scrapy.Field()
    synergists = scrapy.Field()
    stabilizers = scrapy.Field()
    antagoniststabilizers = scrapy.Field()

    #pass
