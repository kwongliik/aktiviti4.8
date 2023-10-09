from aktiviti_4_8_v2 import *
from tud_test_base import *
import pytest

harga = [40, 35, 35, 30]

def test_get_tempahan_():    
    set_keyboard_input([2,3,4,5])
    get_tempahan()
    output = get_display_output()

    assert output == [
        "Masukkan tempahan untuk kek keju: ",
        "Masukkan tempahan untuk kek mentega: ",
        "Masukkan tempahan untuk kek pelangi: ",
        "Masukkan tempahan untuk kek kopi: ",
    ]

@pytest.mark.parametrize("tempahan, jumlah", [([2,3,4,5],[80,105,140,150])])
def test_jumlah_harga(tempahan, jumlah): 
    jum = jumlah_harga(tempahan)
    assert jum == jumlah

def test_cetak(): 
    set_keyboard_input([2,3,4,5])
    cetak()
    output = get_display_output()
    assert output == [
        "Masukkan tempahan untuk kek keju: ",
        "Masukkan tempahan untuk kek mentega: ",
        "Masukkan tempahan untuk kek pelangi: ",
        "Masukkan tempahan untuk kek kopi: ",
        "\n\nTempahan anda ialah: ",
        "2 kek keju : 80",
        "3 kek mentega : 105",
        "4 kek pelangi : 140",
        "5 kek kopi : 150",
        "\nJumlah harga untuk tempahan ialah RM 475"
    ]
