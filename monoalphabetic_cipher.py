# libraries
from streamlit import text_area

# Variables
plain_upper = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
cipher_upper = ['R', 'U', 'T', 'O', 'Q', 'Y', 'W', 'B', 'H', 'C', 'A', 'I', 'E', 'X', 'L', 'Z', 'V', 'K', 'F', 'D', 'M', 'J', 'P', 'S', 'G', 'N']
cipher_lower = ['r', 'u', 't', 'o', 'q', 'y', 'w', 'b', 'h', 'c', 'a', 'i', 'e', 'x', 'l', 'z', 'v', 'k', 'f', 'd', 'm', 'j', 'p', 's', 'g', 'n']
plain_lower = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

def monoalpha_enc(text):
    result = ""
    for i in text:
        result += encrypt_char(i)
    return(result)
    
def monoalpha_dec(text):
    result = ""
    for i in text:
        result += decrypt_char(i)
    return(result)
    
def encrypt_char(char):
    if char.islower():
        idx = plain_lower.index(char)
        return(cipher_lower[idx])
    elif char.isupper():
        idx = plain_upper.index(char)
        return(cipher_upper[idx])
    else:
        return(char)

def decrypt_char(char):
    if char.islower():
        idx = cipher_lower.index(char)
        return(plain_lower[idx])
    elif char.isupper():
        idx = cipher_upper.index(char)
        return(plain_upper[idx])
    else:
        return(char)
    
# GUI
def ma_enc(text):
    result = monoalpha_enc(text)
    text_area("Cipher Text",result)

def ma_dec(text):
    result = monoalpha_dec(text)
    text_area("Decrypted Text",result)


