from flask import Blueprint, make_response, jsonify, current_app as app, send_file
from flask_restful import Resource, Api
from database.models import StoryModel
from flask_restful import reqparse
import os
import traceback

story_bprint = Blueprint('story', __name__)
story_api = Api(story_bprint)
story_model = StoryModel()


@story_api.representation('application/json')
class Favorite(Resource):
    def get(self):
        try:
            parser = reqparse.RequestParser(bundle_errors=True)
            parser.add_argument('count', type=int, default=50)

            parsed_args = parser.parse_args()
            count = parsed_args.get("count")
            return jsonify(story_model.get_top_favorite(limit=count))
        except Exception as e:
            print(e)
            app.logger.error(e)
            return make_response(jsonify(message="error"), 500)

    def put(self, id):
        try:
            # TODO
            print("TEST")
        except Exception as e:
            app.logger.error(e)
            return make_response(jsonify(message="error"), 500)


class LatestUpdate(Resource):
    def get(self):
        pass


class Popular(Resource):
    def get(self):
        try:
            parser = reqparse.RequestParser(bundle_errors=True)
            parser.add_argument('count', type=int, default=50)

            parsed_args = parser.parse_args()
            count = parsed_args.get("count")

            return jsonify(story_model.get_top_popular(limit=count))
        except Exception as e:
            print(e)
            app.logger.error(e)
            return make_response(jsonify(message="error"), 500)


class Avatar(Resource):
    def get(self, _id):
        """
        id of story
        :param _id: 
        :return: 
        """
        try:
            exists, path_rel = story_model.get_avatar(_id)
            path = os.path.join(app.config["PATH_STORY_STORE_CRAWL"], path_rel)
            if not exists:
                return make_response(jsonify(message="story id not found"), 400)

            if not path or not os.path.exists(path):
                path = app.config["PATH_AVATAR_DEFAULT"]
            return send_file(path)
        except Exception as e:
            print(traceback.print_exc())
            app.logger.error(e)
            return make_response(jsonify(message="error"), 500)


story_api.add_resource(Favorite, '/favorite/')
story_api.add_resource(Popular, '/popular/')
story_api.add_resource(Avatar, '/avatar/<string:_id>')
