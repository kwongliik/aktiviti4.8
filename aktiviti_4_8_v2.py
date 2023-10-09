jenis_kek = ['keju','mentega','pelangi','kopi']
harga_kek = [40, 35, 35, 30]
jumlah = [0,0,0,0]

def get_tempahan():
    a = int(input("Masukkan tempahan untuk kek keju: "))
    b = int(input("Masukkan tempahan untuk kek mentega: "))
    c = int(input("Masukkan tempahan untuk kek pelangi: "))
    d = int(input("Masukkan tempahan untuk kek kopi: "))
    tempahan = [a, b, c, d]
    return tempahan
    
def jumlah_harga(tempahan): # user-defined function
    for i in range(4): # struktur kawalan ulangan "for"
        jumlah[i] = harga_kek[i] * tempahan[i]
    return jumlah # keyword: return

def cetak():
    tempah = get_tempahan()
    jum = jumlah_harga(tempah)
    print("\n\nTempahan anda ialah: ")
    print(f"{tempah[0]} kek {jenis_kek[0]} : {jum[0]}")
    print(f"{tempah[1]} kek {jenis_kek[1]} : {jum[1]}")
    print(f"{tempah[2]} kek {jenis_kek[2]} : {jum[2]}")
    print(f"{tempah[3]} kek {jenis_kek[3]} : {jum[3]}")
    print(f"\nJumlah harga untuk tempahan ialah RM {sum(jum)}")

if __name__ == "__main__":
    cetak()
