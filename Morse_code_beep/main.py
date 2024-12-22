import time
import platform

# Morse code dictionary
morse_code_dict = {
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
    '0': '-----',
    '1': '.----',
    '2': '..---',
    '3': '...--',
    '4': '....-',
    '5': '.....',
    '6': '-....',
    '7': '--...',
    '8': '---..',
    '9': '----.',
    '.': '.-.-.-',
    ',': '--..--',
    '?': '..--..',
    "'": '.----.',
    '!': '-.-.--',
    '/': '-..-.',
    '(': '-.--.',
    ')': '-.--.-',
    '&': '.-...',
    ':': '---...',
    ';': '-.-.-.',
    '=': '-...-',
    '+': '.-.-.',
    '-': '-....-',
    '_': '..--.-',
    '"': '.-..-.',
    '$': '...-..-',
    '@': '.--.-.',
    ' ': '/'
}

def play_sound(duration):
    # For Windows
    if platform.system() == 'Windows':
        import winsound
        winsound.Beep(1000, duration)  # Beep at 1000 Hz for 'duration' milliseconds
    # For Linux/macOS
    else:
        import os
        os.system('printf "\a"')  # Produces system beep

def text_to_morse(text):
    morse_code = ''
    for char in text.upper():
        if char in morse_code_dict:
            morse_code += morse_code_dict[char] + ' '
        else:
            morse_code += '/ '  # If character is not found, consider it as a space
    return morse_code

def morse_to_sound(morse_code):
    for symbol in morse_code:
        if symbol == '.':
            play_sound(100)  # Dot duration: 100 milliseconds
        elif symbol == '-':
            play_sound(300)  # Dash duration: 300 milliseconds
        elif symbol == ' ':
            time.sleep(0.3)  # Pause between characters: 300 milliseconds
        elif symbol == '/':
            time.sleep(0.7)  # Pause between words: 700 milliseconds

if __name__ == '__main__':
    # Get input from user
    text = input("Enter text to convert to Morse code: ")
    
    # Convert text to Morse code
    morse = text_to_morse(text)
    print("Morse Code:", morse)
    
    # Convert Morse code to sound
    morse_to_sound(morse)
