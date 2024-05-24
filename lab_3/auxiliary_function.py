import json

from typing import Dict

from cryptography.hazmat.primitives.asymmetric import rsa
from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.primitives.serialization import load_pem_public_key, load_pem_private_key


class FileHelper:
    """
         An auxiliary class that contains static methods for working with reading from files
    """
    @staticmethod
    def read_file(name: str) -> str:
        """
            This function reads text from the file for further processing

        Args:
            name (str): the path and name of the file to be read

        Returns:
            str: the read document
        """
        try:
            with open(name, 'r', encoding='utf-8') as f:
                data = f.read()
                return data
        except FileNotFoundError:
            print("Невозможно открыть файл")

    @staticmethod
    def write_file(document: str, name_file: str) -> None:
        """
            Writes encrypted text to a document
        Args:
            document (str): the actual processed text
            name_file (_type_): the path of the file where it will be written
        """
        try:
            with open(name_file, "w", encoding='utf-8') as f:
                f.write(document)
                return
        except IOError:
            print("Что-то пошло не так")

    @staticmethod
    def read_json_dict(path: str) -> Dict:
        """
            read json file
        Args:
            path (str): the path for the json file

        Returns:
            Dict: keys
        """
        try:
            with open(path, 'r', encoding='utf-8') as f:
                return json.load(f)
        except FileNotFoundError:
            print("Невозможно открыть файл.")

    @staticmethod
    def write_json_dict(path: str, result: dict) -> None:
        """
            write json file
        Args:
            path (str): the path for the json file

        Returns:
            Dict: keys
        """
        try:
            with open(path, 'w', encoding='utf-8') as f:
                json.dump(result, f)
        except FileNotFoundError:
            print("Невозможно открыть файл.")

    @staticmethod
    def read_bytes(path: str) -> bytes:
        """
            reads bytes from a file
        Args:
            path (str): the path of the lo file

        Returns:
            bytes: returns the contents of the file
        """
        try:
            with open(path, 'rb') as f:
                return f.read()
        except FileNotFoundError:
            print("Невозможно открыть файл.")

    @staticmethod
    def write_bytes(path: str, data: bytes) -> None:
        """
            saves information as bytes to a file

        Args:
            path (str): the path of the lo file
            data (bytes): inforamtion
        """
        try:
            with open(path, "wb") as f:
                f.write(data)
        except FileNotFoundError:
            print("Произошла какая-то ошибка")

    @staticmethod
    def write_public_key(path: str, public_key: rsa.RSAPublicKey) -> None:
        """
            saves the RSA public key
        Args:
            path (str): the path of the lo file
            public_key (rsa.RSAPublicKey): RSA public key
        """
        try:
            with open(path, 'wb') as public_out:
                public_out.write(public_key.public_bytes(encoding=serialization.Encoding.PEM,
                                                         format=serialization.PublicFormat.SubjectPublicKeyInfo))
        except FileNotFoundError:
            print("Произошла какая-то ошибка")

    @staticmethod
    def write_private_key(path: str, private_key: rsa.RSAPrivateKey) -> None:
        """
            saves the RSA private key

        Args:
            path (str): the path of the lo file
            private_key (rsa.RSAPrivateKey): RSA private key
        """
        try:
            with open(path, 'wb') as private_out:
                private_out.write(private_key.private_bytes(encoding=serialization.Encoding.PEM,
                                                            format=serialization.PrivateFormat.TraditionalOpenSSL,
                                                            encryption_algorithm=serialization.NoEncryption()))
        except FileNotFoundError:
            print("Произошла какая-то ошибка")

    @staticmethod
    def read_public_key(path: str) -> rsa.RSAPublicKey:
        """
            reading the public key from the file

        Args:
            path (str): the path of the lo file

        Returns:
            rsa.RSAPublicKey: RSA public key
        """
        try:
            with open(path, 'rb') as pem_in:
                public_bytes = pem_in.read()
                return load_pem_public_key(public_bytes)
        except FileNotFoundError:
            print("Произошла какая-то ошибка")

    @staticmethod
    def read_private_key(path: str) -> rsa.RSAPrivateKey:
        """ 
            reading the private key from the file

        Args:
            path (str): the path of the lo file

        Returns:
            rsa.RSAPrivateKey: RSA private key
        """
        try:
            with open(path, 'rb') as pem_in:
                private_bytes = pem_in.read()
                return load_pem_private_key(
                    private_bytes, password=None,)
        except FileNotFoundError:
            print("Произошла какая-то ошибка")
