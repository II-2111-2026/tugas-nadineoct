"""Jawaban w14 — STUB (MAHASISWA)

Aturan pengisian:
- Implementasikan fungsi q01()..q12() sesuai soal di weeks/w14/quiz.qmd
- Jangan ubah nama fungsi.

Format jawaban:
- T/F    -> bool  (True=Benar, False=Salah)
- MC     -> str   ("A"/"B"/"C"/"D")
- Numeric-> int/float (desimal pakai '.')
"""
from __future__ import annotations
def q01() -> bool:
    """[T/F] Uji Chi-Square dapat digunakan untuk menguji independensi antara dua variabel
kategorikal."""
    return True

def q02() -> bool:
    """[T/F] ANOVA digunakan untuk membandingkan rata-rata dari tiga kelompok atau lebih."""
    return True

def q03() -> bool:
    """[T/F] Jika nilai F hitung dalam ANOVA lebih kecil dari F kritis, kita menolak H0."""
    return False

def q04() -> str:
    """[MC] Dalam uji Chi-Square, frekuensi yang diharapkan (Expected) dihitung dengan
asumsi:

A) Ada hubungan kuat.
B) Variabel-variabel independen (H0 benar).
C) Sampel sangat besar.
D) Data berdistribusi Normal."""
    return 'B'

def q05() -> str:
    """[MC] Manakah yang merupakan salah satu asumsi ANOVA?

A) Data kategorikal.
B) Homogenitas variansi (variansi antar kelompok sama).
C) Ukuran sampel harus 10.
D) Slope harus positif."""
    return 'B'

def q06() -> str:
    """[MC] Statistik uji untuk ANOVA adalah:

A) t
B) F
C) Z
D) Chi-Square"""
    return 'B'

def q07() -> str:
    """[MC] Derajat bebas (df) untuk uji Chi-Square tabel r x c adalah:

A) (r-1)(c-1)
B) r + c
C) n - 1
D) r x c"""
    return 'A'

def q08() -> float:
    """[Numeric] Jika total SS (Sum of Squares) = 100 dan SS Between = 80, berapakah nilai
R2 dalam konteks ANOVA (eta-squared)?"""
    return 0.8

def q09() -> float:
    """[Numeric] Dalam uji Chi-Square, jika Observed = 100 dan Expected = 95, berapakah
nilai (O-E)?"""
    return 950.0

def q10() -> float:
    """[Numeric] Jika p-value dari uji ANOVA adalah 0,001 dan = 0,05, berikan angka 0,8
jika kita menolak H0 dan 0 jika tidak."""
    return 0.8

def q11() -> float:
    """[Numeric] Berapa banyak kelompok yang dibandingkan jika df Between dalam ANOVA
adalah 2?"""
    return 2.0

def q12() -> float:
    """[Numeric] Jika df numerator = 3 dan df denominator = 20, berikan angka 1 jika ini
adalah uji F, dan 0 jika bukan."""
    return 1.0
