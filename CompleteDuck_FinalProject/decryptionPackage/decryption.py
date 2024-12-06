#decryption.py

from cryptography.fernet import Fernet
 
 
def decrypt_movie_title(encrypted_title, key):
    """
    Decrypts an encrypted movie title using the provided key.
    @param encrypted_title bytes: The encrypted movie title.
    @param key bytes: The key used for decryption.
    @return str: The decrypted movie title.
    """
    # Initialize the Fernet object with the key
    fernet = Fernet(key)
    # Decrypt the title
    decrypted_title = fernet.decrypt(encrypted_title)
    # Convert bytes to string
    return decrypted_title.decode()
 
# Example usage
# Encrypted movie title (you should have this from the encryption step)
encrypted_title = b'gAAAAABnJ6xXc8WnJ2DxuUMI3yz9g4ZaGNGUd6TPU96o-rmP1YfrxSq387RxZtyEt2Hc1WNWXcsUaz5oWJGd_W7Gs6wNXMoDG7bnwSawyeXVmuNEP88HlA8='
# Key used for encryption/decryption (you should have this from the key generation step)
key = b'WVRqW7wUIQ1mgbz5PAonHGJn-XknVdDV74L_RNFjU0o='
 
# Decrypt the movie title
decrypted_movie_title = decrypt_movie_title(encrypted_title, key)
print(f"Decrypted movie title: {decrypted_movie_title}")