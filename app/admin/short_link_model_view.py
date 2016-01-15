from app.admin.auth_view import AuthView
from app.pages.models import ShortLink

class ShortLinkModelView(AuthView):
  column_display_pk = True
  form_columns = ShortLink.__table__.columns._data.keys()