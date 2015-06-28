DATABASES = {
    'default': {
{% if djra_db_engine  == 'mysql' %}
        'ENGINE': 'django.db.backends.mysql', # Add 'postgresql_psycopg2', 'postgresql', 'mysql', 'sqlite3' or 'oracle'.
        'NAME': '{{ djra_db_name }}',                      # Or path to database file if using sqlite3.
        'USER': '{{ djra_db_user }}',                      # Not used with sqlite3.
        'PASSWORD': '{{ djra_db_password }}',                  # Not used with sqlite3.
        'HOST': '127.0.0.1',                      # Set to empty string for localhost. Not used with sqlite3.
        'PORT': '',                      # Set to empty string for default. Not used with sqlite3.
{% else %}
        'ENGINE': 'django.db.backends.sqlite3', # Add 'postgresql_psycopg2', 'postgresql', 'mysql', 'sqlite3' or 'oracle'.
        'NAME': '/opt/djra/data/db/djra.db',                      # Or path to database file if using sqlite3.
{% endif %}
    },
    'radius': {
        'ENGINE': 'django.db.backends.mysql', # Add 'postgresql_psycopg2', 'postgresql', 'mysql', 'sqlite3' or 'oracle'.
        'NAME': '{{ freeradius_db_name }}',                      # Or path to database file if using sqlite3.
        'USER': '{{ freeradius_db_user }}',                      # Not used with sqlite3.
        'PASSWORD': '{{ freeradius_db_password }}',                  # Not used with sqlite3.
        'HOST': '127.0.0.1',                      # Set to empty string for localhost. Not used with sqlite3.
        'PORT': '',                      # Set to empty string for default. Not used with sqlite3.
    }
}


STATIC_ROOT = '/opt/djra/data/static'

{% if djra_ip_db_file %}
IP_DB_FILE = "/opt/djra/data/ipdb.dat"
{% endif %}
