import unittest
from tests.your_api_key import api_key
from topicsio import Topicsio

class ClientTestCase(unittest.TestCase):
    
    def setUp(self):
        self.client = Topicsio(api_key)
        
    def test_response_search_topics_without_entity(self):
        response = self.client.search_topics('redis')
        self.check_json_content(response)
 
        self.assertEquals( {u'query': u'redis', u'page': 1}, response['request'])
        
    def test_response_search_topics_with_entity(self):
        response = self.client.search_topics('redis', 'computers')
        self.check_json_content(response)

        self.assertEquals( {u'query': u'redis', u'page': 1, u'entity': u'computers'}, 
                           response['request'])
        
    def test_subscribe_unsubscribe_topics(self):
        search_topics = self.client.search_topics('test')
        existing_topic_id = search_topics['response']['topics'][0]['id']
        
        response = self.client.subscribe_topic(existing_topic_id)
        self.check_json_content(response)
        
        response = self.client.unsubscribe_topic(existing_topic_id)
        self.check_json_content(response)

    def test_response_list_topics(self):
        response = self.client.list_topics()
        self.check_json_content(response)
                        
    def test_response_get_last_news(self):
        response = self.client.get_last_news()
        self.check_json_content(response)
        
    def test_response_get_last_news_by_topic(self):
        list_topics = self.client.list_topics()
        existing_topic_id = list_topics['response']['topics'][0]['id']
        
        response = self.client.get_last_news(topic_id=existing_topic_id)
        self.check_json_content(response)
        
    def check_json_content(self, response):
        self.assert_( response.has_key( 'response'))