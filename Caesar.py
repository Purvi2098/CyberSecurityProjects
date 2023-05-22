###### Caesar cipher
# This Function will encrypt the text
def caesarEncrypt(text, shiftAmount):
    EnTxt = ""
    for char in text:
        if char.isalpha():
            Aval = ord(char)
            shiftedAscii = (Aval - ord('a') + shiftAmount) % 26 + ord('a')
            EnChar = chr(shiftedAscii)
            EnTxt += EnChar
        else:
            EnTxt += char
    return EnTxt

### This Function will decrypt the text
def caesarDecrypt(text):
    for shiftAmount in range(1, 26):
        DeTxt = ""
        for char in text:
            if char.isalpha():
                Aval = ord(char)
                shiftedAscii = (Aval - ord('a') - shiftAmount) % 26 + ord('a')
                DeChar = chr(shiftedAscii)
                DeTxt += DeChar
            else:
                DeTxt += char
        print("Shifted by " + str(shiftAmount) + " Char: " + DeTxt)

print("   ")
print("CAESAR CIPHER ENCRYPTION")
EnTxt = caesarEncrypt("hello, i am purvi patel", 3)
print("Encrypted text: " + EnTxt)

print("   ")
print("CAESAR CIPHER DECRYPTION")
caesarDecrypt(EnTxt)
