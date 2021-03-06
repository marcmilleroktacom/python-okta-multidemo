from flask import url_for

def get_widget_config(app_conf, type_=None):
    widget_conf = {
        'baseUrl': app_conf['OKTA_BASE_URL'],
        'clientId': app_conf['OKTA_CLIENT_ID'],
        'logo': '{}/icon.png'.format(app_conf['THEME_URI']),
        'language': 'en',
        'i18n': {
            'en': {
                'primaryauth.title': 'Sign in to {}'.format(app_conf['SITE_TITLE'])
            }
        },
        'authParams': {
            'issuer': app_conf['OKTA_ISSUER'],
            'scopes': app_conf['OKTA_SCOPES'],
        }
    }
    if type_ in ['implicit', 'social']:
        # TODO: is is necessary to use implicit for social? probably not
        widget_conf['redirectUri'] = '{}/implicit/callback'.format(
            app_conf['APP_URL'])
        widget_conf['authParams']['responseType'] = ['token', 'id_token']
        if type_ == 'social':
            widget_conf['idps'] = [
                {'type': 'GOOGLE', 'id': app_conf['OKTA_GOOGLE_IDP']},
                {'type': 'FACEBOOK', 'id': app_conf['OKTA_FACEBOOK_IDP']},
                {'id': app_conf['OKTA_SAML_IDP'], 'text': 'Login with SAML IdP', 'className': '' }
            ]
            widget_conf['authParams']['display'] = 'popup'
    elif type_ == 'idp-disco':
        widget_conf['authParams']['display'] = 'page'
        widget_conf.update({'features': {'idpDiscovery': True}})
        widget_conf.update({'idpDiscovery': {'requestContext': app_conf['OKTA_IDP_REQUEST_CONTEXT']}})
        widget_conf['redirectUri'] = '{}{}/authorized'.format(
            app_conf['APP_URL'], url_for('okta.login')
        )
    else:
        widget_conf['redirectUri'] = '{}{}/authorized'.format(
            app_conf['APP_URL'], url_for('okta.login')
        )
        widget_conf['authParams']['responseType'] = ['code']
    return widget_conf
