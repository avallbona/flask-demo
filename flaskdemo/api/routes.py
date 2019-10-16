from flask import Blueprint, current_app
from flask_restful import Api

from flaskdemo import apispec
from flaskdemo.api import schemas
from flaskdemo.api.resources import PostListResource, PostResource, UserListResource, UserResource

api_bp = Blueprint('api', __name__, url_prefix='/api')
api = Api(api_bp)

# posts
api.add_resource(PostListResource, '/post/')
api.add_resource(PostResource, '/post/<int:post_id>/')

# users
api.add_resource(UserListResource, '/user/')
api.add_resource(UserResource, '/user/<int:user_id>/')


@api_bp.before_app_first_request
def register_views():
    apispec.spec.components.schema("UserSchema", schema=schemas.UserSchema)
    apispec.spec.path(view=UserResource, app=current_app)
    apispec.spec.path(view=UserListResource, app=current_app)

    apispec.spec.components.schema("PostSchema", schema=schemas.PostSchema)
    apispec.spec.path(view=PostResource, app=current_app)
    apispec.spec.path(view=PostListResource, app=current_app)
