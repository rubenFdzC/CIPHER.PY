text = 'mensaje encryptado'
custom_key = 'happycoding'

def vigenere(message, key, direction=1):
    key_index = 0
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    final_message = ''

    for char in message.lower():

        # Append any non-letter character to the message
        if not char.isalpha():
            final_message += char
        else:        
            # Find the right key character to encode/decode
            key_char = key[key_index % len(key)]
            key_index += 1

            # Define the offset and the encrypted/decrypted letter
            offset = alphabet.index(key_char)
            index = alphabet.find(char)
            new_index = (index + offset*direction) % len(alphabet)
            final_message += alphabet[new_index]
    
    return final_message

def encrypt(message, key):
    return vigenere(message, key)
    
def decrypt(message, key):
    return vigenere(message, key, -1)

# print(f'\nEncrypted text: {text}')
# print(f'Key: {custom_key}')
# decryption = decrypt(text, custom_key)
# print(f'\nDecrypted text: {decryption}\n')

# Definir tu mensaje y clave
mensaje_original = 'Hola, este es mi mensaje secreto'
custom_key = 'happycoding'

# Cifrar el mensaje
mensaje_cifrado = encrypt(mensaje_original, custom_key)
print(f'Mensaje cifrado: {mensaje_cifrado}')

# Descifrar el mensaje
mensaje_descifrado = decrypt(mensaje_cifrado, custom_key)
print(f'Mensaje descifrado: {mensaje_descifrado}')