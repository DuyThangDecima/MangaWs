from flask import Blueprint, render_template, make_response, jsonify
from flask_restful import Resource, Api
from database.models import StoryModel
from bson import ObjectId

chapter_bprint = Blueprint('manga', __name__)
chapter_api = Api(chapter_bprint)
story_model = StoryModel()


@chapter_api.representation('application/json')
class ChapTitle(Resource):
    def get(self, _id):
        db = story_model.get_col_connect()
        res = db.find_one(
            {
                "_id": ObjectId(_id)
            },
            {
                "chapters": 1
            })
        if not res:
            return make_response(jsonify(message="story not found"), 400)

        chapters = []
        for chap in res["chapters"]:
            chapters.append(
                {
                    "chap_id":chap["chap_id"],
                    "chap_title":chap["chap_title"]
                }
            )

        return jsonify(chapters)

@chapter_api.representation('application/json')
class ChapContent(Resource):
    def get(self,_id):
        # get chap_id
        pass

chapter_api.add_resource(ChapTitle, '/title/<string:_id>')
chapter_api.add_resource(ChapContent, '/content/<string:_id>')
