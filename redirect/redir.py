
class RedirectException(Exception):
    def __init__(self, msg):
        super(Exception, self).__init__(msg)

class DataStore(object):
    """Our abstracted datastore. This base class is just a dictionary. 
    Subclass this and override the __setitem__, __getitem__, and get
    methods to use some other storage."""

    def __init__(self):
        self.data = {}

    def __setitem__(self, k, v):
        self.data[k] = v

    def __getitem__(self, k):
        return self.data[k]

    def get(self, k):
        return self.data.get(k)

    def redirect(self, url):
        """Really basic redirect algorithm with cycle detection."""
        # todo: use Flask's redirect support
        seen_urls = set([url])
        from_url = url
        while True:
            to_url = self.get(from_url)
            if to_url is None:
                break
            if to_url in seen_urls:
                raise RedirectException('Saw redirect loop with key {0}'.format(url))
            from_url = to_url
        return from_url

