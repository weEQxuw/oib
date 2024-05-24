import argparse

from auxiliary_function import FileHelper
from cryptosystem import CryptoSystem


def main() -> None:
    """
        the main function for working with encryption and key generation
    """
    parser = argparse.ArgumentParser()
    group = parser.add_mutually_exclusive_group(required=True)
    group.add_argument('-gen', '--generation',
                       help='Запускает режим генерации ключей', action="store_true")
    group.add_argument('-enc', '--encryption',
                       help='Запускает режим шифрования', action="store_true")
    group.add_argument('-dec', '--decryption',
                       help='Запускает режим дешифрования', action="store_true")
    parser.add_argument('-p', '--paths', type=str, help="Путь до json файла")

    parser.add_argument('--sym-key-path', type=str,
                        help="Путь для симметричного ключа")
    parser.add_argument('--priv-key-path', type=str,
                        help="Путь для приватного ключа")
    parser.add_argument('--pub-key-path', type=str,
                        help="Путь для публичного ключа")
    parser.add_argument('--input-file', type=str,
                        help="Путь к исходному файлу")
    parser.add_argument('--decr-file', type=str,
                        help="Путь к дешифрованному файлу файлу")
    parser.add_argument('--encr-file', type=str,
                        help="Путь к шифрованному файлу файлу")

    args = parser.parse_args()

    if args.paths:
        paths = FileHelper.read_json_dict(args.paths)

    sym_key_path = args.sym_key_path if args.sym_key_path else paths.get(
        'symmetric_key')
    private_key_path = args.priv_key_path if args.priv_key_path else paths.get(
        'secret_key')
    public_key_path = args.pub_key_path if args.pub_key_path else paths.get(
        'public_key')
    initial_file = args.input_file if args.input_file else paths.get(
        'initial_file')
    encrypted_file = args.encr_file if args.encr_file else paths.get(
        'encrypted_file')
    decrypted_file = args.decr_file if args.encryption else paths.get(
        'decrypted_file')

    match(args.generation, args.encryption, args.decryption):
        case(True, False, False):
            sym_key, private_key, public_key = CryptoSystem.generate_key()
            FileHelper.write_bytes(sym_key_path, sym_key)
            FileHelper.write_private_key(private_key_path, private_key)
            FileHelper.write_public_key(public_key_path, public_key)
        case(False, True, False):
            text = FileHelper.read_file(initial_file)
            sym_key = FileHelper.read_bytes(sym_key_path)
            private_key = FileHelper.read_private_key(private_key_path)
            encrypted_text = CryptoSystem.encrypt(text, sym_key, private_key)
            FileHelper.write_bytes(encrypted_file, encrypted_text)
        case(False, False, True):
            encrypted_text = FileHelper.read_bytes(encrypted_file)
            sym_key = FileHelper.read_bytes(sym_key_path)
            private_key = FileHelper.read_private_key(private_key_path)
            decrypted_text = CryptoSystem.decrypt(
                encrypted_text, sym_key, private_key)
            FileHelper.write_file(decrypted_text, decrypted_file)


if __name__ == "__main__":
    main()
