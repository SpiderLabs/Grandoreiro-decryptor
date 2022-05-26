# sample: ff908727cc1b5335e541fbcd80a327565f308bc7
''' encrypted strings and output
        34C116B01045F71235F1 - Santander
        7B89EE046F849392A4BF8747CA789F40964FF429 - TRAVASITE |Bradesco
        C34B8C35AF16C0689EE8739745F519C3187DF90509 - Internet Banking BNB
        3FC6025AF66E8B4EF53AF177AA49EB15BB5A8FF018D26E - AplicativoBradesco.exe
        A257F95BE223DB0E35F533EC113DEF1BA4578FBE78B675A254874AF522D76ABE66FE29D413CF0FC06DAF6BA2399325A25D9840EA39F116C178A324D97BBA699A599650F42FC678B145F11DBA74A64BFB2CE0133EEB23AA21BA193BF936F63DEC2AD909C6023BE51FDE16C47A9F48FA2FD07CA55088C16C91B77FBD689543F225AD1146F635D47FBA6F90B4688D4E8E44EC29EB1EC76BA0508B5CFE20CA749D35E1133AE91DC70371 - nuu|4|dinu|eglo|mrdw|lqtv|ckpd|cgkp|quyi|vyin|qvyi|vycn|osxc|loty|ilot|adgl|wbej|sehy|jnrf|zjnr|ruyj|hlqu|ybel|dhwb|jmpd|xbjo|pswb|zehm|dgxc|orfw|psgx|uxaf|aehm|ehmr|4
'''


def decrypt(cipher, key):
    plain = ''
    cipher = bytes.fromhex(cipher)
    for i in range(1, len(cipher)):
        n = cipher[i] ^ ord(key[(i-1) % len(key)])
        c = cipher[i-1]
        c = n - c if c < n else n + int(0xff) - c
        plain += chr(c)
    return plain


ciphertext = input('Input encrypted string: ')
key = 'F5454DNBVXCCEFD3EFMNBVDCMNXCEVXD3CMBKJHGFM'
print(f'{ciphertext} >> {decrypt(ciphertext, key)}')