import os

BASEDIR = os.path.abspath(os.path.dirname(__file__))


class Config:

    SECRET_KEY = os.environ.get("SECRET_KEY")
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or 'sqlite:///' + os.path.join(BASEDIR, 'sqlite.db')
    # SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://{}:{}@{}:{}/{}'.format(
    #     os.environ.get('DB_USER'),
    #     os.environ.get('DB_PASSWORD'),
    #     os.environ.get('DB_HOSTNAME'),
    #     os.environ.get('DB_PORT'),
    #     os.environ.get('DB_NAME'),
    # )
    SQLALCHEMY_TRACK_MODIFICATIONS = True
    MAIL_SERVER = "smtp.googlemail.com"
    MAIL_PORT = 587
    MAIL_USE_TLS = True
    MAIL_USERNAME = os.environ.get("EMAIL_USER")
    MAIL_PASSWORD = os.environ.get("EMAIL_PASS")

    # EXPLAIN_TEMPLATE_LOADING = True
    # print('SC', SECRET_KEY)
    # print('MU', MAIL_USERNAME)
    # print('MP', MAIL_PASSWORD)
    # print('dbu', SQLALCHEMY_DATABASE_URI)

    print('db_uri')
    print(SQLALCHEMY_DATABASE_URI)
    print('SECRET_KEY', os.environ.get('SECRET_KEY'))
