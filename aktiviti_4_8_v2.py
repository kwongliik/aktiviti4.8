jenis_kek = ['keju','mentega','pelangi','kopi']
harga_kek = [40, 35, 35, 30]
jumlah = [0,0,0,0]

..... get_tempahan():
    a = .....(input("Masukkan tempahan untuk kek keju: ")) #pengguna masukkan nombor integer untuk tempahan kek
    b = int(input("Masukkan tempahan untuk kek mentega: "))
    c = int(input("Masukkan tempahan untuk kek pelangi: "))
    d = int(input("Masukkan tempahan untuk kek kopi: ").....
    tempahan = [a, b, c, .....]
    return ............
    
def jumlah_harga(.........): # user-defined function ini menggunakan parameter "tempahan"
    for i in range(.....): # struktur kawalan ulangan "for" sebanyak 4 kali
        jumlah[i] = harga_kek[.....] * tempahan[.....]
    return ....... # memulangkan senarai "jumlah"

def cetak():
    tempah = get_tempahan()
    jum = ..................(tempah) # jum diumpukkan kepada function "jumlah_harga" dengan argumen "tempah"
    print("\n\nTempahan anda ialah: ")
    print(f"{tempah[.....]} kek {jenis_kek[0]} : {jum[0]}")
    print(f"{tempah[1]} kek {jenis_kek[.....]} : {jum[1]}")
    print(f"{tempah[2]} kek {jenis_kek[2]} : {jum[2]}")
    print(f"{tempah[3]} kek {jenis_kek[3]} : {jum[.....]}")
    print(f"\nJumlah harga untuk tempahan ialah RM {.....(jum)}")

#############################
# Jangan ubah kod di bawah!
#############################
if __name__ == "__main__":
    cetak()
