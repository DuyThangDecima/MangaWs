# coding=utf-8
LOG_FOLDER = ""
CAT_ICON_FOLDER = "/media/thangld/000970C6000D80A3/StoryStore/cat-icons"


DEBUG = True

if DEBUG:
    MONGO_MANGA_HOST = "127.0.0.1"
    MONGO_MANGA_PORT = 27017
    MONGO_MANGA_NAME = "sexy_manga"
    MONGO_MANGA_USER = None
    MONGO_MANGA_PASSWD = None

    RD_MANGA_HOST = "127.0.0.1"
    RD_MANGA_PORT = 6379
    RD_DB_INDEX = 1

    PATH_STORY_STORE_CRAWL = "/media/thangld/000970C6000D80A3/StoryStore/crawl"
    PATH_STORY_STORE_EPUB = "/media/thangld/000970C6000D80A3/StoryStore/epub"
    PATH_AVATAR_DEFAULT = ""
else:
    MONGO_MANGA_HOST = "45.32.119.115"
    MONGO_MANGA_PORT = 27017
    MONGO_MANGA_NAME = "manga"
    MONGO_MANGA_USER = "thangld-manga"
    MONGO_MANGA_PASSWD = "CVRlcMWOmtRV5UjzPbYcZTKs"

    RD_MANGA_HOST = "127.0.0.1"
    RD_MANGA_PORT = 6379
    RD_DB_INDEX = 1

    PATH_STORY_STORE_CRAWL = "/home/thangld/StoryStore/crawl"
    PATH_STORY_STORE_EPUB = "/home/thangld/StoryStore/epub"
    PATH_AVATAR_DEFAULT = "/home/thangld/StoryStore/crawl/"

NUM_PAGE_CAT = 10
