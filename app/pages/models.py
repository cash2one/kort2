from app.app_and_db import db
from sqlalchemy.dialects import mysql

class ShortLink(db.Model):
  __tablename__ = "short_links"
  
  slug = db.Column(db.String(255), nullable=False, primary_key=True)
  redirect = db.Column(mysql.TEXT(), nullable=False)