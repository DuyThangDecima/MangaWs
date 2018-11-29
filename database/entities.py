class Proxy(object):
    def __init__(self, ip, port, provider):
        self.ip = ip
        self.port = port
        self.provider = provider  # provider proxy


class Category:
    """
    Category of manga
    """
    category_id = None
    category_name = None
    sub_categories = None  # array of category

    def __init__(self):
        pass

        # def __init__(self, category_id, category_name, sub_categories):
        #     self.category_id = category_id
        #     self.category_name = category_name
        #     self.sub_categories = sub_categories


class Story:
    store_id = None
    story_id = None
    category_id = None
    sub_cat_id = None
    story_name = None
    number_chap = None

    last_update = None

    def __init__(self, store_id=None, story_id=None, category_id=None, sub_cat_id=None, story_name=None,
                 number_chap=None, chapters=None, sub_categories=None, last_update=None):
        self.store_id = store_id
        self.story_id = story_id
        self.category_id = category_id
        self.sub_cat_id = sub_cat_id
        self.story_name = story_name
        self.number_chap = number_chap
        self.chapters = chapters
        self.sub_categories = sub_categories
        self.last_update = last_update


class Chapter:
    story_id = None
    chap_id = None
    chap_url = None
    is_crawl = None
    path = None

    def __init__(self, story_id, chap_id, chap_url, is_crawl=False, path=None):
        self.story_id = story_id
        self.chap_id = chap_id
        self.chap_url = chap_url
        self.is_crawl = is_crawl
        self.path = path

class Avatar:
    story_id = None
    url = None
    is_crawl = None
    path = None

    def __init__(self, story_id, url, is_crawl=False, path=None):
        self.story_id = story_id
        self.url = url
        self.is_crawl = is_crawl
        self.path = path
