# Aes 256 file encryptor
It uses AES CBC 256 bit mode to encrypt the data and output it  lzmat, a compression
algorithm,  to make it as small as possible for transfers.


## To encrypt
```bash
python aes.py --input "input_file" --output "output_file" --key "32 byte key"
```


## To decrypt


```bash
python aes.py --input "prev encrypted file" --output "original file" --key "32 byte key"
```
## Warning
As long as you keep the key safe so that nobody can see it in your shell history,
it should be very secure as AES 256-bit is a very strong algorithm 
according to [kiteworks](https://www.kiteworks.com/risk-compliance-glossary/aes-256-encryption/#:~:text=AES%2D256%20encryption%20is%20extremely,operating%20in%20highly%20regulated%20industries.)
