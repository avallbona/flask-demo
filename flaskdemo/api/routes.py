from flask import Blueprint
from flask_restful import Api

from flaskdemo.api.resources import PostListResource, PostResource

api_bp = Blueprint('api', __name__, url_prefix='/api')
api = Api(api_bp)
api.add_resource(PostListResource, '/post/')
api.add_resource(PostResource, '/post/<int:id>/')



