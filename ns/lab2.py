"""Implement the following assignment using Python only
   import hashlib in python which includes all hash algorithms 
   and implement MAC, Nested MAC, HMAC."""
import hashlib
import hmac

""" MAC """
msg = 'Nagendra Chaudhary'
key = 'NagRaj'
msg_key = (key + msg).encode()
mac = hashlib.sha512(msg_key).hexdigest()
print("MAC : ", mac)

""" Nested MAC """
msg = 'Nagendra Chaudhary'
key = 'NagRaj'
msg = str(key + msg).encode('utf-8')
m = hashlib.sha256()
m.update(msg)
unicode_mac = m.digest()
encoded_key = str(key).encode('utf-8')
nm = hash.sha256()
nm.update(unicode_mac + encoded_key)
nested_mac = nm.hexdigest()
print("Nested MAC : ", nested_mac)

""" Nested MAC """
msg = 'Nagendra Chaudhary'
key = 'NagRaj'
msg_key = (key + msg).encode()
mac = hashlib.sha512(msg_key).hexdigest()
print("MAC Digest : ", mac)
"""digest1 = hmac.new(key, msg, hashlib.sha3_256)
print(type(digest1))
digest2 = hmac.new(key, b'hi', hashlib.sha3_256)
print("Nested MAC Digest : ", digest2.hexdigest())"""

""" HMAC """
msg = b'Nagendra Chaudhary'
key = b'NagRaj'
digest = hmac.new(key, msg, hashlib.sha3_256).hexdigest()
print("HMAC Digest : ", digest)
