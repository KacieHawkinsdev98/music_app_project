SECRET_KEY = 'django-insecure-qvk_f)t#s(6-aeij9s7$xk@its7@epq8=nwkak_w916y#rk&rm'

DATABASES = {
    'default': {
        'ENGINE': 'mysql.connector.django',
        'NAME': 'music_library_database',
        'USER': 'root', 
        'PASSWORD': 'rabbit',
        'HOST': '127.0.0.1',
        'PORT': 3306, 
        'OPTIONS': {
            'autocommit': True
        }
    }
}
