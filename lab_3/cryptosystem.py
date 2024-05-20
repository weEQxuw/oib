import struct
import os

from cryptography.hazmat.primitives.asymmetric import rsa
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes

from auxiliary_function import FileHelper
from symmetric import Symmetric
from assymetric import Assymetric


class CryptoSystem:
    def __init__(self) -> None:
        pass

    @staticmethod
    def encrypt(text: str, sym_key: bytes, private_key: rsa.RSAPublicKey) -> bytes:
        sym_key = Assymetric.decrypt_key()
        nonce = os.urandom(8)
        counter = 0
        full_nonce = struct.pack("<Q", counter) + nonce
        algorithm = algorithms.ChaCha20(sym_key, full_nonce)
        cipher = Cipher(algorithm, mode=None)
        encryptor = cipher.encryptor()
        cipher_text = encryptor.update(text)
        return full_nonce + cipher_text

    @staticmethod
    def decrypt(encrypt_data: bytes, sym_key: bytes) -> bytes:
        full_nonce = encrypt_data[:16]
        cipher_text = encrypt_data[16:]
        algorithm = algorithms.ChaCha20(sym_key, full_nonce)
        cipher = Cipher(algorithm, mode=None)
        decryptor = cipher.decryptor()
        return decryptor.update(cipher_text)

    @staticmethod
    def generate_key() -> tuple:
        symmetric_key = Symmetric.generate_key()
        private_key, public_key = Assymetric.generate_key()
        return symmetric_key, private_key, public_key
