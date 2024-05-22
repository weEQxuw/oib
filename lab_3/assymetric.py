from cryptography.hazmat.primitives.asymmetric import rsa
from cryptography.hazmat.primitives.asymmetric.padding import OAEP, MGF1
from cryptography.hazmat.primitives import hashes


class Assymetric:
    """
        The RSA encryption algorithm uses two different keys: 
        one for encrypting the message, and the second — different from the first, 
        but related to it — for decryption. The encryption key (public, unclassified key) 
        is based on the product of two huge primes, 
        and the decryption key (private, secret key) is based on the primes themselves.
    """

    def __init__(self) -> None:
        """
            the designer, but for the sake of security, it was decided not to store the keys
        """
        pass

    @staticmethod
    def generate_keys() -> tuple:
        """ 
            generating a key pair for an asymmetric encryption algorithm
        Returns:
            tuple: returns A public and private key
        """
        keys = rsa.generate_private_key(public_exponent=65537, key_size=2048)
        return keys, keys.public_key()

    @staticmethod
    def encrypt_key(symmetric_key: bytes, public_key: rsa.RSAPublicKey) -> bytes:
        """
            key encryption using RSA-OAEP
        Args:
            symmetric_key (bytes): generated symmetric key
            public_key (rsa.RSAPublicKey): assymetric public key generated

        Returns:
            bytes: encrypt symmetric key
        """
        return public_key.encrypt(symmetric_key, OAEP(
            mgf=MGF1(algorithm=hashes.SHA256()),
            algorithm=hashes.SHA256(),
            label=None))

    @staticmethod
    def decrypt_key(symmeric_key: bytes, private_key: rsa.RSAPrivateKey) -> bytes:
        """
            decryption of text by an asymmetric algorithm
        Args:
            symmeric_key (bytes): encrypt symmetric key
            private_key (rsa.RSAPrivateKey): assymetric private key generated

        Returns:
            bytes:  decrypt symmetric key
        """
        return private_key.decrypt(symmeric_key, OAEP(
            mgf=MGF1(algorithm=hashes.SHA256()),
            algorithm=hashes.SHA256(),
            label=None))
