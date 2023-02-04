<h1 align=center>
Python Projects - Coding
</h1>

<p align=center>  
<a>About | Versions and Updates</a>
</p>
  
## :question:	 About
- :fire: Simple coding using python
  
## Versions and Updates

### Version 2.0.0

- [x] New encoding method
- [x] Possibility to change or add an encryption key
- [x] Possibility to code through a GUI
- [x] Possibility to start via a command line - cmd or terminal.

> In command line

| Function                     | Encode             | Decode              |
| -------------                | -------------      |-------------        |
| Strings                      | -s "String ENC" -e | -s "String Dec" -d  |
| Files Without Title of file  | -f "file.txt" -e   | -f "fileENC.txt" -d |
| Files With Title of file     | -f+ "file.txt" -e  | -f+ "fileENC.cef" -d|
| Files Without Modifications  |                    | -f- "fileENC.cef" -d|

> If you need help, use -h to show the help menu;

> Use -v to show the version;

> Change encryption key
- Look for "SELECTED_KEY" in "coding.py" and change the variable value to another key string.
- To make a new string key, write the desired characters into the string. There can only be one character of each.
- The default key can be modified, possibly it's normal that it doesn't make all the characters.

### Version 1.2.0

- [x] Added new special characters.
- [x] Possibility to encode the title of a file (.txt)
- [x] Possibility to decode, but not change the file.

> Encode and Decode files with title
```
from coding import *

file = "file.txt"

file_enc_title = " PRjw4mNm"

file_enc = code.encoder(file, "f+") # encoding file with mode=file+

file_dec = code.decoder(file_enc_title, "f+") # decoding file with mode=file+
```

> Decode file without writing
```
file_enc_title = " PRjw4mNm"

file_dec = code.decoder(file_enc_title, "f-") # decoding file with mode=file-
print(file_enc_title)

```

  
### Version 1.1.0
  
- [x] Added new characters: Uppercase and some special characters.
- [x] Possibility of encoding and decoding files (*.txt).
 
> Encode and Decode **Strings**
```
from coding import *

var = "strings to encode"

var_enc = code.encoder(var, "s") # encoding string "var" with mode=string
print(var_enc)

var_dec = code.decoder(var_enc, "s") # decoding string "var" with mode=string
print(var_dec)
```

> Encode and Decode **Files**
```
from coding import *
  
file_txt = "file.txt"
  
file_enc = code.encoder(var, "f") # encoding file "file_txt" with mode=file
file_dec = code.decoder(var_enc, "f") # decoding file "file_txt" with mode=file
```

### Version 1.0.0

- [x] Encode and decode strings.
  
