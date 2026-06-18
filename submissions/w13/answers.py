"""Jawaban w13 — STUB (MAHASISWA)

Aturan pengisian:
- Implementasikan fungsi q01()..q12() sesuai soal di weeks/w13/quiz.qmd
- Jangan ubah nama fungsi.

Format jawaban:
- T/F    -> bool  (True=Benar, False=Salah)
- MC     -> str   ("A"/"B"/"C"/"D")
- Numeric-> int/float (desimal pakai '.')
"""
from __future__ import annotations
def q01() -> bool:
    """[T/F] Dalam regresi linear sederhana, hanya ada satu variabel independen X untuk
memprediksi variabel dependen Y."""
    return False

def q02() -> bool:
    """[T/F] Koefisien determinasi (R2) menunjukkan proporsi variansi Y yang dijelaskan oleh
model."""
    return True

def q03() -> bool:
    """[T/F] Metode Least Squares bertujuan meminimalkan jumlah kuadrat residu (error)."""
    return True

def q04() -> str:
    """[MC] Jika model regresi adalah Y = 5 + 2X, maka 5 adalah:

A) Slope (kemiringan).
B) Intercept (titik potong).
C) Residu.
D) Korelasi."""
    return 'B'

def q05() -> str:
    """[MC] Nilai R2 yang menunjukkan model sangat fit dengan data adalah mendekati:

A) 0
B) 1
C) -1
D) 0,5"""
    return 'B'

def q06() -> str:
    """[MC] Garis regresi terbaik adalah yang memiliki:

A) Residu terbesar.
B) Intercept nol.
C) Jumlah kuadrat error terkecil.
D) Slope negatif."""
    return 'C'

def q07() -> str:
    """[MC] Jika slope (b1) bernilai positif, maka:

A) Jika X naik, Y turun.
B) Jika X naik, Y naik.
C) X dan Y tidak berhubungan.
D) Y selalu konstan."""
    return 'B'

def q08() -> float:
    """[Numeric] Menggunakan model Y = 10 + 3X, berapakah prediksi nilai Y jika X = 5?"""
    return 25.0

def q09() -> float:
    """[Numeric] Jika total variansi adalah 100 dan variansi yang tidak dijelaskan (error) adalah
20, berapakah nilai R2?"""
    return 0.8

def q10() -> float:
    """[Numeric] Berapakah nilai residu jika nilai observasi Y = 15 dan nilai prediksi Y = 12?"""
    return 0.0

def q11() -> float:
    """[Numeric] Dalam Y = a + bX, jika a = 2, b = 0,5 dan X = 6, hitung Y."""
    return 5.0

def q12() -> float:
    """[Numeric] Jika R2 = 0,64, berapakah nilai koefisien korelasi r (asumsikan slope positif)?"""
    return 4.0
