# Coding System created by GFS-0508
# For more details visit: https://github.com/GFS-0508/Python-Projects/
# Visit my GitHub please: https://github.com/GFS-0508

try:
    import os
except ImportError:
    print("Error while import library: os")

try:
    import sys
except:
    print("Error while import library: sys")

VERSION = 2.00

# MODES
F = "f"
FP = "f+"
FM = "f-"
S = "s"

key = "é1q=wáé2Q@âe3àÃr£W4í<út'}§5yE>{\t6uãi[7õRo]8pT*ó9+Y`0´U\n^ù~IasOdfPghAjkSlçDÉºªFzxGcvHbÈnèJm,K;.L:)-Ç_ Z!X#C$VB&N/M(?" 

SELECTED_KEY = key

class code:
    def encoder(string, mode, SELECTED_KEY):
        if (mode == S or mode == "s" or mode == "string"):
            global string_enc
            string_enc = ""
            for char in string: 
                try: string_enc = string_enc + SELECTED_KEY[SELECTED_KEY.find(char)+1]
                except: string_enc = string_enc + SELECTED_KEY[0]
            return string_enc
        if (mode == F or mode == "f" or mode == "file"):
            try:
                file = open(string)
                val = file.read()
                val_enc = code.encoder(val, "s", SELECTED_KEY)
                file.close()
                file = open(string, "w")
                file.write(val_enc)
                file.close()
                return val_enc
            except: print("Error: No such file or directory")
        if (mode == FP or mode == "f+" or mode == "file+"):
            try:
                file2 = open(string)
                val2 = file2.read()
                val_enc2 = code.encoder(val2, "s", SELECTED_KEY)
                file2.close()
                file2 = open(string, "w")
                file2.write(val_enc2)
                file2.close()
                new_name = code.encoder(file2.name, "s", SELECTED_KEY)
                os.rename(file2.name, new_name + ".cef")
                return val_enc2
            except: print("Error: No such file or directory")
    def decoder(string_TOdec, mode, SELECTED_KEY):
        if (mode == S or mode == "s" or mode == "string"):
            string_dec = ""
            for char2 in string_TOdec: 
                try: string_dec = string_dec + SELECTED_KEY[SELECTED_KEY.find(char2)-1]
                except: string_dec = string_dec + SELECTED_KEY[0]
            return string_dec
        if (mode == F or mode == "f" or mode == "file"):
            try:
                file = open(string_TOdec)
                val = file.read()            
                val_dec = code.decoder(val, "s", SELECTED_KEY)
                file.close()
                file = open(string_TOdec, "w")
                file.write(val_dec)
                file.close()
                return val_dec
            except: print("Error: No such file or directory")
        if (mode == FP or mode == "f+" or mode == "file+"):
            try:
                file2 = open(string_TOdec)
                val2 = file2.read()
                val_dec2 = code.decoder(val2, "s", SELECTED_KEY)
                file2.close()
                file2 = open(string_TOdec, "w")
                file2.write(val_dec2)
                file2.close()
                new_name = code.decoder(file2.name, "s", SELECTED_KEY)
                os.rename(file2.name, new_name.replace(code.decoder(".cef", "s", SELECTED_KEY),""))
                return val_dec2
            except: print("Error: No such file or directory")
        if (mode == FM or mode == "f-" or mode == "file-"):
            try:
                file3 = open(string_TOdec)
                val3 = file3.read()
                val_dec3 = code.decoder(val3, "s" ,key)
                file3.close()
                return val_dec3
            except: print("Error: No such file or directory")

for i in range(0, 2):
    try:
        if sys.argv[i] == "-h": 
            print("\n"
                "\tCoding by GFS-0508\n"
                "\t-h  -> show menu\n"
                "\t-v  -> show version\n"
                "\t-s  -> mode: string\n"
                "\t-f  -> mode: file\n"
                "\t-f+ -> mode: file and title\n"
                "\t-f- -> mode: file without modifications\n"
                "\t-e  -> encoder\n"
                "\t-d  -> decoder\n")
        elif sys.argv[i] == "-v": print(VERSION)

        elif sys.argv[i] == "-s":
            string = sys.argv[i+1]
            try:
                if sys.argv[i+2] == "-e":
                    string_enc = code.encoder(string, S, SELECTED_KEY)
                    print(string_enc)
                if sys.argv[i+2] == "-d":
                    string_dec = code.decoder(string, S, SELECTED_KEY)
                    print(string_dec)
            except: 
                print("Args. -e or -d not found") 
        elif sys.argv[i] == "-f":
            string = sys.argv[i+1]  
            try:
                if sys.argv[i+2] == "-e":
                    string_enc = code.encoder(string, F, SELECTED_KEY)
                    print(string_enc)
                if sys.argv[i+2] == "-d":
                    string_dec = code.decoder(string, F, SELECTED_KEY)
                    print(string_dec)
            except: 
                print("Args. -e or -d not found or file not found") 
        elif sys.argv[i] == "-f+":
            string = sys.argv[i+1]  
            try:
                if sys.argv[i+2] == "-e":
                    string_enc = code.encoder(string, FP, SELECTED_KEY)
                    print(string_enc)
                if sys.argv[i+2] == "-d":
                    string_dec = code.decoder(string, FP, SELECTED_KEY)
                    print(string_dec)
            except SystemExit: 
                print("Args. -e or -d not found or file not found") 
        elif sys.argv[i] == "-f-":
            string = sys.argv[i+1]  
            try:
                if sys.argv[i+2] == "-d":
                    string_dec = code.decoder(string, FM, SELECTED_KEY)
                    print(string_dec)
            except: 
                print("Args. -e or -d not found or file not found") 
        else: pass
    except: pass
