from flask import Blueprint
from flask_restful import Api

from flaskdemo.api.resources import PostListResource, PostResource, UserListResource, UserResource

api_bp = Blueprint('api', __name__, url_prefix='/api')
api = Api(api_bp)

# posts
api.add_resource(PostListResource, '/post/')
api.add_resource(PostResource, '/post/<int:post_id>/')

# users
api.add_resource(UserListResource, '/user/')
api.add_resource(UserResource, '/user/<int:user_id>/')
