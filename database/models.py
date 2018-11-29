# coding=utf-8
from database.db import MongoDb, RedisDb
from database.entities import *
from bson import ObjectId

9
class ColModel():
    col_name = None
    col_connect = None
    db = MongoDb.getInstance().db

    def get_col_connect(self):
        return self.db[self.col_name]


class ProxyModel(ColModel):
    """
    Danh sách proxy
    """
    col_name = "proxy"

    def get_active_proxy(self):
        """
        Get list proxy and sort by last_update
        :return: 
        """
        cursor = self.get_col_connect().find(
            {
                "status": True
            }
        ).sort("last_update", -1)
        result = []
        for item in cursor:
            result.append(Proxy(item["ip"], item["port"], item["provider"]))
        return result


class CategoryModel(ColModel):
    """
    Các category truyện
    Mô hình:
        category_name:
        category_id:
        sub_categories:
            [
                {category_id,category_name,sub_categories}
            ]
    """
    col_name = "category"

    def get_all(self):
        data = []
        for item in self.get_col_connect().find({}, {"_id": 1, "name": 1, "path": 1}):
            data.append(
                {
                    "id": item["_id"],
                    "name": item["name"],
                    "path": item.get("path", None)
                }
            )
        return data


class StoryModel(ColModel):
    """
    Các category truyện
    Mô hình:
        category_name:
        category_id:
        sub_categories:
            [
                {category_id,category_name,sub_categories}
            ]
    """
    col_name = "story"

    def get_top_favorite(self, limit=100):
        favorites = []
        data = self.get_col_connect().find({}, {"favorite": 1, "_id": 1}) \
            .limit(limit) \
            .sort("favorite", -1)
        for item in data:
            content = {
                'rmt_id': str(item['_id']),
                "title": item['story_name'],
                "ava": item['ava'],
                "author": item.get('author', 'Unknown'),
                "num_chap": item['number_chapter'],
                "favorite": item.get('favorite', 1),
                "popular": item.get('popular', 1),
                "content_update": item.get('content_update', None),
            }
            favorites.append(content)
        return favorites

    def get_top_popular(self, limit=100):
        populars = []
        data = self.get_col_connect().find(
            {
                "number_chapter": {"$exists": True},
                "chapters": {"$exists": True},
                "ava.path": {"$exists": True},

            },
            {
                "_id": 1,
                "story_name": 1,
                "ava": 1,
                "author": 1,
                "number_chapter": 1,
                "favorite": 1,
                "popular": 1,
                "content_update": 1
            }
        ) \
            .limit(limit) \
            .sort("popular", -1)
        for item in data:
            # Chi lay ten file thoi
            ava = item['ava'].get("path", None)
            if ava:
                ava = ava.split("/")[-1]

            content = {
                'rmt_id': str(item['_id']),
                "name": item['story_name'],
                "ava": ava,
                "author": item.get('author', 'Unknown'),
                "num_chap": item['number_chapter'],
                "favorite": item.get('favorite', 1),
                "popular": item.get('popular', 1),
                "content_update": item.get('content_update', None),
            }
            populars.append(content)
        return populars

    def get_by_category(self, cat_id, from_val, count):
        cat_stoies = []
        data = self.get_col_connect().find(
            {
                "cats": cat_id  # field `cats` contain `cat_id`
            },
            {
                "_id": 1,
                "story_name": 1,

            }
        ).skip(from_val).limit(count)
        for item in data:
            cat_stoies.append(
                {
                    "id": str(item["_id"]),
                    "story_name": item["_id"]
                }
            )
        return cat_stoies

    def get_avatar(self, _id):
        value = self.get_col_connect().find_one({"_id": ObjectId(_id)}, {"ava": 1})
        if value and "ava" in value:
            return True, value['ava'].get('path', None)
        return False, None

    def increase_favorite(self, _id):
        # TODO
        self.get_col_connect().find_one()


class StoreModel(ColModel):
    """
    Các category truyện
    Mô hình:
        category_name:
        category_id:
        sub_categories:
            [
                {category_id,category_name,sub_categories}
            ]
    """
    col_name = "store"
