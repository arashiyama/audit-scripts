'''
fuxx a binary 
jonc@lacunae.org
'''
import subprocess
import random
import string

def fuzz(binary):
    # Generate a random input string of variable length
    input_str = ''.join(random.choice(string.ascii_letters) for _ in range(random.randint(1, 1000)))
    
    # Run the binary with the random input string as an argument
    try:
        output = subprocess.check_output([binary, input_str])
    except subprocess.CalledProcessError as e:
        output = e.output
    
    # Check if the binary crashed or not
    if output == b'':
        print("Crash detected!")
        print("Input string:", input_str)
    else:
        print("No crash detected.")

# Fuzz the binary indefinitely
while True:
    fuzz("binary_to_fuzz")
