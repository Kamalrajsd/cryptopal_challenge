dic_hex_dec = {
    '0': 0,
    '1': 1,
    '2': 2,
    '3': 3,
    '4': 4,
    '5': 5,
    '6': 6,
    '7': 7,
    '8': 8,
    '9': 9,
    'a': 10,
    'b': 11,
    'c': 12,
    'd': 13,
    'e': 14,
    'f': 15

}
str_dec_hec ='0123456789abcdef'
str_dec_base64 = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/'

def hex_to_bin(str_hex):
    str_bin = ''

    for c in str_hex:
        str_bin += ('000' + bin(dic_hex_dec[c])[2:])[-4:]

    return str_bin

def bin_to_hex(str_bin):
    str_hex = ''

    str_bin += (4 -len(str_bin) % 4 if len(str_bin) % 4 > 0 else 0) * '0'

    for i in range(0, len(str_bin),4):
        str_hex += str_dec_hec[int(str_bin[i: i+4],2)]

    return str_hex


def hex_xor(str_hex1, str_hex2):

    str_bin1 = hex_to_bin(str_hex1)
    str_bin2 = hex_to_bin(str_hex2)
    str_bin_output = ''

    if len(str_bin1) == len(str_bin2):
        for i in range(len(str_bin2)):
            str_bin_output +=  '0' if str_bin1[i] == str_bin2[i] else '1'

        return bin_to_hex(str_bin_output)
    else:
        raise Exception('The inputs cannot be XORed')




def hex_to_base64(str_hex):
    str_base64 = ''

    str_bin = hex_to_bin(str_hex)

    str_bin += (6 -len(str_bin) % 6 if len(str_bin) % 6 > 0 else 0) * '0'

    for i in range(0, len(str_bin),6):
        str_base64 += str_dec_base64[int(str_bin[i: i+6],2)]

    return str_base64
