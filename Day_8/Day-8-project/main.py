from art import logo
print(logo)

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))

#TODO-1: Create a function called 'encrypt' that takes the 'text' and 'shift' as inputs.

def encrypt(text, shift):
  print("ENCRYPTING MESSAGE...")
  
  # Reduce the loops of the shift
  shift = shift % 26

  # Convert text into a list
  text_list = list(text)
  encrypted_list = list()
  
  # Make a list of ascii values
  for i in range(0, len(text_list)):
    encrypted_list.append( ord(text_list[i]) )

  # Convert ascii values
  for i in range(0, len(text_list)):
    # If space bar, do not change
    if(encrypted_list[i] != 32):
      if(encrypted_list[i] > 122 - shift):
        text_list[i] = chr(encrypted_list[i] + shift - 26)    
      else:
        text_list[i] = chr(encrypted_list[i] + shift)

  print("Your encrypted message is: " + ''.join(text_list))

def decrypt(text, shift):
  print("DECRYPTING MESSAGE...")
  # Reduce the loops, and make negative
  shift = shift % 6
  
  # Convert text into a list
  text_list = list(text)
  decrypted_list = list()
  
  # Make a list of ascii values
  for i in range(0, len(text_list)):
    decrypted_list.append( ord(text_list[i]) )

  # Convert ascii values
  for i in range(0, len(text_list)):
    # If space bar, do not change
    if(decrypted_list[i] != 32):
      if(decrypted_list[i] < 97 + shift):
        text_list[i] = chr(decrypted_list[i] - shift + 26)    
      else:
        text_list[i] = chr(decrypted_list[i] - shift)

  print("Your decrypted message is: " + ''.join(text_list))


#TODO-3: Call the encrypt function and pass in the user inputs. You should be able to test the code and encrypt a message. 

if (direction == "encode"):
  encrypt(text, shift)
elif (direction == "decode"):
  decrypt(text, shift)
else:
  print("Invalid direction given")
