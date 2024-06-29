# Database configuration
DB_CONFIG = {
    'host': 'localhost',
    'user': 'root',
    'password': '',
    'database': 'mikrotikbilling'
}

# MikroTik API configuration
MIKROTIK_CONFIG = {
    'host': '192.168.56.101',
    'username': 'admin',
    'password': '1111',
    'api_port': 8728
}

# M-Pesa API configuration (if applicable)
MPESA_CONFIG = {
    'shortcode': '174379',
    'consumer_key': 'yrQq21AKgqZPZrFQmHBXB8AVHGcERaYOlSsjQdKEffzDdt20U',
    'consumer_secret': 'rrhrucAwdGXie6ZIGPOhwO1ILa5PWIsyOhofvX7RCUSA64Zsjn0i4BGJAtZbMqKI',
    'environment': 'sandbox', 
    'passkey': 'bfb279f9aa9bdbcf158e97dd71a467cd2e0c893059b10f78e6b72ada1ed2c919',
    'endpoint': 'https://sandbox.safaricom.co.ke',
    'callback': 'https://mydomain.com/pat' 
}

# JWT secret key for authentication (if needed)
JWT_SECRET = '4rever2moro'

# Flask application secret key (for session management)
SECRET_KEY = 'fgdhbfdnhrtyh435gdfg3.,/;'
