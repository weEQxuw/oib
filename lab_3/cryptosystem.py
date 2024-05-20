import struct
import os
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from auxiliary_function import read_file


class Cryptosystem:
    def __init__(self) -> None:
        pass

    def encrypt(path_text, sym_key) -> bytes:
        text = read_file(path_text)
        nonce = os.urandom(8)
        counter = 0
        full_nonce = struct.pack("<Q", counter) + nonce
        algorithm = algorithms.ChaCha20(sym_key, full_nonce)
        cipher = Cipher(algorithm, mode=None)
        encryptor = cipher.encryptor()
        return encryptor.update()

    def decrypt():
        pass
