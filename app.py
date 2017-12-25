from toapi import Api
from items.google import Google
from items.bing import Bing
from items.baidu import Baidu
from settings import MySettings

api = Api(settings=MySettings)

api.register(Google)
api.register(Bing)
api.register(Baidu)

if __name__ == '__main__':
    api.serve()
