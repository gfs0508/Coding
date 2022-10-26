# Coding System created by GFS-0508
# For more details visit: https://github.com/GFS-0508/Python-Projects/tree/main/Coding%20Strings
# Visit my GitHub please: https://github.com/GFS-0508


class code:
    def encoder(string_TOenc, mode):
        if (mode == "s" or mode == "string"):
            string = " "
            for pos,char in enumerate(string_TOenc):
                # --------------------------
                if(char == " "):
                    string = string + "0"
                elif(char == "\n"):
                    string = string + "1"
                elif(char == "_"):
                    string = string + "2"
                elif(char == "-"):
                    string = string + "3"
                elif(char == "."):
                    string = string + "4"
                elif(char == ":"):
                    string = string + "5"
                elif(char == "-"):
                    string = string + "6"
                elif(char == ","):
                    string = string + "7"
                elif(char == ";"):
                    string = string + "8"
                elif(char == '"'):
                    string = string + "9"
                # --------------------------

                # --------------------------
                elif(char == "a"):
                    string = string + "p"
                elif(char == "A"):
                    string = string + "o" 

                elif(char == "b"):
                    string = string + "i"
                elif(char == "B"):
                    string = string + "u"

                elif(char == "c"):
                    string = string + "y"
                elif(char == "C"):
                    string = string + "t"

                elif(char == "d"):
                    string = string + "r"
                elif(char == "D"):
                    string = string + "e"

                elif(char == "e"):
                    string = string + "w"
                elif(char == "E"):
                    string = string + "q"
                
                elif(char == "f"):
                    string = string + "P"
                elif(char == "F"):
                    string = string + "O"

                elif(char == "g"):
                    string = string + "I"
                elif(char == "G"):
                    string = string + "U"

                elif(char == "h"):
                    string = string + "Y"
                elif(char == "H"):
                    string = string + "T"

                elif(char == "i"):
                    string = string + "R"
                elif(char == "I"):
                    string = string + "E"

                elif(char == "j"):
                    string = string + "W"
                elif(char == "J"):
                    string = string + "Q"

                elif(char == "k"):
                    string = string + "l"
                elif(char == "K"):
                    string = string + "k"

                elif(char == "l"):
                    string = string + "j"
                elif(char == "L"):
                    string = string + "h"

                elif(char == "m"):
                    string = string + "g"
                elif(char == "M"):
                    string = string + "f"

                elif(char == "n"):
                    string = string + "d"
                elif(char == "N"):
                    string = string + "s"

                elif(char == "o"):
                    string = string + "a"
                elif(char == "O"):
                    string = string + "L"
                    
                elif(char == "p"):
                    string = string + "K"
                elif(char == "P"):
                    string = string + "J"

                elif(char == "q"):
                    string = string + "H"
                elif(char == "Q"):
                    string = string + "G"

                elif(char == "r"):
                    string = string + "F"
                elif(char == "R"):
                    string = string + "D"

                elif(char == "s"):
                    string = string + "S"
                elif(char == "S"):
                    string = string + "A"

                elif(char == "t"):
                    string = string + "m"
                elif(char == "T"):
                    string = string + "n"

                elif(char == "u"):
                    string = string + "b"
                elif(char == "U"):
                    string = string + "v"

                elif(char == "v"):
                    string = string + "c"
                elif(char == "V"):
                    string = string + "x"

                elif(char == "w"):
                    string = string + "z"
                elif(char == "W"):
                    string = string + "M"

                elif(char == "x"):
                    string = string + "N"
                elif(char == "X"):
                    string = string + "B"

                elif(char == "y"):
                    string = string + "V"
                elif(char == "Y"):
                    string = string + "C"

                elif(char == "z"):
                    string = string + "X"
                elif(char == "Z"):
                    string = string + "Z"

            return string

        if (mode == "f" or mode == "file"):
            file = open(string_TOenc)
            val = file.read()
            val_enc = code.encoder(val, "s")
            file.close()
            file = open(string_TOenc, "w")
            file.write(val_enc)
            file.close()
            return val_enc
        
    def decoder(string_TOdec, mode):
        string = ""
        if (mode == "s" or mode == "string"):
            for pos,char in enumerate(string_TOdec):
                # --------------------------
                if(char == "0"):
                    string = string + " "
                elif(char == "1"):
                    string = string + "\n"
                elif(char == "2"):
                    string = string + "_"
                elif(char == "3"):
                    string = string + "-"
                elif(char == "4"):
                    string = string + "."
                elif(char == "5"):
                    string = string + ":"
                elif(char == "6"):
                    string = string + "-"
                elif(char == "7"):
                    string = string + ","
                elif(char == "8"):
                    string = string + ";"
                elif(char == '9'):
                    string = string + '"'
                # --------------------------

                # --------------------------
                elif(char == "p"):
                    string = string + "a"
                elif(char == "o"):
                    string = string + "A" 

                elif(char == "i"):
                    string = string + "b"
                elif(char == "u"):
                    string = string + "B"

                elif(char == "y"):
                    string = string + "c"
                elif(char == "t"):
                    string = string + "C"

                elif(char == "r"):
                    string = string + "d"
                elif(char == "e"):
                    string = string + "D"

                elif(char == "w"):
                    string = string + "e"
                elif(char == "q"):
                    string = string + "E"

                elif(char == "P"):
                    string = string + "f"
                elif(char == "O"):
                    string = string + "F"
                
                elif(char == "I"):
                    string = string + "g"
                elif(char == "U"):
                    string = string + "G"

                elif(char == "Y"):
                    string = string + "h"
                elif(char == "T"):
                    string = string + "H"

                elif(char == "R"):
                    string = string + "i"
                elif(char == "E"):
                    string = string + "I"

                elif(char == "W"):
                    string = string + "j"
                elif(char == "Q"):
                    string = string + "J"

                elif(char == "l"):
                    string = string + "k"
                elif(char == "k"):
                    string = string + "K"

                elif(char == "j"):
                    string = string + "l"
                elif(char == "h"):
                    string = string + "L"

                elif(char == "g"):
                    string = string + "m"
                elif(char == "f"):
                    string = string + "M"

                elif(char == "d"):
                    string = string + "n"
                elif(char == "s"):
                    string = string + "N"

                elif(char == "a"):
                    string = string + "o"
                elif(char == "L"):
                    string = string + "O"

                elif(char == "K"):
                    string = string + "p"
                elif(char == "J"):
                    string = string + "P"
                    
                elif(char == "H"):
                    string = string + "q"
                elif(char == "G"):
                    string = string + "Q"

                elif(char == "F"):
                    string = string + "r"
                elif(char == "D"):
                    string = string + "R"

                elif(char == "S"):
                    string = string + "s"
                elif(char == "A"):
                    string = string + "S"

                elif(char == "m"):
                    string = string + "t"
                elif(char == "n"):
                    string = string + "T"

                elif(char == "b"):
                    string = string + "u"
                elif(char == "v"):
                    string = string + "U"

                elif(char == "c"):
                    string = string + "v"
                elif(char == "x"):
                    string = string + "V"

                elif(char == "z"):
                    string = string + "w"
                elif(char == "M"):
                    string = string + "W"

                elif(char == "N"):
                    string = string + "x"
                elif(char == "B"):
                    string = string + "X"

                elif(char == "V"):
                    string = string + "y"
                elif(char == "C"):
                    string = string + "Y"

                elif(char == "X"):
                    string = string + "z"
                elif(char == "Z"):
                    string = string + "Z"

            return string

        if (mode == "f" or mode == "file"):
            file = open(string_TOdec)
            val = file.read()
            val_dec = code.decoder(val, "s")
            file.close()
            file = open(string_TOdec, "w")
            file.write(val_dec)
            file.close()
            return val_dec
