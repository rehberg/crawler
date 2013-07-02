#!/usr/bin/python3
#-------------------------------------------------------------------------------
# Name:        geturls.py
# Purpose:     Grabs URLs from pages
# Platform:    written on Python 3.2.3
# Author:      Ben Rehberg, Two Leg Software
#	       ben@twoleg.com
# Created:     01/07/2013
# Copyright:   (c) Ben Rehberg 2013
# More Information: http://www.twoleg.com, if I bothered to publish something there...
# Licence:     GPL
#-------------------------------------------------------------------------------

import urllib.request
from time import sleep

def main():
    url = 'http://www.benrehberg.com'
    page = get_page(url)
    if page:
        links = write_links_to_file(get_page(url))
        for link in links:
            content = get_page(link)
            if content:
                write_links_to_file(content)

def get_page(url):
    """Takes a <string> url and returns a <string>
    with the page's contents."""
    header = create_header()
    req = urllib.request.Request(url, header)
    pObj = urllib.request.urlopen(req)
    pByt = pObj.read()
    try:
        page = pByt.decode('utf-8')
    except UnicodeDecodeError:
        return None
    return page


def write_links_to_file(page):
    a = []
    f = open('links.txt', 'a')
    while True:
        url, endpos = next_http_target(page)
        if url:
            a.append(url)
            f.write(url + '\n')
            f.flush()
            page = page[endpos:]
        else:
            f.close()
            return a

def next_http_target(page):
    """Takes a <string> page and picks all the '<a href=' text elements
    from it.  Only returns those beginning with 'http'"""
    start_link = page.find('<a href=')
    if start_link == -1:
        return None, 0
    start_quote = page.find('"', start_link)
    end_quote = page.find('"', start_quote + 1)
    url = page[start_quote + 1:end_quote]
    if url.find('http',0) != -1:
        return url, end_quote
    else:
        return None, end_quote





def get_next_target(page):
    start_link = page.find('<a href=')
    if start_link == -1:
        return None, 0
    start_quote = page.find('"', start_link)
    end_quote = page.find('"', start_quote + 1)
    url = page[start_quote + 1:end_quote]
    return url, end_quote


def print_all_links(page):
    a = []
    while True:
        url, endpos = next_http_target(page)
        if url:
            a.append(url)
            print(url)
            page = page[endpos:]
        else:
            return a

def create_header():
    header = {'User-Agent':'TwoLeg-Crawler/1.0 Python-urllib/3.3'}

if __name__ == '__main__':
    main()

