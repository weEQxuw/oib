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
        """
            method for text encryption

        Args:
            text (str): the text to encrypt
            sym_key (bytes): symmetric key
            private_key (rsa.RSAPublicKey): RSA private key

        Returns:
            bytes: encrypted text
        """
        sym_key = Assymetric.decrypt_key(sym_key, private_key)
        nonce = os.urandom(8)
        counter = 0
        b_text = bytes(text, 'UTF-8')
        full_nonce = struct.pack("<Q", counter) + nonce
        algorithm = algorithms.ChaCha20(sym_key, full_nonce)
        cipher = Cipher(algorithm, mode=None)
        encryptor = cipher.encryptor()
        cipher_text = encryptor.update(b_text)
        return full_nonce + cipher_text

    @staticmethod
    def decrypt(encrypt_data: bytes, sym_key: bytes, private_key: rsa.RSAPublicKey) -> str:
        """
            method for text decrypt

        Args:
            encrypt_data (bytes): encrypted text
            sym_key (bytes): symmetric key
            private_key (rsa.RSAPublicKey): RSA private key

        Returns:
            str: the text
        """
        sym_key = Assymetric.decrypt_key(sym_key, private_key)
        full_nonce = encrypt_data[:16]
        cipher_text = encrypt_data[16:]
        algorithm = algorithms.ChaCha20(sym_key, full_nonce)
        cipher = Cipher(algorithm, mode=None)
        decryptor = cipher.decryptor()
        text = decryptor.update(cipher_text)
        text = text.decode('UTF-8')
        return text

    @staticmethod
    def generate_key() -> tuple:
        """
            generates both a symmetric key and an asymmetric one

        Returns:
            tuple: symmetric_key, private_key, public_key
        """
        symmetric_key = Symmetric.generate_key()
        private_key, public_key = Assymetric.generate_keys()
        symmetric_key = Assymetric.encrypt_key(symmetric_key, public_key)
        return symmetric_key, private_key, public_key
