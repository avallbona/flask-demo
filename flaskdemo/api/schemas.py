from marshmallow import post_load

from flaskdemo import ma
from flaskdemo.models import Post, User


class PostSchema(ma.ModelSchema):

    class Meta:
        model = Post
        # fields = ('id', 'title')
    # author = ma.HyperlinkRelated("api.user_detail")


class UserSchema(ma.ModelSchema):
    class Meta:
        model = User
