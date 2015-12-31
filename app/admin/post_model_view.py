from app.admin.ck_text_area_field import CKTextAreaField
from app.articles.models import Post
from flask_admin.contrib.sqla import ModelView
from flask_admin.model.template import macro
from wtforms import validators
# from flask_admin.form import SecureForm

def no_white_space(form, field):
  field.data = field.data.replace(' ', '-')

class PostModelView(ModelView):
  form_overrides = {
    'content': CKTextAreaField
  }
  
  form_args = {
    'title' : {
      'validators' : [validators.Length(max=100)]
    },
    'subtitle' : {
      'validators' : [validators.Length(max=100)]
    },
    'published_date' : {
      'description' : 'This date must be set in the past for the post to be displayed'
    },
    'content': {
      'label': 'Post Contents',
      'validators': [validators.required()]
    },
    'slug': {
      'label': 'URL Slug (Label)',
      'validators' : [no_white_space]
    },
    'visibility': {
      'default' : 'Published'
    },
    'should_break': {
      'label' : 'Should Break After First Paragraph'
    }
  }
  column_exclude_list = ['content', 'should_break']
  column_searchable_list = ['title', 'slug', 'visibility']
  column_formatters = dict(slug=macro('render_slug'), visibility=macro('render_visibility'))
  column_default_sort = ('published_date', True)
  column_display_pk = True
  form_columns = Post.__table__.columns._data.keys()
  # form_base_class = SecureForm
