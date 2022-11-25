MORSE_CODE_DICT = {
    'A': '.-',
    'B': '-...',
    'C': '-.-.',
    'D': '-..',
    'E': '.',
    'F': '..-.',
    'G': '--.',
    'H': '....',
    'I': '..',
    'J': '.---',
    'K': '-.-',
    'L': '.-..',
    'M': '--',
    'N': '-.',
    'O': '---',
    'P': '.--.',
    'Q': '--.-',
    'R': '.-.',
    'S': '...',
    'T': '-',
    'U': '..-',
    'V': '...-',
    'W': '.--',
    'X': '-..-',
    'Y': '-.--',
    'Z': '--..',
    '1': '.----',
    '2': '..---',
    '3': '...--',
    '4': '....-',
    '5': '.....',
    '6': '-....',
    '7': '--...',
    '8': '---..',
    '9': '----.',
    '0': '-----',
    ', ': '--..--',
    '.': '.-.-.-',
    '?': '..--..',
    '/': '-..-.',
    '-': '-....-',
    '(': '-.--.',
    ')': '-.--.-',
    ' ': '/'
}

# 1. Ask user for input
# 2. Read user's input
message = input("What is your message? ").upper()

print(f'Message = {message}')
print(f'Message Length = {len(message)}')

# 3. [optional] Validate user's input, ask again if invalid input
#TODO

# 4. Convert string into an array of characters --> dont need this as strings in python can already be iterated

# 5. Create an empty array for the translated message
translated_message = []

# 6. Iterate through the array and translate each code
for letter in message:
    print(f'{letter} = {MORSE_CODE_DICT[letter]}')
    translated_message.append(MORSE_CODE_DICT[letter])

# 7. Print out morse code
output = ""
for letter in translated_message:
    output += f'{letter} ' 

print("final output")
print(output)


