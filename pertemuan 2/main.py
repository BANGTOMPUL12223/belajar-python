def isi_biodata():
    biodata = {}
    biodata['NIM'] = input("Masukkan NIM Anda: ")
    biodata['Nama'] = input("Masukkan Nama Anda: ")
    biodata['Kelas'] = input("Masukkan Kelas Anda: ")
    biodata['Prodi'] = input("Masukkan Program Studi Anda: ")
    return biodata

def cetak_biodata(biodata):
    print("\n=== BIODATA ===")
    for key, value in biodata.items():
        print(key + ":", value)

# Mengisi biodata
data = isi_biodata()

# Mencetak biodata
cetak_biodata(data)
