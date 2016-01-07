from app.app_and_db import app
from app.articles.models import Post
from datetime import datetime
from flask import abort, Blueprint, flash, render_template, redirect, url_for

articles = Blueprint('articles', __name__, template_folder='templates/articles')

@articles.route('/', defaults={'page': 1})
@articles.route('/page/<int:page>')
def index(page):
  articles = Post.query.filter(Post.visibility=="Published").filter(Post.published_date <= datetime.now()).order_by(Post.published_date.desc()).paginate(page, app.config["POSTS_PER_PAGE"])
  return render_template('articles/index.html', articles=articles)

@articles.route('/<string:slug>')
def post(slug):
  article = Post.query.get_or_404(slug)
  if article.is_visible():
    return render_template('articles/article.html', article=article)
  return abort(404)

app.register_blueprint(articles, url_prefix='/article')
app.register_blueprint(articles, url_prefix='/blog')
app.register_blueprint(articles, url_prefix='/post')