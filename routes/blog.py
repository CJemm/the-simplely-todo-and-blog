from flask import (
    render_template,
    request,
    redirect,
    url_for,
    Blueprint,
)


from models.blog import (
    Blog,
    BlogComment,
)


main = Blueprint('blog', __name__)


@main.route("/")
def index():
    all_blog = Blog.all()
    return render_template("blog_index.html", blogs=all_blog)


@main.route("/add", methods=["POST"])
def add():
    form = request.form
    Blog.new(form)
    return redirect(url_for('.index'))


@main.route("/new", methods=["GET"])
def new():
    return render_template("blog_new.html")


@main.route("/<int:blog_id>", methods=["GET"])
def view(blog_id):
    comments = BlogComment.find_all(blog_id=blog_id)
    blog = Blog.find(blog_id)
    return render_template("blog_view.html", blog=blog, comments=comments)


@main.route("/comment/new", methods=["POST"])
def comment():
    form = request.form
    BlogComment.new(form)
    return redirect(url_for('.view', blog_id=form.get("blog_id")))