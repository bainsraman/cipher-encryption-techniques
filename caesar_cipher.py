# LIBRARIES
from streamlit import selectbox,text_area

# LOGIC
def caesar_encrypt(text,place):
    cipher_text = ""
    for i in text:
            cipher_text += encrypt_char(i,place=place)
    return cipher_text

def caesar_decrypt(text,place):
    cipher_text = ""
    for i in text:
            cipher_text += decrypt_char(i,place=place)
    return cipher_text

def encrypt_char(char,place):
    char_upper = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    char_lower = char_upper.lower()

    if char in char_upper:
        place = place%26
        index = char_upper.index(char) + place
        index = index%26
        result = char_upper[index]
        return result
    elif char in char_lower:
        place = place%26
        index = char_lower.index(char) + place
        index = index%26
        result = char_lower[index]
        return result
    else :
        return char

def decrypt_char(char,place):
    char_upper = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    char_lower = char_upper.lower()

    if char in char_upper:
        place = place%26
        index = char_upper.index(char) - place
        index = index%26
        result = char_upper[index]
        return result
    elif char in char_lower:
        place = place%26
        index = char_lower.index(char) - place
        index = index%26
        result = char_lower[index]
        return result
    else :
        return char

# GUI
def caesar_enc(text):
    place = selectbox("Shift",range(0,260))
    result = caesar_encrypt(text,place)
    text_area("Cipher Text",result)

def caesar_dec(text):
    place = selectbox("Shift",range(0,260))
    result = caesar_decrypt(text,place)
    text_area("Decrypted Text",result)


