from app.admin.post_model_view import PostModelView
from app.app_and_db import app, db
from app.articles.models import Post
from flask_admin import Admin
from flask_admin.contrib.sqla import ModelView

admin = Admin(app, name='Admin', template_mode='bootstrap3')
admin.add_view(PostModelView(Post, db.session))