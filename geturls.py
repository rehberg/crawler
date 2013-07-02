#-------------------------------------------------------------------------------
# Name:        geturls.py
# Purpose:     Grabs URLs from pages
#
# Author:      Ben Rehberg
#
# Created:     July 1, 2013
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
        links = print_all_links(get_page(url))
        for link in links:
            content = get_page(link)
            if content:
                print_all_links(content)

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

def next_http_target(page):
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
    return {'User-Agent':'TwoLeg-Crawler/1.0 Python-urllib/3.3'}

def base_url(url):
    """Returns the root URL from a given url, ending
    with a slash just after the tld."""
    start = url.find('://')
    slash = url.find('/', start+3)
    return url[:slash+1]

def can_scrape(url):
    """Takes a url and looks for robots.txt.
    Returns true if robots.txt allows crawling."""
    rp = urllib.robotparser.RobotFileParser()
    rp.set_url(base_url(url)+'robots.txt')
    rp.read()
    rp.can_fetch('*', url)

if __name__ == '__main__':
    main()
