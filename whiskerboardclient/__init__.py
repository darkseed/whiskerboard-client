#!/usr/bin/python
import requests
import json
from datetime import datetime

__author__ = 'Tom Mulder <mulder.tom@gmail.com>'


class Whiskerboard(object):

    def __init__(self, user=('api', 'api'), host='localhost',
                 port=8000, protocol='http', api='/api/v1'):
        self.user = user[0]
        self.apikey = user[1]
        self.host = host
        self.port = port
        self.protocol = protocol
        self.api = "%s://%s:%d%s" % (protocol, host,
                                     port, api)

        self.headers = {
            'Content-Type': 'application/json',
            'Accept': '*/*'
        }

    def _get_uri(self, endpoint, name):
        name = name.lower()
        response = requests.get('%s/%s/?slug=%s' % (self.api, endpoint, name),
                                headers=self.headers)
        uri = json.loads(response.content)['objects'][0]['resource_uri']
        return uri

    def get_status_uri(self, name):
        return self._get_uri('statuses', name)

    def get_service_uri(self, name):
        return self._get_uri('services', name)

    def update_status(self, status, message, service):
        status_uri = self.get_status_uri(status)
        service_uri = self.get_service_uri(service)

        self.headers['Authorization'] = 'ApiKey %s:%s' % (self.user,
                                                          self.apikey)

        params = {
            'informational': False,
            'message': '%s' % message,
            'service': '%s' % service_uri,
            'start': '%s' % datetime.now(),
            'status': '%s' % status_uri
        }

        api_url = '%s/%s/' % (self.api, 'events')
        response = requests.post(api_url, data=json.dumps(params),
                                 headers=self.headers)
        return response




