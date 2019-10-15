from marshmallow import post_load

from flaskdemo import ma
from flaskdemo.models import Post, User


class PostSchema(ma.ModelSchema):

    class Meta:
        model = Post
        # fields = ('id', 'title')
    # user = ma.HyperlinkRelated("user_detail")


class UserSchema(ma.ModelSchema):
    class Meta:
        model = User

    # @post_load
    # def make_user(self, data, **kwargs):
    #     return User(**data)
