from marshmallow import fields

from flaskdemo import ma
from flaskdemo.models import Post, User


class PostSchema(ma.ModelSchema):
    id = fields.Integer(dump_only=True)

    class Meta:
        model = Post
        # fields = ('id', 'title')
    # author = ma.HyperlinkRelated("api.user_detail")


class UserSchema(ma.ModelSchema):
    id = fields.Integer(dump_only=True)
    email = fields.Email(required=True)
    password = fields.String(load_only=True)

    class Meta:
        model = User
