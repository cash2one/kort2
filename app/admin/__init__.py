from app.admin.auth_view import AuthView
from app.admin.post_model_view import PostModelView
from app.admin.short_link_model_view import ShortLinkModelView
from app.app_and_db import app, db
from app.articles.models import Post
from app.pages.models import ShortLink
from app.users.models import Role, User
from flask_admin import Admin

admin = Admin(app, name='Admin', template_mode='bootstrap3')
admin.add_view(PostModelView(Post, db.session))
admin.add_view(AuthView(User, db.session))
admin.add_view(AuthView(Role, db.session))
admin.add_view(ShortLinkModelView(ShortLink, db.session))