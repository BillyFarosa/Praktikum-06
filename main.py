from view.view_nilai import cari,cetak,awal,lanjutan
from view.input_nilai import masukan,cari,hapus,ubah
awal()
while True:

    c = input("\nPilih Opsi: ")

    if c.lower() == 'k':
        print("CREATE BY : BILLY FAROSA")
        break

    elif c.lower() == 'l':
        cetak()

    elif c.lower() == 't':
        masukan()

    elif c.lower() == 'e':
        ubah()

    elif c.lower() == 'c':
        cari()

    elif c.lower() == 'h':
        hapus()

    else:
        lanjutan()