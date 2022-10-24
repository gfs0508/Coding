# Coding System created by GFS-0508
# For more details visit: 
# Visit my GitHub please: https://github.com/GFS-0508

class code:
    def encoder(string_TOenc):
        string_enc = " "
        for pos,char in enumerate(string_TOenc):
            if(char == " "):
                string_enc = string_enc + "0"
            if(char == "a"):
                string_enc = string_enc + "1"
            if(char == "b"):
                string_enc = string_enc + "2"
            if(char == "c"):
                string_enc = string_enc + "3"
            if(char == "d"):
                string_enc = string_enc + "4"
            if(char == "e"):
                string_enc = string_enc + "5"
            if(char == "f"):
                string_enc = string_enc + "6"
            if(char == "g"):
                string_enc = string_enc + "7"
            if(char == "h"):
                string_enc = string_enc + "8"
            if(char == "i"):
                string_enc = string_enc + "9"
            if(char == "j"):
                string_enc = string_enc + "A"
            if(char == "k"):
                string_enc = string_enc + "B"
            if(char == "l"):
                string_enc = string_enc + "C"
            if(char == "m"):
                string_enc = string_enc + "D"
            if(char == "n"):
                string_enc = string_enc + "E"
            if(char == "o"):
                string_enc = string_enc + "F"
            if(char == "p"):
                string_enc = string_enc + "G"
            if(char == "q"):
                string_enc = string_enc + "H"
            if(char == "r"):
                string_enc = string_enc + "I"
            if(char == "s"):
                string_enc = string_enc + "J"
            if(char == "t"):
                string_enc = string_enc + "K"
            if(char == "u"):
                string_enc = string_enc + "L"
            if(char == "v"):
                string_enc = string_enc + "M"
            if(char == "w"):
                string_enc = string_enc + "N"
            if(char == "x"):
                string_enc = string_enc + "O"
            if(char == "y"):
                string_enc = string_enc + "P"
            if(char == "z"):
                string_enc = string_enc + "Q"

        return string_enc
        
    def decoder(string_TOdec):
        string_dec = ""
        for pos,char in enumerate(string_TOdec):
            if(char == "0"):
                string_dec = string_dec + " "
            if(char == "1"):
                string_dec = string_dec + "a"
            if(char == "2"):
                string_dec = string_dec + "b"
            if(char == "3"):
                string_dec = string_dec + "c"
            if(char == "4"):
                string_dec = string_dec + "d"
            if(char == "5"):
                string_dec = string_dec + "e"
            if(char == "6"):
                string_dec = string_dec + "f"
            if(char == "7"):
                string_dec = string_dec + "g"
            if(char == "8"):
                string_dec = string_dec + "h"
            if(char == "9"):
                string_dec = string_dec + "i"
            if(char == "A"):
                string_dec = string_dec + "j"
            if(char == "B"):
                string_dec = string_dec + "k"
            if(char == "C"):
                string_dec = string_dec + "l"
            if(char == "D"):
                string_dec = string_dec + "m"
            if(char == "E"):
                string_dec = string_dec + "n"
            if(char == "F"):
                string_dec = string_dec + "o"
            if(char == "G"):
                string_dec = string_dec + "p"
            if(char == "H"):
                string_dec = string_dec + "q"
            if(char == "I"):
                string_dec = string_dec + "r"
            if(char == "J"):
                string_dec = string_dec + "s"
            if(char == "K"):
                string_dec = string_dec + "t"
            if(char == "L"):
                string_dec = string_dec + "u"
            if(char == "M"):
                string_dec = string_dec + "v"
            if(char == "N"):
                string_dec = string_dec + "w"
            if(char == "O"):
                string_dec = string_dec + "x"
            if(char == "P"):
                string_dec = string_dec + "y"
            if(char == "Q"):
                string_dec = string_dec + "z"

        return string_dec
