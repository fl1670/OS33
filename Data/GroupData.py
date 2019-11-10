class group_data(object):
    branch = 'way2automation.com'

    GLOBAL = {
        'time_element_Wait': 30,

        'Browser': {
            # 'Name': 'firefox',
            # 'Name': 'MicrosoftEdge',
            # 'Name': 'internet explorer',
            'Name': 'chrome'
        },
        'way2automation.com': {
            'Name': 'kickico.com',
            'main_page': 'http://www.way2automation.com/angularjs-protractor/registeration/#/login',
            'Internal_Link': '',
            'External_Link': 'http://www.way2automation.com/angularjs-protractor/registeration/#/login',
            'API_Internal_Link': '',
            'API_External_Link': '',
            'USERS': {
                'SystemOperator': {
                    'Name': "",
                    'Login': "",
                    'password': "",
                },
            },
            'SQL_SERVER': {
                'SERVER': '',
                'DATABASE': '',
                'user': '',
                'password': '',
                'DRIVER': '',
            }

        },
    }

    Users = {
        'User1': {
            'Login': "angular",
            'password': "password",
            'Name': "test",
        }
    }

    access_token = "",
    token_type = "",
    expires_in = ""
