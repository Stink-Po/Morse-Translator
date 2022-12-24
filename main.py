import replit
from morse_dict import morse_dict, symbols, logo
import os

print(logo)
print("\n\nType '1' for Morse Code Rule, Type 'Encode' for Encode Your message, Type 'Decode'\n"
      "for Decode Your Message")
# explain morse code and rules of morse code to user
rules = ("\n\nInternational Morse Code\n"
         "We just accept letters and natural numbers how ever we delete other things base the morse rule\n"
         "The length of dot is one unit\n"
         "A dash is 3 units\n"
         "The Space between part of the same letter is '1' unit\n"
         "The Space between letters is '3' units\n"
         "The Space between words is '7' units\n")


# this function encode user entry to morse code and print the result in console
def encode(encode_entry):
    entry_symbol = ""
    # check the user entry and if there is a symbol we tell the user why we must delete the symbol
    for item in encode_entry:
        if item in symbols:
            print("I think You Enter a Symbol The Morse Code just Support the Alphabet and Integer\n"
                  "We remove this Symbol and Encode the Rest of your entry")
            entry_symbol += item
    clean_user_input = encode_entry.replace(entry_symbol, "")
    # split user input to a list
    input_list = clean_user_input.split(" ")
    # variable for output
    final_cod = ""

    # decode user input with for loop start with split input list
    for word in input_list:
        # avoid the Entry of symbol result in final output
        if word != "":
            # looping in each text in user input
            for txt in word:
                # looping into morse dict
                for (key, val) in morse_dict.items():
                    if txt.upper() == key:
                        # if text was equal to a key in morse dict we add value to the output
                        final_cod += val
                # add 3 space between each latter this is a morse rule
                final_cod += "   "
            # I decide to go to a new line and scape from adding 7 space between each word
            # and show the user what is the morse code of each word
            final_cod += f"=  {word}\n"

    # We have two output first one is for a user how don't use symbols in entry
    if entry_symbol == "":
        # finally show the user final output with morse code of each word entry
        print(f"\n\nThe Result for the {encode_entry} is : \n{final_cod}")
    else:
        # and this output for the user who don't follow the morse code rule
        print(f"\n\nThe result for the {clean_user_input} is :\n{final_cod}\n"
              f"we delete this {entry_symbol} form your input because the rule of Morse Code")

    if continue_decode_encode():
        start()
    else:
        print("Thank You for using my application")


# this function decode user entry and print the result in console
def decode(decode_entry):
    clean_entry = ""
    for item in decode_entry:
        if item == "." or item == "_" or item == " ":
            clean_entry += item
    print(clean_entry)
    # by the morse rules space between a words is 7:
    to_decode_list = clean_entry.split("       ")
    print(to_decode_list)
    final_decoded_message = ""
    for coded_word in to_decode_list:
        split_word = coded_word.split("   ")
        print(split_word)
        decoded_word = ""
        for coded_txt in split_word:
            for (key, val) in morse_dict.items():
                if coded_txt == val:
                    decoded_word += key
        final_decoded_message += f"{decoded_word} "

    print(f"This is Your Result for Your Entry : {final_decoded_message}")
    if continue_decode_encode():
        start()
    else:
        print("Thank You for using my application")


# this command clear the window
def clear():
    replit.clear()
    os.system("cls")


# this function ask user if you  want to continue to encode and decode and return True and False
def continue_decode_encode():
    want_continue = input("Do You want to 'Encode' or 'Decode' Again? Please Answer With (Y/N")
    if want_continue.upper() == "Y":
        return True
    elif want_continue.upper() == "N":
        return False
    else:
        print("Wrong Entry Try Again")
        continue_decode_encode()


def start():
    # ask user for a input
    user = user_inp = input("\nInput something we change it to morse for you:  ")
    if user == "1":
        print(rules)
        clear()
        start()
    elif user.lower() == "encode":
        encode_entry = input("\nEnter Somthing to Encode:\n")
        encode(encode_entry=encode_entry)
    elif user.lower() == "decode":
        decode_entry = input("\nEnter the Code you want to Decode:\n")
        decode(decode_entry=decode_entry)
    else:
        print("Wrong Entry Try Again")
        start()


start()
