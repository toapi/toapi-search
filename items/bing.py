#!/usr/bin/env python
from toapi import Css, Item


class Bing(Item):
    __name__ = 'bing'
    __base_url__ = 'https://www.bing.com'

    url = Css('h2 a', attr='href')
    title = Css('h2 a')

    def clean_url(self, url):
        if isinstance(url, list) and len(url):
            url = url[0].get('href')
        return url if url else ''

    def clean_title(self, title):
        if isinstance(title, list) and len(title):
            text = ''
            for node in title[0].itertext():
                text += node
            title = text.strip()
        return title if title else ''

    class Meta:
        source = Css('li.b_algo')
        route = {'/:wd': '/search?q=:wd&ensearch=1'}
