# Libraries
import streamlit as st

# Importing Functions
from caesar_cipher import caesar_enc,caesar_dec
from monoalphabetic_cipher import ma_enc,ma_dec

# Layout 
st.title("Text Encryption/Decryption Techniques")

text = st.text_area('Enter or paste text Here',"")

col1, col2= st.columns(2)
with col1:
    cipher = ['Caesar Cipher','Mono-alphabetic Cipher','Homo-phonic Substitution Cipher','Polygram Substitution Cipher','Polyalphabetic Substitution Cipher','Playfair Cipher','Hill Cipher']
    tech = st.selectbox("Technique",cipher)

with col2:
    req = ["Encryption","Decryption"]
    demand = st.selectbox("Requirement",req)

st.caption('___')

if demand=='Encryption':
    if tech==cipher[0]:
        st.header("Caesar Cipher Encryption")
        caesar_enc(text)
    
    if tech==cipher[1]:
        st.header("Monoalphabetic Substitution Cipher Encryption")
        ma_enc(text)
        
    if tech==cipher[2]:
        pass
    if tech==cipher[3]:
        pass
    if tech==cipher[4]:
        pass
    if tech==cipher[5]:
        pass
    if tech==cipher[6]:    
        pass
    
elif demand=='Decryption':
    if tech==cipher[0]:
        st.header("Caesar Cipher Decryption")
        caesar_dec(text)
    
    if tech==cipher[1]:
        st.header("Monoalphabetic Substitution Cipher Decryption")
        ma_dec(text)
    
    if tech==cipher[2]:
        pass
    if tech==cipher[3]:
        pass
    if tech==cipher[4]:
        pass
    if tech==cipher[5]:
        pass
    if tech==cipher[6]:    
        pass