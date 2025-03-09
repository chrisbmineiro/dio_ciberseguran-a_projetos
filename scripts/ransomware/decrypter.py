import os
import pyaes

# abrir arquivo criptografado
file_name = 'Caminho/para/o/arquivo/a/ser/descriptografado'

if not os.path.exists(file_name):
    print(f"Arquivo {file_name} não encontrado!")
    exit(1)
    
file = open(file_name, 'rb')
file_data = file.read()
file.close()

# chave de descriptografia
key = b'testeransomwares'
aes = pyaes.AESModeOfOperationCTR(key)
decrypt_data = aes.decrypt(file_data)

# remover o arquivo criptografado
os.remove(file_name)

# criar arquivo descriptografado
new_file = 'teste.txt'
new_file = open(new_file, 'wb')
new_file.write(decrypt_data)
new_file.close()