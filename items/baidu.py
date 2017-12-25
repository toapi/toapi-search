#!/usr/bin/env python
from toapi import Css

from .bing import Bing


class Baidu(Bing):
    __name__ = 'baidu'
    __base_url__ = 'http://www.baidu.com'

    url = Css('h3.t a', attr='href')
    title = Css('h3.t a')

    class Meta:
        source = Css('div.result')
        route = {'/:wd': '/s?wd=:wd&ie=utf-8&vf_bl=1'}
