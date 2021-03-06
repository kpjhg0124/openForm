##############################  LocalSettings.py  ##############################
####################### ENTREE Flask Web App Config File #######################

# SQLITE3_FILENAME must be in string format.
sqlite3_filename = 'data/' + 'db.db'
# flask_host must be in string format.
flask_host = '0.0.0.0'
# flask_host must be in integer format.
flask_host_port = 2500
# CRYPT_SECRET_KEY must be in string format.
crypt_secret_key = 'SECRET_KEY'
# ENTREE_APPNAME must be in string format.
entree_appname = 'Fe-tea'

# must be included protocol
publish_host_name = 'http://localhost:2500'

# If you publish application, You must turn off the debug mode.
flask_debug_mode = True

flask_ssl_key = 'data/ssl/' + '' # flask_ssl_key + '.key' / flask_ssl_key + '.crt'