DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql', # Add 'postgresql_psycopg2', 'postgresql', 'mysql', 'sqlite3' or 'oracle'.
        'NAME': '{{ freeradius_admin.db_name }}',                      # Or path to database file if using sqlite3.
        'USER': '{{ freeradius_admin.db_user }}',                      # Not used with sqlite3.
        'PASSWORD': '{{ freeradius_admin.db_password }}',                  # Not used with sqlite3.
        'HOST': '127.0.0.1',                      # Set to empty string for localhost. Not used with sqlite3.
        'PORT': '',                      # Set to empty string for default. Not used with sqlite3.
    },
    'radius': {
        'ENGINE': 'django.db.backends.mysql', # Add 'postgresql_psycopg2', 'postgresql', 'mysql', 'sqlite3' or 'oracle'.
        'NAME': '{{ freeradius.db_name }}',                      # Or path to database file if using sqlite3.
        'USER': '{{ freeradius.db_user }}',                      # Not used with sqlite3.
        'PASSWORD': '{{ freeradius.db_password }}',                  # Not used with sqlite3.
        'HOST': '127.0.0.1',                      # Set to empty string for localhost. Not used with sqlite3.
        'PORT': '',                      # Set to empty string for default. Not used with sqlite3.
    }
}


STATIC_ROOT = '/opt/djra/data/static'
