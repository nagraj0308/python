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

"""Nested MAC """
msg = 'Nagendra Chaudhary'
key = 'NagRaj'
encoded_key = str(key).encode()
encoded_msg = str(msg).encode()
mac1 = hashlib.sha512(encoded_key + encoded_msg)
mac2 = hashlib.sha512(encoded_key + mac1.digest())
print("Nested MAC : ", mac2.hexdigest())

""" HMAC """
msg = b'Nagendra Chaudhary'
key = b'NagRaj'
digest = hmac.new(key, msg, hashlib.sha3_256)
print("HMAC : ", digest.hexdigest())
