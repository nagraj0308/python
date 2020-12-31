
import hashlib
import hmac



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
encoded_key = str(key).encode()
encoded_msg = str(msg).encode()
msg_key = (key + msg).encode()
mac1 = hashlib.sha512(msg_key)


digest2 = hmac.new(key, b'hi', hashlib.sha3_256)
print("Nested MAC Digest : ", digest2.hexdigest())"""

