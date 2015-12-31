from flask.ext.assets import Bundle, Environment

from app.app_and_db import app, webassets

js_libs = Bundle("js/jquery.min.js",
                "js/bootstrap.min.js",
                "js/moment.js",
                "js/select2.min.js",
                "js/daterangepicker.js",
                 filters="jsmin",
                 output="js/libs.js")

js_main = Bundle("js/main.js",
                 filters="jsmin",
                 output="js/main.js")

js_admin = Bundle("js/admin.js",
                  "js/ckeditor/ckeditor.js",
                 filters="jsmin",
                 output="js/admin.js")

css_libs = Bundle("css/bootstrap.css",
                  "css/font-awesome.css",
                  "css/select2.css",
                  "css/daterangepicker.css",
                  filters="less",
                  output="css/libs.css")

css_main = Bundle("css/main.less",
                  "css/index.less",
                  filters="less",
                  output="css/styles.css"
                  )

css_admin = Bundle("css/main.less",
                  "css/admin.less",
                  filters="less",
                  output="css/admin.css"
                  )

webassets.manifest = 'cache' if not app.config['DEBUG'] else False
webassets.cache = not app.config['DEBUG']
webassets.debug = "merge" if app.config['DEBUG'] == True else False

webassets.register('js_libs', js_libs)
webassets.register('css_libs', css_libs)

webassets.register('js_main', js_main)
webassets.register('css_main', css_main)

webassets.register('js_admin', js_admin)
webassets.register('css_admin', css_admin)
