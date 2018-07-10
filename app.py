from flask import Flask

from routes.todo import main as todo_routes
from routes.comment import main as comment_routes
from routes.session_exp import main as session_routes
from routes.blog import main as blog_routes
from routes.index import main as index_routes


app = Flask(__name__)
app.secret_key = 'test for good'


app.register_blueprint(todo_routes, url_prefix='/todo')
app.register_blueprint(comment_routes, url_prefix='/comment')
app.register_blueprint(session_routes, url_prefix='/session')
app.register_blueprint(blog_routes, url_prefix='/blog')
app.register_blueprint(index_routes)


if __name__ == '__main__':
    config = dict(
        debug=True,
        host='0.0.0.0',
        port=2000,
    )
    app.run(**config)
