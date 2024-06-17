import jwt

# Detected use of 'none' algorithm in JWT token
token = jwt.encode({'some': 'payload'}, algorithm='none')

