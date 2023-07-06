import base64
from w3lib.http import basic_auth_header 

class ProxiesMiddleware(object):
    def __init__(self, settings):
        self.proxy_auth = settings.get('PROXY_AUTH')

    @classmethod
    def from_crawler(cls, crawler):
        return cls(crawler.settings)

    def process_request(self, request, spider):
        request.meta['proxy'] = "http://p.webshare.io:80"
        request.headers['Proxy-Authorization'] = basic_auth_header("ltyaszoc-rotate", "mhw092eawi3z")
