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
    
    