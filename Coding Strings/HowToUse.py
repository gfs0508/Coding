from coding import *

var = "string to encoder"

var_enc = code.encoder(var) # encoding string "var"
print(var_enc)

var_dec = code.decoder(var_enc) # decoding string "var"
print(var_dec)
