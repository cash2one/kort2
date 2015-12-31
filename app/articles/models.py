from app.app_and_db import db
from sqlalchemy.dialects import mysql
from sqlalchemy.sql import func
from sqlalchemy.types import Enum

class Post(db.Model):
  __tablename__ = "posts"
  
  slug = db.Column(db.String(255), nullable=False, primary_key=True)
  
  # author = db.relationship("User")
  title = db.Column(db.String(255), nullable=False)
  subtitle =db.Column(db.String(255))

  published_date = db.Column(db.TIMESTAMP(), nullable=False)

  content = db.Column(mysql.MEDIUMTEXT())
  statuses = Enum('Hidden', 'Visible', 'Published', 'Requires Authentication')
  visibility = db.Column(statuses)

  should_break = db.Column(db.Boolean(), nullable=False, default=True)
  
  def __unicode__(self):
    return self.title

  def before_the_break(self):
    partition = self.content.partition('</p>')
    return partition[0] + partition[1]

  def is_visible(self):
    return self.visibility == 'Visible' or self.visibility == 'Published'