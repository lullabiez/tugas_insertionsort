def insertion_sort(arr):
    """
    Fungsi untuk mengurutkan array menggunakan metode Insertion Sort.
    Menampilkan proses pemindahan di setiap iterasi.
    """
    print(f"\n Data Awal: {arr} \n" + "="*40)
    
    # Berjalan dari elemen kedua (indeks 1) hingga elemen terakhir
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        
        print(f"Iterasi ke-{i} (Memeriksa angka {key}):")
        
        # Geser elemen yang lebih besar dari key ke posisi setelahnya
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
            print(f"  -> Menggeser elemen: {arr}")
            
        # Tempatkan key pada posisi yang benar
        arr[j + 1] = key
        print(f"  -> Hasil iterasi ke-{i}: {arr}\n")
        
    return arr

def main():
    # TOP PAGE: Identitas Pembuat Aplikasi
    print("="*40)
    print("        APLIKASI INSERTION SORT        ")
    print("="*40)
    print(" Nama : ADI DARMANA")
    print(" NIM  : 310125023966")
    print("="*40)
    
    try:
        # Input data dari user
        input_user = input("Masukkan angka (pisahkan dengan koma, contoh: 5,2,9,1,5): ")
        # Mengubah string input menjadi list of integer
        data = [int(x.strip()) for x in input_user.split(",")]
        
        # Proses Sorting
        data_terurut = insertion_sort(data)
        
        print("="*40)
        print(f"Hasil Akhir (Terurut): {data_terurut}")
        print("===============================")
        
        # BOTTOM PAGE: Teori, Konsep, dan Cara Kerja
        print("\n" + "="*40)
        print("        EDUKASI INSERTION SORT        ")
        print("="*40)
        print("1. Pengertian:")
        print("   Insertion Sort adalah salah satu algoritma pengurutan data sederhana")
        print("   yang cara kerjanya mirip seperti menyusun kartu di tangan.")
        print("\n2. Konsep Dasar:")
        print("   Algoritma membagi array menjadi dua bagian: bagian yang sudah terurut")
        print("   (di sebelah kiri) dan bagian yang belum terurut (di sebelah kanan).")
        print("   Elemen diambil satu per satu dari bagian yang belum terurut untuk")
        print("   disisipkan ke posisi yang tepat pada bagian yang sudah terurut.")
        print("\n3. Cara Kerja:")
        print("   - Dimulai dari elemen ke-2 (indeks 1), simpan nilai ini sebagai 'key'.")
        print("   - Bandingkan 'key' dengan elemen-elemen di sebelah kirinya.")
        print("   - Jika elemen di kiri lebih besar dari 'key', geser elemen tersebut ke kanan.")
        print("   - Letakkan 'key' di tempat kosong setelah tidak ada lagi elemen di kiri yang lebih besar.")
        print("   - Ulangi langkah di atas untuk semua elemen berikutnya hingga selesai.")
        print("="*40)
        
    except ValueError:
        print("\nError: Pastikan input hanya berupa angka yang dipisahkan oleh koma!")

if __name__ == "__main__":
    main()