english_letters = [
    "a",
    "b",
    "c",
    "d",
    "e",
    "f",
    "g",
    "h",
    "i",
    "j",
    "k",
    "l",
    "m",
    "n",
    "o",
    "p",
    "q",
    "r",
    "s",
    "t",
    "u",
    "v",
    "w",
    "x",
    "y",
    "z",
]

morse_code = [
    ".-",
    "-...",
    "-.-.",
    "-..",
    ".",
    "..-.",
    "--.",
    "....",
    "..",
    ".---",
    "-.-",
    ".-..",
    "--",
    "-.",
    "---",
    ".--.",
    "--.-",
    ".-.",
    "...",
    "- ",
    "..-",
    "...-",
    ".--",
    "-..-",
    "-.--",
    "--..",
]
english_to_morse_code = {
    english_letters[i]: morse_code[i] for i in range(len(english_letters))
}
english_to_morse_code[" "] = " "


def encrypt():
    entry = input("What would you like to convert to morse code?: ").lower()
    encrypted_entry = ""
    for letter in entry:
        encrypted_entry += english_to_morse_code[letter]
    print(encrypted_entry)


encrypt()
