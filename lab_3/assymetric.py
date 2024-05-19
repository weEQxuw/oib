from cryptography.hazmat.primitives.asymmetric import rsa
from cryptography.hazmat.primitives.asymmetric.padding import OAEP, MGF1
from cryptography.hazmat.primitives import hashes


class Assymetric:
    def __init__(self) -> None:
        pass

    @staticmethod
    def generate_key(self) -> tuple:
        """_summary_

        Returns:
            tuple: _description_
        """
        keys = rsa.generate_private_key(public_exponent=65537, key_size=2048)
        return keys, keys.public_key()

    @staticmethod
    def encrypt_key(symmetric_key: bytes, public_key: rsa.RSAPublicKey) -> bytes:
        return public_key.encrypt(symmetric_key, OAEP(
            mgf=MGF1(algorithm=hashes.SHA256()),
            algorithm=hashes.SHA256(),
            label=None))

    @staticmethod
    def decrypt_key(symmeric_key: bytes, private_key: rsa.RSAPrivateKey) -> bytes:
        return private_key.decrypt(symmeric_key, OAEP(
            mgf=MGF1(algorithm=hashes.SHA256()),
            algorithm=hashes.SHA256(),
            label=None))
