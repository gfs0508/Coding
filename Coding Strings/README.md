<h1 align=center>
Python Projects - Coding
<h1>

<p align=center>  
<a>About | Versions and Updates</a>
</p>
  
## :question:	 About
- :fire: Simple coding using python
  
## Versions and Updates
  
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
  
