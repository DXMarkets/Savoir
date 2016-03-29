import requests
import json
from base64 import b64encode
import logging

log = logging.getLogger('Savoir')


class Savoir():
    __id_count = 0

    def __init__(self,
        rpcuser,
        rpcpasswd,
        rpchost,
        rpcport,
        chainname,
        rpc_call=None
    ):
        self.__rpcuser = rpcuser.encode('utf-8')
        self.__rpcpasswd = rpcpasswd.encode('utf-8')
        self.__rpchost = rpchost
        self.__rpcport = rpcport
        self.__chainname = chainname
        self.__auth_header = ' '.join(
            ['Basic', b64encode(':'.join([self.__rpcuser, self.__rpcpasswd]))]
            )
        self.__headers = {'Host': self.__rpchost,
            'User-Agent': 'Savoir v0.1',
            'Authorization': self.__auth_header,
            'Content-type': 'application/json'
            }
        self.__rpc_call = rpc_call

    def __getattr__(self, name):
        if name.startswith('__') and name.endswith('__'):
            # Python internal stuff
            raise AttributeError
        if self.__rpc_call is not None:
            name = "%s.%s" % (self.__rpc_call, name)
        return Savoir(self.__rpcuser,
            self.__rpcpasswd,
            self.__rpchost,
            self.__rpcport,
            self.__chainname,
            name)

    def __call__(self, *args):
        Savoir.__id_count += 1
        postdata = {'chain_name': self.__chainname,
            'version': '1.1',
            'params': args,
            'method': self.__rpc_call,
            'id': Savoir.__id_count}
        url = ''.join(['http://', self.__rpchost, ':', self.__rpcport])
        encoded = json.dumps(postdata)
        log.info("Request: %s" % encoded)
        r = requests.post(url, data=encoded, headers=self.__headers)
        if r.status_code == 200:
            log.info("Response: %s" % r.json())
            return r.json()['result']
        else:
            log.error("Error! Status code: %s" % r.status_code)
            log.error("Text: %s" % r.text)
            log.error("Json: %s" % r.json())
            return r.json()
