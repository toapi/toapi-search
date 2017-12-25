#!/usr/bin/env python
from urllib.parse import urlparse, parse_qs

from toapi import Css, Item


class Google(Item):
    __name__ = 'google'
    __base_url__ = 'https://www.google.com'

    url = Css('h3.r > a', attr='href')
    title = Css('h3.r > a')

    def clean_url(self, url):
        if isinstance(url, list) and len(url):
            url = url[0].get('href')
        return self.filter_link(link=url) if url else ''

    def clean_title(self, title):
        if isinstance(title, list) and len(title):
            text = ''
            for node in title[0].itertext():
                text += node
            title = text.strip()
        return title if title else ''

    @classmethod
    def filter_link(cls, link):
        """
        Returns None if the link doesn't yield a valid result.
        Token from https://github.com/MarioVilas/google
        :return: a valid result
        """
        try:
            # Valid results are absolute URLs not pointing to a Google domain
            # like images.google.com or googleusercontent.com
            o = urlparse(link, 'http')
            if o.netloc:
                return link
            # Decode hidden URLs.
            if link.startswith('/url?'):
                link = parse_qs(o.query)['q'][0]
                # Valid results are absolute URLs not pointing to a Google domain
                # like images.google.com or googleusercontent.com
                o = urlparse(link, 'http')
                if o.netloc:
                    return link
        # Otherwise, or on error, return None.
        except Exception as e:
            return ''

    class Meta:
        source = Css('div.g')
        route = {
            '/:wd': '/search?hl=en&q=:wd&btnG=Search&gbv=1',
        }
        web = {
            "with_ajax": False,
            "request_config": {
                'headers': {
                    'User-Agent': "Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; Win64; x64; Trident/5.0; .NET CLR 3.5.30729; .NET CLR 3.0.30729; .NET CLR 2.0.50727; Media Center PC 6.0)"
                },
                'proxies': {
                    'http': '0.0.0.0:8118',
                    'https': '0.0.0.0:8118'
                }
            },
            "headers": None
        }
