from pymongo import MongoClient
from redis import StrictRedis
import config


class MongoDb:
    # Here will be the instance stored.
    __instance = None
    db = None

    @staticmethod
    def getInstance():
        """ Static access method. """
        if MongoDb.__instance is None:
            MongoDb()
        return MongoDb.__instance

    def __init__(self):
        """ Virtually private constructor. """
        if MongoDb.__instance is not None:
            raise Exception("This class is a singleton!")
        else:
            MongoDb.__instance = self
            client = MongoClient(config.MONGO_MANGA_HOST, config.MONGO_MANGA_PORT)
            self.db = client[config.MONGO_MANGA_NAME]
            if config.MONGO_MANGA_USER:
                self.db.authenticate(name=config.MONGO_MANGA_USER,password=config.MONGO_MANGA_PASSWD)
            # self.db["x"].initialize_ordered_bulk_op()


class RedisDb:
    __instance = None
    db = None

    @staticmethod
    def getInstance():
        """ Static access method. """
        if RedisDb.__instance is None:
            RedisDb()
        return RedisDb.__instance

    def __init__(self):
        """ Virtually private constructor. """
        if RedisDb.__instance is not None:
            raise Exception("This class is a singleton!")
        else:
            RedisDb.__instance = self
            self.db = StrictRedis(host=config.RD_MANGA_HOST, port=config.RD_MANGA_PORT, db=config.RD_DB_INDEX)
