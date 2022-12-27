# Web content scraper for websites protected by CloudFlare
# Author: Rick Huang
# All rights reserved. Do not reproduce without consent.

import re
import cfscrape
import requests
from bs4 import BeautifulSoup

# Create a scraper object
scraper = cfscrape.create_scraper()

# Use the scraper to get the raw HTML content of the website
url = "https://www.reddit.com/r/CustomerService/comments/zc8vth/customer_treating_me_like_a_scam_artist/"
html = scraper.get(url).content

# Parse the HTML content using BeautifulSoup
soup = BeautifulSoup(html, 'html.parser')
print("[OUTPUT] soup = ", soup)

post_text_lst = []
# Pull post title and add to the list
post_text_lst.append(soup.find(href=re.compile("/r/CustomerService/")))
comments_lst = [] # one post has multiple comments

authors_list = soup.find(href=re.compile("/user/*"))
print("[DEBUG] authors_list = ", authors_list)
comment_authors_lst = []

content = []
src = []
title = []

for post in post_text_lst:
    title_RS = soup.find_all("title")
    title_ls = list(title_RS)
    content.append(post.previous.attrs['content'])
    print("[TODO] post content = ", content)
    # TODO: chain post content paragraphs into one item in the list for a given post
    # print("[DEBUG] title is of type ", type(title))
    src.append(post.attrs[['href'][0]])
    print("[OUTPUT] Post source = ", post.attrs[['href'][0]])
    title.append(title_ls)
    print("[OUTPUT] Post title = ", title_ls)
    comment_authors_lst.append(authors_list.attrs['href'])
    print("[OUTPUT] cmt_author = ", authors_list.attrs['href'])

    # for comment in post.attrs['']:
    #     print
    #     comments.append(comment)

# test


