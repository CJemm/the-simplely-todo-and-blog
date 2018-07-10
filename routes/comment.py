from flask import (
    render_template,
    request,
    redirect,
    url_for,
    Blueprint,
)


from models.comment import Comment
from models.todo import Todo
from utils import log


main = Blueprint('comment', __name__)

@main.route('/')
def index():
    comments = Comment.all()
    return render_template('comment.html', comments = comments)


@main.route('/add', methods=['POST'])
def add():
    t = Comment.new(request.form)
    t.save()
    return redirect(url_for('.index'))


@main.route('/delete/<int:todo_id>/')
def delete(todo_id):
    t = Todo.delete(todo_id)
    log("deleted todo id", todo_id)
    return redirect(url_for('.index'))
