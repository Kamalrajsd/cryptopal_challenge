from mycryptolib import *
#question 1
print 'question 1'
str_hex = '49276d206b696c6c696e6720796f757220627261696e206c696b65206120706f69736f6e6f7573206d757368726f6f6d'
str_base64 = 'SSdtIGtpbGxpbmcgeW91ciBicmFpbiBsaWtlIGEgcG9pc29ub3VzIG11c2hyb29t'
print str_base64 == hex_to_base64(str_hex)
 
#question 2
print 'question 2'
print '746865206b696420646f6e277420706c6179' == hex_xor('1c0111001f010100061a024b53535009181c', '686974207468652062756c6c277320657965')
