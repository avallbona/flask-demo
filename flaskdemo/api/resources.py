from flask_restful import Resource, abort
from flaskdemo.models import Post


def get_or_404(todo_id):
    post = Post.query.get(todo_id)
    if not post:
        abort(404, message="Post {} doesn't exist".format(todo_id))
    return post


class PostResource(Resource):

    def get(self, id):
        post = get_or_404(id)
        result = {'id': post.id, 'title': post.title}
        return result

    def put(self, id):
        pass

    def delete(self, id):
        pass


class PostListResource(Resource):

    def get(self):
        posts = Post.query.all()
        result = [{'id': it.id, 'title': it.title} for it in posts]
        return result

    def post(self):
        pass
