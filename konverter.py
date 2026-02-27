import kurs

def hitung_konversi(mata_uang_asal, mata_uang_tujuan, jumlah):
    """
    Fungsi untuk mengkonversi mata uang.
    Konsep: Ubah ke IDR terlebih dahulu, baru ubah ke mata uang tujuan.
    """
    rates = kurs.EXCHANGE_RATES.copy()
    rates["IDR"] = 1
    
    if mata_uang_asal not in rates or mata_uang_tujuan not in rates:
        return None
    
    jumlah_dalam_idr = jumlah * rates[mata_uang_asal]
    
    hasil_konversi = jumlah_dalam_idr / rates[mata_uang_tujuan]
    
    return hasil_konversi