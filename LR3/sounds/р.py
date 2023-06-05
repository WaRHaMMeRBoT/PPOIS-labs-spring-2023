if __name__ == "__main__":

    encrypted_text = "абвгдеёжзийклмнопрстуфхцчшщъыьэюя"
    # encrypted_text = "эанлы"

    alphabet = "абвгдеёжзийклмнопрстуфхцчшщъыьэюя"

    for key in alphabet:
        decrypted_text = ""
        for char in encrypted_text:
            if char.lower() in alphabet:
                char_index = alphabet.index(char.lower())
                key_index = alphabet.index(key.lower())
                decrypted_index = (char_index - key_index) % len(alphabet)
                decrypted_char = alphabet[decrypted_index]
                decrypted_text += decrypted_char.upper() if char.isupper() else decrypted_char
            else:
                decrypted_text += char
        print(f"Key: {key}, Decrypted Text: {decrypted_text}")