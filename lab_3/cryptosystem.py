import struct
import os
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from auxiliary_function import read_file


class Cryptosystem:
    def __init__(self) -> None:
        pass

    @staticmethod
    def encrypt(path_text: str, sym_key: bytes) -> bytes:
        text = read_file(path_text)
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
