from flask import Flask
from logging.handlers import RotatingFileHandler
import logging
from api.category import cat_bprint
from api.chapter import chapter_bprint
from api.story import story_bprint

app = Flask(__name__)

app.debug = True


def config():
    app.config.from_pyfile("config.py")
    add_handler_log()
    regis_blueprint()


def add_handler_log():
    logHandler = RotatingFileHandler('/media/thangld/000970C6000D80A3/Project/Server/MangaWs/info.log', maxBytes=10000,
                                     backupCount=10)

    # set the app logger level
    logHandler.setLevel(logging.DEBUG)
    app.logger.addHandler(logHandler)

    logging.getLogger('werkzeug').setLevel(logging.DEBUG)
    logging.getLogger('werkzeug').addHandler(logHandler)
    logging.getLogger('werkzeug').addHandler(logging.StreamHandler())
    app.logger.addHandler(logHandler)
    app.logger.setLevel(logging.DEBUG)


def regis_blueprint():
    app.register_blueprint(cat_bprint, url_prefix="/cat")
    app.register_blueprint(chapter_bprint, url_prefix="/chap")
    app.register_blueprint(story_bprint, url_prefix="/story")


if __name__ == '__main__':
    config()
    app.run(host="0.0.0.0")
