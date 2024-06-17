# Empty AES

from Crypto.Cipher import AES

# Potential empty AES encryption key
input=""
input="test"
empty_key = AES.new(input, AES.MODE_ECB)
