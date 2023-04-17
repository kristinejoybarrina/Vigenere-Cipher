# Kristine Joy Barrina # BSCPE 1-5 # April 5, 2023
# Creating a program that encrypts a plaintext and key

# PSEUDOCODE

# Initialize the variables
loop_ctrl_plaintext = 0
loop_ctrl_key = 0
key_char_value = []
plaintext_char_value = []

# Use while loop for error input (message)
while loop_ctrl_plaintext == 0:
    loop_ctrl_plaintext += 1   

# Let the user input a message
    plaintext = str (input ("Enter the message: " ))
    loop_ctrl_plaintext == 0   
# Display an error message when there's a space in message 
    def has_space (plaintext):
        return " " in plaintext

    plaintext_space = (has_space(plaintext))

    if plaintext_space == False:
        loop_ctrl_plaintext += 1
        
#      Display an error message when there's a lowercase in message
        if plaintext.isupper () == True:
            loop_ctrl_plaintext += 1

        else:
            print ("Input the message in uppercase!\n")
            loop_ctrl_plaintext = 0

    else:
        print ("Input the message with no spaces!\n")
        loop_ctrl_plaintext = 0

# Use while loop for error input (key)
while loop_ctrl_key == 0:
    print ("it's working!")
    loop_ctrl_key += 1


# Let the user input the key
# Display an error message when there's a space in key   
# Display an error message when there's a lowercase in key
# Convert the plaintext to its integer equivalent using ord
# Convert the key to its integer equivalent using ord
# Define a function
# Produce the ciphertext by taking result of mod 26 and adding 65
# Call the function and display the output
# Designing the output then displat it