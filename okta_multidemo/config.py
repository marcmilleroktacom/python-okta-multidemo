import json
import os

from pathlib import Path

from dotenv import load_dotenv
load_dotenv()


def get_theme_config(theme_mode, theme):
    path = Path(__file__).parent.absolute()
    with open(os.path.join(
            path, 'conf/{}/{}/config.json'.format(theme_mode, theme)
        )) as file_:
        data = file_.read()
    return json.loads(data)

class BaseConfig(object):
    DEBUG = False
    TESTING = False
    SITE_NAME = ''
    APP_URL=os.getenv('APP_URL')
    DB_PATH=os.getenv('DB_PATH')
    API_URL=os.getenv('API_URL')
    SECRET_KEY = os.getenv('SECRET_KEY')

    OKTA_BASE_URL=os.getenv('OKTA_BASE_URL')
    OKTA_API_KEY=os.getenv('OKTA_API_KEY')
    OKTA_CLIENT_ID=os.getenv('OKTA_CLIENT_ID')
    OKTA_CLIENT_SECRET=os.getenv('OKTA_CLIENT_SECRET')
    OKTA_ISSUER=os.getenv('OKTA_ISSUER')
    OKTA_AUDIENCE=os.getenv('OKTA_AUDIENCE')
    OKTA_GOOGLE_IDP=os.getenv('OKTA_GOOGLE_IDP')
    OKTA_FACEBOOK_IDP=os.getenv('OKTA_FACEBOOK_IDP')
    OKTA_SAML_IDP=os.getenv('OKTA_SAML_IDP')
    OKTA_SCOPES=os.getenv('OKTA_SCOPES').split(',')
    OKTA_ADMIN_SCOPES=os.getenv('OKTA_ADMIN_SCOPES').split(',')
    OKTA_ADMIN_CLIENT_ID=os.getenv('OKTA_ADMIN_CLIENT_ID')
    OKTA_IDP_REQUEST_CONTEXT=os.getenv('OKTA_IDP_REQUEST_CONTEXT')

    THEME=os.getenv('THEME', 'default')
    THEME_MODE=os.getenv('THEME_MODE', 'default')
    theme_config = get_theme_config(THEME_MODE, THEME)
    THEME_LABEL = theme_config['label']
    SITE_TITLE = theme_config['site-title']
    ITEMS_TITLE = theme_config['items-title']
    ITEMS_TITLE_LABEL = theme_config['items-title-label']
    ITEMS_PATH = '/{}'.format(theme_config['items-title-label'])
    ITEMS_ACTION_TITLE = theme_config['action-title']


class DevelopmentConfig(BaseConfig):
    SECRET_KEY = os.getenv('SECRET_KEY')
    SITE_NAME = os.getenv('SITE_NAME')
    HOME_HTML = os.getenv('HOME_HTML')
    DEBUG = True
    TESTING = True


class TestingConfig(BaseConfig):
    DEBUG = False
    TESTING = True


class ProductionConfig(BaseConfig):
    SECRET_KEY = os.getenv('SECRET_KEY')
    SITE_NAME = os.getenv('SITE_NAME')
    HOME_HTML = os.getenv('HOME_HTML')
    GROUP_ID="1"
