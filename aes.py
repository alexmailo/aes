import json
from base64 import b64encode, b64decode
import argparse
from Crypto.Util.Padding import pad , unpad
from Crypto.Cipher import AES

KEY_LENGTH = 32
BLOCK_SIZE = KEY_LENGTH


def handle_encrypt(args):
    with open(args.input, "rb") as f:
        data = f.read()
    key = args.key
    cipher = AES.new(bytes(key, 'utf8'), AES.MODE_CBC)
    ciphertext = cipher.encrypt( pad( data, BLOCK_SIZE))

    iv = b64encode(cipher.iv).decode('utf-8')
    ct = b64encode(ciphertext).decode('utf-8')
    with open( args.output, "wb") as fw:
        result = json.dumps({'iv':iv, 'ciphertext':ct})
        fw.write(b64encode( result.encode()))

def handle_decrypt(args):
    key = args.key

    with open(args.input, "rb") as f:
        blob = f.read()

    json_data = b64decode( blob)
    json_data = json.loads(json_data)
    iv  = json_data["iv"]
    iv = b64decode(iv)
    ct = json_data["ciphertext"]
    ct = b64decode(ct)


    cipher = AES.new(bytes(key, 'utf8'), AES.MODE_CBC, iv)
    file_data = unpad(cipher.decrypt( ct ), BLOCK_SIZE)

    
    with open( args.output, "wb") as fw:
        fw.write(file_data)


if __name__ == "__main__": 
    

    parser = argparse.ArgumentParser(
                        prog="aes.py",
                        description='Encrypts with aes 256-bit CBC encryption',
                        epilog='Encrypts files with aes 256-bit CBC encryption'
     )

    parser.add_argument("--decrypt", "-d", action="store_true",help="Whether is it decrypting or not")
    parser.add_argument("--input", "-i",type=str, required=True, help="The input file ( can be the ciphertext or the file)")
    parser.add_argument("--output", "-o",default="aes256.out", help="output file ( can be the ciphertext or the file)")
    parser.add_argument("--key", "-k", type=str, required=True, help="the key used to encrypt")

    args = parser.parse_args()


    if len(args.key) != 32:
        print("key is not 32 bytes long")
        exit(1)


    if args.decrypt:
        handle_decrypt(args)
    else:
        handle_encrypt(args)
