import crypt

def check_password_strength(encrypted_password, password):
    # Check the length of the password
    if len(password) < 8:
        return "Weak: Password is too short"
    # Check for the presence of uppercase and lowercase letters, digits, and special characters
    if not re.search(r'[A-Z]', password) or not re.search(r'[a-z]', password) or not re.search(r'[0-9]', password) or not re.search(r'[^A-Za-z0-9]', password):
        return "Weak: Password is missing required character types"
    # Check if the password is a common one
    with open('common_passwords.txt', 'r') as f:
        common_passwords = [line.strip() for line in f]
        if password in common_passwords:
            return "Weak: Password is a common one"
    # Check if the password can be easily guessed by cracking the encrypted password
    salt = encrypted_password[:2]
    with open('dictionary.txt', 'r') as f:
        for word in f:
            word = word.strip()
            # Encrypt the word using the same salt as the encrypted password
            encrypted_word = crypt.crypt(word, salt)
            # If the encrypted word matches the encrypted password, the password is considered weak
            if encrypted_word == encrypted_password:
                return "Weak: Password is easily guessable"
    # If the password passed all checks, it is considered strong
    return "Strong"

# Test the function with an example encrypted passwd file
with open('encrypted_passwd.txt', 'r') as f:
    for line in f:
        username, encrypted_password, _, _, _, _, _ = line.split(':')
        password = input("Enter the password for {}: ".format(username))
        strength = check_password_strength(encrypted_password, password)
        print("{}'s password is {}".format(username, strength))
