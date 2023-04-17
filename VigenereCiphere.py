# Kristine Joy Barrina # BSCPE 1-5 # April 5, 2023
# Creating a program that encrypts a plaintext and key

# PSEUDOCODE

# Import modules
import tkinter as tk
from tkinter import *
from pyfiglet import Figlet
from termcolor import colored
from colorama import Style, Back

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

# Let the user input the key
    key = str (input ("Enter the key: "))

# Display an error message when there's a space in key   

    def has_space (key):
        return " " in key

    key_space = (has_space(key))

    if key_space == False:
        loop_ctrl_key += 1
        
#    Display an error message when there's a lowercase in key
        if key.isupper() == True:
            loop_ctrl_key += 1

        else:
            print ("Input the key in uppercase!\n") 
            loop_ctrl_key = 0

    else:
        print ("Input the key with no spaces!\n")
        loop_ctrl_key = 0

# Get the character length of message and key input
plaintext_length = len (plaintext)
key_length = len (key)

# Convert the plaintext to its integer equivalent using ord
for i in range (plaintext_length):
    plaintext_char_value.append (ord (plaintext [i]))

# Convert the key to its integer equivalent using ord
for i in range (key_length):
    key_char_value. append (ord (key [i]))

# Define a function called "encrypt"
def encrypt (plaintext, key):

#   Create a variable with empty strings
    ciphertext = ""
    for i in range (len(plaintext_char_value)):  

#       Add numbers then take the result of mod 26
        character_value = (plaintext_char_value [i] + key_char_value [i % key_length]) % 26

#       Add 65 to get the ciphertext
        ciphertext += chr (character_value + 65)

#   Return the value
    return ciphertext

# Call the function and display the output
encrypted_code = (encrypt(plaintext, key))

# Displaying a notice message that the user got the code
notice_message = Figlet (font = "standard")
print (colored (notice_message.renderText("YOU GOT THE CIPHERTEXT"), "yellow"))

# Designing the output through tkinter
# Create an instance tkinter window or frame
root = Tk ()

# Create the dimension of window
root. geometry ("400x250")
root.title ("Encrypted Code")


# Designing the output then display it

tk.mainloop()