from flask_admin.contrib.sqla import ModelView
from flask_security import current_user

class AuthView(ModelView):
  def is_accessible(self):
    if not current_user.is_active or not current_user.is_authenticated:
      return False
    if current_user.has_role('Admin'):
      return True
    return False