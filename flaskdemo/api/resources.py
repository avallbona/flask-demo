from flask_restful import Resource, reqparse

from flaskdemo import db
from flaskdemo.models import Post


def get_or_404(post_id):
    return Post.query.filter_by(id=post_id).first_or_404(description=f'Post {post_id} not found')


class PostResource(Resource):

    def get(self, post_id):
        post = get_or_404(post_id)
        result = {'id': post.id, 'title': post.title, 'content': post.content}
        return result

    def delete(self, post_id):
        post = get_or_404(post_id)
        db.session.delete(post)
        db.session.commit()
        return {}, 204

    def put(self, post_id):
        parser = reqparse.RequestParser()
        parser.add_argument('title', type=str, help='Title of the post')
        parser.add_argument('content', type=str, help='Content of the post')
        args = parser.parse_args()
        post = get_or_404(post_id=post_id)
        post.title = args.get('title')
        post.content = args.get('content')
        db.session.commit()
        return {'id': post_id, 'title': post.title, 'content': post.content}


class PostListResource(Resource):

    def get(self):
        posts = Post.query.all()
        result = [{'id': it.id, 'title': it.title} for it in posts]
        return result

    def post(self):
        parser = reqparse.RequestParser()
        parser.add_argument('title', type=str, help='Title of the post')
        parser.add_argument('content', type=str, help='Content of the post')
        parser.add_argument('user_id', type=int, help='Id of the user')
        args = parser.parse_args()
        post = Post(title=args.get('title'), content=args.get('content'), user_id=args.get('user_id'))
        db.session.add(post)
        db.session.commit()
        return {'id': post.id, 'title': post.title, 'content': post.content}
