import re

# Baca file .slk
with open("promosijabatan.slk", "r") as file:
    content = file.read()

# Cari semua nilai CHAR(x)
char_pattern = r"CHAR\((\d+)\)"
char_values = re.findall(char_pattern, content)

# Konversi nilai CHAR(x) menjadi byte
shellcode = bytes([int(value) for value in char_values])

# Simpan shellcode ke file biner
with open("shellcode.bin", "wb") as output:
    output.write(shellcode)

print("Shellcode berhasil diekstrak ke shellcode.bin")