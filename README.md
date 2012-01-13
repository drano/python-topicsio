# python-topicsio

The Python interface to the Topics.io backend. 
Topics.io is a free API used to add relevant news from topics into your apps.

## Installation

    $ sudo pip install python-topicsio

or alternatively (you really should be using pip though):

    $ sudo easy_install python-topicsio

From source:

    $ sudo python setup.py install


## Getting Started

    >>> import topicsio
    >>> client = topicsio.Topicsio(auth_api_key='Your api key')
    >>> all_last_news = client.get_last_news()
 
Author
------

python-topicsio is developed and maintained by Didier Rano (didier.rano@gmail.com).
It can be found here: http://github.com/drano/python-topicsio

Special thanks to:

* Wesley Bouarab, topics.io co-founder.
