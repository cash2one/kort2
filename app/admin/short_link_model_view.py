from app.pages.models import ShortLink
from flask_admin.contrib.sqla import ModelView

class ShortLinkModelView(ModelView):
  column_display_pk = True
  form_columns = ShortLink.__table__.columns._data.keys()