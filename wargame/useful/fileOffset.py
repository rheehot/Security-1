_data_offset = 0x2400
with open("./chall6.exe", "rb") as f:
    data = f.read()
    n = data[_data_offset+0x20:_data_offset+0xff]
    enc_flag = data[_data_offset:_data_offset+0x12]

dec_flag = ""
for j in range(len(enc_flag)):
    for i in range(0x20, 0x7e):
        if enc_flag[j] == n[i]:
            dec_flag += chr(i)

print(dec_flag)
