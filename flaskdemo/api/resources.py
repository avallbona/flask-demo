from flask_restful import Resource

from flaskdemo import db
from flaskdemo.models import Post


def get_or_404(post_id):
    return Post.query.filter_by(id=post_id).first_or_404(description=f'Post {post_id} not found')


class PostResource(Resource):

    def get(self, post_id):
        post = get_or_404(post_id)
        result = {'id': post.id, 'title': post.title}
        return result

    def delete(self, post_id):
        post = get_or_404(post_id)
        db.session.delete(post)
        db.session.commit()
        return {}, 204

    def put(self, post_id):
        post = get_or_404(post_id=post_id)
        pass


class PostListResource(Resource):

    def get(self):
        posts = Post.query.all()
        result = [{'id': it.id, 'title': it.title} for it in posts]
        return result

    def post(self):
        pass
