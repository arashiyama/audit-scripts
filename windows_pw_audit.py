import re
import ldap

def check_password_strength(password):
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
    # If the password passed all checks, it is considered strong
    return "Strong"

# Connect to the AD server
server = "ldap://ad.example.com"
bind_dn = "cn=admin,dc=example,dc=com"
bind_pw = "password"
conn = ldap.initialize(server)
conn.simple_bind_s(bind_dn, bind_pw)

# Search for all user accounts in the AD
search_filter = "(objectClass=user)"
result = conn.search_s("dc=example,dc=com", ldap.SCOPE_SUBTREE, search_filter)

# Check the strength of the password for each user account
for dn, entry in result:
username = entry["sAMAccountName"][0]
password = input("Enter the password for {}: ".format(username))
strength = check_password_strength(password)
print("{}'s password is {}".format(username, strength))

Disconnect from the AD server
conn.unbind()

