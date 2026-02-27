from tabulate import tabulate
import kurs
import konverter

def tampilkan_tabel_kurs():
    print("--- KONVERTER MATA UANG ---")
    tabel_data = []
    
    for kode, nilai in kurs.EXCHANGE_RATES.items():

        nilai_format = f"{nilai:,.0f}".replace(',', '.')
        tabel_data.append([kode, nilai_format])
        
    print(tabulate(tabel_data, headers=["kode", "kurs"], tablefmt="grid"))

def format_rupiah(angka):
    return f"Rp {angka:,.0f}".replace(',', '.')

def main():
    tampilkan_tabel_kurs()
    
    pilihan_tersedia = ["IDR"] + list(kurs.EXCHANGE_RATES.keys())
    teks_pilihan = "/".join(pilihan_tersedia)
    
    dari = input(f"dari ({teks_pilihan}): ").upper()
    ke = input(f"Ke ({teks_pilihan}): ").upper()
    
    try:
        jumlah = float(input("jumlah: "))
    except ValueError:
        print("wrror: masukkan jumlah dalam bentuk angka!")
        return
        
    hasil = konverter.hitung_konversi(dari, ke, jumlah)
    
    if hasil is not None:

        if dari == "IDR":
            str_asal = format_rupiah(jumlah)
        else:
            str_asal = f"{jumlah:g} {dari}"
            
        if ke == "IDR":
            str_hasil = format_rupiah(hasil)
        else:
            str_hasil = f"{hasil:.2f} {ke}"
        print(f"{str_asal} = {str_hasil}")
    else:
        print("error: kode mata uang tidak valid. silakan cek kembali input anda.")

if __name__ == "__main__":
    main()