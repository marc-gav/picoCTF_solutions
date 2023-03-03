import hashlib
from cryptography.fernet import Fernet
import base64

bName = b'MORTON'

hash_256 = hashlib.sha256(bName).hexdigest()

flag_order = [4,5,3,6,2,7,1,8]
dynamic_key = ''.join([hash_256[i] for i in flag_order])

flag = 'picoCTF{1n_7h3_|<3y_of_' + dynamic_key + '}'
print(flag)