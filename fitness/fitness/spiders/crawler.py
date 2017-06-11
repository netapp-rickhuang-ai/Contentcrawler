import scrapy
import os
from bs4 import BeautifulSoup
from fitness.items import FitnessItem

class FitCrawler(scrapy.Spider):
    new_path = '/users/TimLin/fitness/fitness/test.txt'
    os.remove(new_path) if os.path.exists(new_path) else None
    name = 'fitness'
    start_urls=['http://www.exrx.net/Lists/Directory.html']
    def parse(self, response):
        res = BeautifulSoup(response.body, 'lxml')
        domain = "http://www.exrx.net/Lists/"
        for items in res.select('li'):
            if "#" not in items.select('a')[0]['href'] and "/Muscles/" not in items.select('a')[0]['href']:
                print (domain + items.select('a')[0]['href'])
                yield scrapy.Request(domain + items.select('a')[0]['href'], self.parse_detail)


    def parse_detail(self, response):
        domain = "http://www.exrx.net"
        checklist = []
        res = BeautifulSoup(response.body, 'lxml')
        for items in res.select('li'):
            if len(items('ul')) != 0:
                for i in items('a'):
                    if i['href'][5:] not in str(checklist):
                        yield scrapy.Request(domain + i['href'][5:], self.parse_detail_l2)
                        checklist.append(i['href'][5:])
        #    myfile.write('-----------------------------------------------------------------------------\n')

    def parse_detail_l2(self, response):
        new_path = '/users/TimLin/fitness/fitness/test.txt'
        domain = 'http://www.exrx.net/'
        res = BeautifulSoup(response.body, 'lxml')
        fitem = FitnessItem()
        fitem['exercisename'] = res.select('h1')[0].text.replace('\n','').replace('\r','').replace('   ','')
        fitem['gif'] = domain + res.select('img')[1]['src'][6:]
        fitem['video'] = res.select('iframe')[0]['src']
        fitem['preparation'] = res.select('td')[5]('dd')[0].text.replace('\n','').replace('\r','').replace('  ','')
        fitem['execution'] = res.select('td')[5]('dd')[1].text.replace('\n','').replace('\r','').replace('  ','')
        fitem['comments'] = res.select('td')[5]('dd')[2].text.replace('\n','').replace('\r','').replace('  ','')
        utilitylist = []
        for i in res.select('td')[6]('tr')[0]('a'):
            utilitylist.append(i.text)
        fitem['utility'] = utilitylist
        mechanicslist = []
        for i in res.select('td')[6]('tr')[1]('a'):
            mechanicslist.append(i.text)
        fitem['mechanics'] = mechanicslist
        forcelist = []
        for i in res.select('td')[6]('tr')[2]('a'):
            forcelist.append(i.text)
        fitem['force'] = forcelist
        ls = []
        for i in res.select('p'):
            if len(i('a')) != 0:
                ls.append(i('a')[0].text.replace('\n','').replace('\r','').replace('   ',''))
        for i in range(0,len(ls)):
            muls = []
            for j in res.select('ul')[i]('a'):
                muls.append(j.text.replace('\n','').replace('\r','').replace('   ',''))
            fitem[ls[i].lower().replace(' ','')] = muls
        return fitem
