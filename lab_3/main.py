import argparse
from auxiliary_function import FileHelper
from cryptosystem import CryptoSystem


def main():
    parser = argparse.ArgumentParser()
    group = parser.add_mutually_exclusive_group(required=True)
    group.add_argument('-gen', '--generation',
                       help='Запускает режим генерации ключей', action="store_true")
    group.add_argument('-enc', '--encryption',
                       help='Запускает режим шифрования', action="store_true")
    group.add_argument('-dec', '--decryption',
                       help='Запускает режим дешифрования', action="store_true")
    parser.add_argument('-p', '--paths', type=str, help="Путь до json файла")

    args = parser.parse_args()

    paths = FileHelper.read_json_dict(args.paths)

    match(args.generation, args.encryption, args.decryption):
        case(True, False, False):
            sym_key, private_key, public_key = CryptoSystem.generate_key()
            FileHelper.write_bytes(paths["symmetric_key"], sym_key)
            FileHelper.write_private_key(paths["secret_key"], private_key)
            FileHelper.write_public_key(paths["public_key"], public_key)
        case(False, True, False):
            text = FileHelper.read_file(paths["initial_file"])
            sym_key = FileHelper.read_bytes(paths['symmetric_key'])
            private_key = FileHelper.read_private_key(paths['secret_key'])
            encrypted_text = CryptoSystem.encrypt(text, sym_key, private_key)
            FileHelper.write_bytes(paths["encrypted_file"], encrypted_text)
        case(False, False, True):


if __name__ == "__main__":
    main()
