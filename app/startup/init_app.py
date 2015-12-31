from flask_mail import Mail
from flask.ext.security import Security, SQLAlchemyUserDatastore
from flask.ext.social import Social, SQLAlchemyConnectionDatastore
from logging.handlers import SMTPHandler

import logging

def init_app(app, db, extra_config_settings={}):
    app.config.from_object('app.startup.settings')
    app.config.update(extra_config_settings)
    
    mail = Mail(app)

    init_error_logger_with_email_handler(app)

    from app.startup import assets
    
    #views
    from app.admin import views
    from app.articles import views
    from app.contact import views
    from app.pages import views

    return app


def init_error_logger_with_email_handler(app):
    """
    Initialize a logger to send emails on error-level messages.
    Unhandled exceptions will now send an email message to app.config.ADMINS.
    """
    if app.debug: return                        # Do not send error emails while developing

    # Retrieve email settings from app.config
    host      = app.config['MAIL_SERVER']
    port      = app.config['MAIL_PORT']
    from_addr = app.config['MAIL_DEFAULT_SENDER']
    username  = app.config['MAIL_USERNAME']
    password  = app.config['MAIL_PASSWORD']
    secure = () if app.config.get('MAIL_USE_TLS') else None

    # Retrieve app settings from app.config
    to_addr_list = app.config['ADMINS']
    subject = app.config.get('APP_SYSTEM_ERROR_SUBJECT_LINE', 'System Error')

    # Setup an SMTP mail handler for error-level messages
    mail_handler = SMTPHandler(
        mailhost=(host, port),                  # Mail host and port
        fromaddr=from_addr,                     # From address
        toaddrs=to_addr_list,                   # To address
        subject=subject,                        # Subject line
        credentials=(username, password),       # Credentials
        secure=secure,
    )
    mail_handler.setLevel(logging.ERROR)
    app.logger.addHandler(mail_handler)

    # Log errors using: app.logger.error('Some error message')