# PROGRAM PROJEK APLIKASI PANATU MBG

import tkinter as tk
from tkinter import ttk, messagebox
import json
from pathlib import Path
from datetime import date

FILE_DATA = Path("data_mbg.json")

# DAFTAR JURUSAN
jurusan = {
    "TKJ": 2,
    "TKR": 4,
    "TITL": 3,
    "TPM": 4,
    "DPIB": 2,
    "Kimia": 2,
    "TKP": 2,
    "TAV": 2,
    "TOI": 2
}

tingkat_kelas = {
    "10": "X",
    "11": "XI",
    "12": "XII"
}

if FILE_DATA.exists():
    with open(FILE_DATA, "r", encoding="utf-8") as f:
        data = json.load(f)
        
else:
    data = []
    
# DAFTAR SEMUA KELAS
semua_kelas = []

for nomor, nama_tingkat in tingkat_kelas.items():
    for nama_jurusan, jumlah_kelas in jurusan.items():
        for nama_kelas in range(1, jumlah_kelas + 1):
            kelas = (
                nama_tingkat + " " + 
                nama_jurusan + " " + 
                str(nama_kelas)
            )
            semua_kelas.append(kelas)
            
# MENYIMPAN DATA KELAS
def simpan_data():
    with open(FILE_DATA, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=4, ensure_ascii=False)

#MEMILIH SESUAI KELAS
def pilih_kelas(event=None):
    nama_tingkat = tingkat_kelas[combo_tingkat.get()]
    daftar_kelas = []
    
    for nama_jurusan, jumlah in jurusan.items():
        for nomor in range(1, jumlah + 1):
            daftar_kelas.append(
                nama_tingkat + " " + 
                nama_jurusan + " " + 
                str(nomor)
            )
            
    combo_kelas['values'] = daftar_kelas
    combo_kelas.set("")

# CATATAN PENGAMBILAN
def tambah_data():  
    kelas = combo_kelas.get()
    nama = entry_nama.get() .strip()
    jumlah = entry_jumlah.get().strip()
    
    if not kelas or not nama or not jumlah:
        messagebox.showwarning(
            "Peringatan",
            "Semua kolom harus diisi!"
        )
        return
        
    try:
        jumlah = int(jumlah)
        
        if jumlah <= 0:
            raise ValueError
        
    except ValueError:
        messagebox.showwarning(
            "Peringatan",
            "Jumlah harus berupa angka positif!"
        )
        return
    
    catatan = {
        "kelas": kelas,
        "nama": nama,
        "jumlah": jumlah,
        "tanggal": date.today().isoformat()
    }   
    
    data.append(catatan)
    simpan_data()
    
    entry_nama.delete(0, tk.END)
    entry_jumlah.delete(0, tk.END)
    
    perbarui_tabel()
    
    messagebox.showinfo(
        "Berhasil",
        "Pengambilan MBG berhasil dicatat!"
    )
    
    