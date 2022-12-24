dot = "."
line = "___"
# make dict for chane user input to morse code
# I use some emoji to make it look better
morse_dict = {
    "A": f"{dot} {line}",
    "B": f"{line} {dot} {dot} {dot}",
    "C": f"{line} {dot} {line} {dot}",
    "D": f"{line} {dot} {dot}",
    "E": f"{dot}",
    "F": f"{dot} {dot} {line} {dot}",
    "G": f"{line} {line} {dot}",
    "H": f"{dot} {dot} {dot} {dot}",
    "I": f"{dot} {dot}",
    "J": f"{dot} {line} {line} {line}",
    "K": f"{line} {dot} {line}",
    "L": f"{dot} {line} {dot} {dot}",
    "M": f"{line} {line}",
    "N": f"{line} {dot}",
    "O": f"{line} {line} {line}",
    "P": f"{dot} {line} {line} {dot}",
    "Q": f"{line} {line} {dot} {line}",
    "R": f"{dot} {line} {dot}",
    "S": f"{dot} {dot} {dot}",
    "T": f"{line}",
    "U": f"{dot} {dot} {line}",
    "V": f"{dot} {dot} {dot} {line}",
    "W": f"{dot} {line} {line}",
    "X": f"{line} {dot} {dot} {line}",
    "Y": f"{line} {dot} {line} {line}",
    "Z": f"{line} {line} {dot} {dot}",
    "1": f"{dot} {line} {line} {line} {line}",
    "2": f"{dot} {dot} {line} {line} {line}",
    "3": f"{dot} {dot} {dot} {line} {line}",
    "4": f"{dot} {dot} {dot} {dot} {line}",
    "5": f"{dot} {dot} {dot} {dot} {dot}",
    "6": f"{line} {dot} {dot} {dot} {dot}",
    "7": f"{line} {line} {dot} {dot} {dot}",
    "8": f"{line} {line} {line} {dot} {dot}",
    "9": f"{line} {line} {line} {line} {dot}",
    "0": f"{line} {line} {line} {line} {line}"

}
symbols = ["!", "@", "#", "%", "^", "&", "*", "(", ")",
           "=", "+", "-", "_", ";", ",", ">", "<", "?",
           "/", "]", "[", "{", "}", "`", "~"]

logo = str(
    "\n\n"
    "___  ___                      _____           _\n"
    "|  \/  |                     /  __ \         | |  \n"
    "| .  . | ___  _ __ ___  ___  | /  \/ ___   __| | ___\n"
    "| |\/| |/ _ \| '__/ __|/ _ \ | |    / _ \ / _` |/ _ \n"
    "| |  | | (_) | |  \__ |  __/ | \__/| (_) | (_| |  __/\n"
    "\_|  |_/\___/|_|  |___/\___|  \____/\___/ \__,_|\___|"

)
