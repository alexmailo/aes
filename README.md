# Aes 256 file encryptor
It uses AES CBC 256 bit mode to encrypt the data and output it to lzmat the compression'
algorithm to make it as small as possible.


## To encrypt
```bash
python aes.py --input "input_file" --output "output_file" --key "32 byte key"
```


## To decrypt


```bash
python aes.py --input "prev encrypted file" --output "original file" --key "32 byte key"
```
