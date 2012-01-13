import urllib
import httplib
import json

class Topicsio(object):
    '''
    Topics.io API Handler

    Parameters
    ----------
    auth_api_key : string the Topics.io API Key.

    '''
    API_URL = 'api.topics.io'

    def __init__(self, auth_api_key):
        self._auth_api_key = auth_api_key

    def make_api_call(self, verb_http, method_url, page=None, params={}):
        params['page'] = page
        url = self._build_url(method_url, params)
        
        conn = httplib.HTTPConnection(self.API_URL)
        conn.request(verb_http, url)
        resp = conn.getresponse()
        
        data = resp.read()
        data = json.loads(data)
        
        return data
        
    def _build_url(self, method_url, params):
        all_params = {'auth_api_key': self._auth_api_key}
        params_not_none = dict((k, v) for (k, v) in params.iteritems() if v is not None)
        all_params.update(params_not_none)

        return "%s?%s" % (method_url, urllib.urlencode( all_params))
      
    def search_topics(self, query, entity=None, page=1):
        verb_http = 'GET'
        method_url = '/topics/search/v1/'
        return self.make_api_call( verb_http, method_url, page, {'query': query, 'entity': entity})
                  
    def subscribe_topic(self, topic_id):
        verb_http = 'POST'
        method_url = '/topics/%s/subscribe/v1/' % topic_id
        return self.make_api_call( verb_http, method_url)
        
    def unsubscribe_topic(self, topic_id):
        verb_http = 'DELETE'
        method_url = '/topics/%s/subscribe/v1/' % topic_id
        return self.make_api_call( verb_http, method_url)

    def list_topics(self, page=1):
        verb_http = 'GET'
        method_url = '/topics/v1/'
        return self.make_api_call( verb_http, method_url, page)
        
    def create_topic(self, display_name, entity):
        verb_http = 'POST'
        method_url = '/topics/v1/'
        return self.make_api_call( verb_http, method_url, 
                                   page=None, params={'displayName': display_name, 'entity': entity})
                        
    def get_last_news(self, topic_id=None, page=1):
        verb_http = 'GET'
        if topic_id is None:
            method_url = '/topics/news/v1/'
        else:
            method_url = '/topics/%s/news/v1/' % topic_id
        return self.make_api_call( verb_http, method_url, page)