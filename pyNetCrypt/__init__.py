__doc__ = '''Networking Tool set
Password Encryption / Decryption
'''

__all__ = [
	# cpw_cracker
	'encrypt_type7', 'decrypt_type7', 'decrypt_file_passwords', 'mask_file_passwords',
	# jpw_cracker
	'juniper_decrypt', 'juniper_encrypt', 'decrypt_doller9_file_passwords', 'mask_doller9_file_passwords',
]

__version__ = "0.0.1"

from .cpw_cracker import decrypt_type7, encrypt_type7, decrypt_file_passwords, mask_file_passwords
from .jpw_cracker import juniper_decrypt, juniper_encrypt, decrypt_doller9_file_passwords, mask_doller9_file_passwords


def version():
	return __version__