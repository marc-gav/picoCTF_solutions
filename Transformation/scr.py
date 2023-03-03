with open('enc', 'r', encoding='utf-8') as f:
    flag = f.read()

res = ''

for c in flag:
    first_byte = ord(c) >> 8
    second_byte = ord(c) & 0xff
    first_ascii = chr(first_byte)
    second_ascii = chr(second_byte)
    res += first_ascii + second_ascii

print(res)