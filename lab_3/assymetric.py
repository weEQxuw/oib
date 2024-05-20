from cryptography.hazmat.primitives.asymmetric import rsa
from cryptography.hazmat.primitives.asymmetric.padding import OAEP, MGF1
from cryptography.hazmat.primitives import hashes


class Assymetric:
    def __init__(self) -> None:
        """_summary_
        """
        pass

    @staticmethod
    def generate_keys() -> tuple:
        """_summary_

        Returns:
            tuple: _description_
        """
        keys = rsa.generate_private_key(public_exponent=65537, key_size=2048)
        return keys, keys.public_key()

    @staticmethod
    def encrypt_key(symmetric_key: bytes, public_key: rsa.RSAPublicKey) -> bytes:
        """_summary_

        Args:
            symmetric_key (bytes): _description_
            public_key (rsa.RSAPublicKey): _description_

        Returns:
            bytes: _description_
        """
        return public_key.encrypt(symmetric_key, OAEP(
            mgf=MGF1(algorithm=hashes.SHA256()),
            algorithm=hashes.SHA256(),
            label=None))

    @staticmethod
    def decrypt_key(symmeric_key: bytes, private_key: rsa.RSAPrivateKey) -> bytes:
        """_summary_

        Args:
            symmeric_key (bytes): _description_
            private_key (rsa.RSAPrivateKey): _description_

        Returns:
            bytes: _description_
        """
        return private_key.decrypt(symmeric_key, OAEP(
            mgf=MGF1(algorithm=hashes.SHA256()),
            algorithm=hashes.SHA256(),
            label=None))
