from flask import request
from flask_restful import Resource
from marshmallow import ValidationError

from flaskdemo import db, bcrypt
from flaskdemo.api.errors import bad_request
from flaskdemo.api.schemas import PostSchema, UserSchema
from flaskdemo.models import Post, User


def get_post_or_404(post_id):
    return Post.query.get_or_404(post_id, description=f'Post {post_id} not found')


def get_user_or_404(user_id):
    return User.query.get_or_404(user_id, description=f'User {user_id} not found')


class PostResource(Resource):
    """Single object resource

    ---
    get:
      tags:
        - Post
      parameters:
        - in: path
          name: post_id
          schema:
            type: integer
      responses:
        200:
          content:
            application/json:
              schema:
                PostSchema
        404:
          description: post does not exists
    put:
      tags:
        - Post
      parameters:
        - in: path
          name: post_id
          schema:
            type: integer
      requestBody:
        content:
          application/json:
            schema:
              PostSchema
      responses:
        200:
          content:
            application/json:
              schema:
                PostSchema
        404:
          description: post does not exists
    delete:
      tags:
        - Post
      parameters:
        - in: path
          name: post_id
          schema:
            type: integer
      responses:
        204:
          description: no content
        404:
          description: post does not exists
    """
    def get(self, post_id):
        post = get_post_or_404(post_id)
        post_schema = PostSchema()
        return post_schema.dump(post)

    def delete(self, post_id):
        post = get_post_or_404(post_id)
        db.session.delete(post)
        db.session.commit()
        return {}, 204

    def put(self, post_id):
        old_post = get_post_or_404(post_id=post_id)
        post_schema = PostSchema()
        raw_data = request.get_json() or {}
        try:
            post = post_schema.load(data=raw_data, instance=old_post)
        except ValidationError as e:
            return bad_request(str(e))
        db.session.commit()
        return post_schema.dump(post)


class PostListResource(Resource):
    """Creation and get_all

    ---
    get:
      tags:
        - Post
      responses:
        200:
         content:
           application/json:
             schema:
               allOf:
                 - type: array
                   items:
                     $ref: '#/components/schemas/PostSchema'

    post:
      tags:
        - Post
      requestBody:
        content:
          application/json:
            schema:
              PostSchema
      responses:
        201:
          content:
            application/json:
              schema:
                PostSchema
    """
    def get(self):
        post_schema = PostSchema(many=True)
        return post_schema.dump(Post.query.all())

    def post(self):
        post_schema = PostSchema()
        raw_data = request.get_json() or {}
        try:
            post = post_schema.load(data=raw_data)
        except ValidationError as e:
            return bad_request(str(e))
        db.session.add(post)
        db.session.commit()
        return post_schema.dump(post), 201


class UserResource(Resource):
    """Single object resource

    ---
    get:
      tags:
        - User
      parameters:
        - in: path
          name: user_id
          schema:
            type: integer
      responses:
        200:
          content:
            application/json:
              schema:
                UserSchema
        404:
          description: user does not exists
    put:
      tags:
        - User
      parameters:
        - in: path
          name: user_id
          schema:
            type: integer
      requestBody:
        content:
          application/json:
            schema:
              UserSchema
      responses:
        200:
          content:
            application/json:
              schema:
                UserSchema
        404:
          description: user does not exists
    delete:
      tags:
        - User
      parameters:
        - in: path
          name: user_id
          schema:
            type: integer
      responses:
        204:
          description: no content
        404:
          description: user does not exists
    """

    def get(self, user_id):
        user = get_user_or_404(user_id)
        user_schema = UserSchema()
        return user_schema.dump(user)

    def delete(self, user_id):
        user = get_user_or_404(user_id)
        db.session.delete(user)
        db.session.commit()
        return {}, 204

    def put(self, user_id):
        old_user = get_user_or_404(user_id=user_id)
        user_schema = UserSchema()
        raw_data = request.get_json() or {}
        try:
            user = user_schema.load(data=raw_data, instance=old_user)
            user.password = bcrypt.generate_password_hash(user.password).decode("utf-8")
        except ValidationError as e:
            return bad_request(str(e))
        db.session.commit()
        return user_schema.dump(user)


class UserListResource(Resource):
    """Creation and get_all

    ---
    get:
      tags:
        - User
      responses:
        200:
         content:
           application/json:
             schema:
               allOf:
                 - type: array
                   items:
                     $ref: '#/components/schemas/UserSchema'

    post:
      tags:
        - User
      requestBody:
        content:
          application/json:
            schema:
              UserSchema
      responses:
        201:
          content:
            application/json:
              schema:
                UserSchema
    """

    def get(self):
        user_schema = UserSchema(many=True)
        return user_schema.dump(User.query.all())

    def post(self):
        user_schema = UserSchema()
        raw_data = request.get_json() or {}
        try:
            user = user_schema.load(data=raw_data)
            user.password = bcrypt.generate_password_hash(user.password).decode("utf-8")
        except ValidationError as e:
            return bad_request(str(e))
        db.session.add(user)
        db.session.commit()
        return user_schema.dump(user)
