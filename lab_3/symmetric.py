import os


class Symmetric:
    """
        Symmetric ChaCha20 encryption algorithm. the key length is 256 bits
    """

    def __init__(self) -> None:
        """ 
             for the sake of security, it was decided not to store the keys
        """
        pass

    def generate_key() -> bytes:
        """
            symmetric key generation key length 256 bit

        Returns:
            bytes: symmetric key
        """
        return os.urandom(32)
