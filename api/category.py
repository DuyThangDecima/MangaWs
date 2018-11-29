from flask import Blueprint, render_template, send_file, current_app, jsonify, make_response, abort
from flask_restful import Resource, Api
import os
from database.models import CategoryModel

cat_bprint = Blueprint('category', __name__)
cat_api = Api(cat_bprint)


class CategoryName(Resource):
    def get(self):
        try:
            cat_model = CategoryModel()
            res = cat_model.get_all()
            return jsonify(res)
        except Exception as e:
            return make_response(jsonify(message="error"), 500)


class CategoryIcon(Resource):
    def get(self, file_name):
        folder = current_app.config["CAT_ICON_FOLDER"]
        return send_file(os.path.join(folder, file_name))


cat_api.add_resource(CategoryName, '/name/')
cat_api.add_resource(CategoryIcon, '/icon/<string:file_name>/')
