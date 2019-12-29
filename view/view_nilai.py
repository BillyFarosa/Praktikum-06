from model.daftar_nilai import data

def awal():
    print("|==========================================================================|")
    print("|                     PROGRAM INPUT DATA MAHASISWA                         |")
    print("|==========================================================================|")
    print("T)ambah, E)dit, H)apus, C)ari, L)ist, K)eluar:")


def lanjutan():
    print("T)ambah, E)dit, H)apus, C)ari, L)ist, K)eluar:")


def cetak():
    print("\-------------------------DATA NILAI AKHIR MAHASISWA----------------------------------/")
    print("****************************************************************************************")
    print()
    print()
    print("========================================================================================")
    print(" |  No |   Nama   |     NIM     |  Tugas |   UTS  |   UAS  |  NILAI |")
    print("========================================================================================")
    i = 0
    for x in data.items():
        i += 1
        print(" |  {7:2} | {0:7s}  | {2:11} | {3:6d} | {4:6d} | {5:6d} | {6:6.2f} |" \
              .format(x[0], x[1][0], x[1][1], x[1][2], x[1][3], x[1][4], x[1][5], i))
    print("|=========================================================================|")
    print("T)ambah, E)dit, H)apus, C)ari, L)ist, K)eluar:")


def cari():
    from view.input_nilai import cari
    cari()
    print("T)ambah, E)dit, H)apus, C)ari, L)ist, K)eluar:")