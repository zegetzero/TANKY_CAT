from base64 import b64encode
from base64 import b64decode #i had issues here im not sure why it wouldnt work without importing base64 but wtv (might be a bonk moment)
import base64    # this actually bothers me in class we only used from base64 import b64edecode
from Crypto.Cipher import AES
from Crypto.Protocol.KDF import PBKDF2     #  (password-based key derivation function 2) is the derivation basically hasing the hash + salt 
from Crypto.Util.Padding import pad ,unpad
from  Crypto.Random import get_random_bytes

class Chunkster:
    def __init__(self,master_password):
        # salt is used to add string of bytes before the encryption so even if the same password is used the output will be different
        self.salt = get_random_bytes(16)   # random salt (string) of 16 bytes
        self.key = PBKDF2(master_password,self.salt,dkLen=32,count=100000)
        
    def encryption(self,plaintext):
        cipher = AES.new(self.key ,AES.MODE_CBC)  # CBC mode encrypts data in blocks and relys on the orevious block to encrypt the next one
        # the IV is made randomyl by AES.new 
        iv=cipher.iv  # iv (initialization vector) i basically understood that its like salt but used in the blocks and trickles down to the next block??
        
        padded_data= pad(plaintext.encode(),AES.block_size)  
        #padding basically if the block has the slack(yes like fileslack) its added to the block in order to make it the same size as the block size (16 bytes for AES)
        ciphertext = cipher.encrypt(padded_data)
        # the iv is added to the beginning of the ciphertext so it can be used in decryption and then its encoded to base64 for safe transmission
        return b64encode(iv + ciphertext).decode('utf-8') 
    
    def decryption(self,ciphertext):
        try:
            combined_data = base64.b64decode(ciphertext)
            
            iv = combined_data[:16]  # the first 16 bytes are the iv (no secret)
            actual_ciphertext = combined_data[16:]  # the rest is the actual ciphertext (yes secret)
            
            cipher =AES.new(self.key,AES.MODE_CBC,iv=iv)  # the iv is used in decryption to reverse the encryption process
            
            raw_data = unpad(cipher.decrypt(actual_ciphertext),AES.block_size)  # the decrypted data is unpadded to get the original plaintext
            
            return raw_data.decode('utf-8')  
        except(ValueError,KeyError):
            return " ah ah  you didnt say the magic word"  
 
# chonkster is done | If there is typos no there isnt 

master_key="ImCooked09!"     # no explaintiond needed here its just the master key for the class come on bro
chunkster_class= Chunkster(master_key)          # calling the class


creditals= "username: admin, password: 123456"

encrypted_data= chunkster_class.encryption(creditals)   # read line 44

print(f"plaintext: {creditals}")
print(f"encrypted: {encrypted_data}")

decrypted_data= chunkster_class.decryption(encrypted_data)  

print(f"decrypted: {decrypted_data}")


 # for terminal testing only  you an comment out the above to test in terminal
 
if __name__ == "__main__":
    
    master_key = input("Enter your Master key: ")
    
    chunkster_class = Chunkster(master_key)
    usrname = input("Enter the username: ")
    password = input("Enter the password: ")
    creditals = f"username: {usrname}, password: {password}"
    
    encrypted_data = chunkster_class.encryption(creditals)
    
    print(f"\nEncrypted data: {encrypted_data}")
    
    
    print(f"Decrypted data: {chunkster_class.decryption(encrypted_data)}")
    
    input("\nPress Enter to exit...")