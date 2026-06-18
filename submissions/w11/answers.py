"""Jawaban w11 — STUB (MAHASISWA)

Aturan pengisian:
- Implementasikan fungsi q01()..q12() sesuai soal di weeks/w11/quiz.qmd
- Jangan ubah nama fungsi.

Format jawaban:
- T/F    -> bool  (True=Benar, False=Salah)
- MC     -> str   ("A"/"B"/"C"/"D")
- Numeric-> int/float (desimal pakai '.')
"""
from __future__ import annotations
def q01() -> bool:
    """[T/F] Interval kepercayaan memberikan rentang nilai yang mungkin mengandung
parameter populasi dengan tingkat keyakinan tertentu."""
    return True

def q02() -> bool:
    """[T/F] Semakin tinggi tingkat kepercayaan (misal dari 95% ke 99%), maka lebar interval
kepercayaan akan semakin sempit."""
    return False

def q03() -> bool:
    """[T/F] Margin of Error dipengaruhi oleh ukuran sampel dan variabilitas data."""
    return True

def q04() -> str:
    """[MC] Nilai kritis Z untuk tingkat kepercayaan 95% adalah sekitar:

A) 1,645
B) 1,96
C) 2,576
D) 1,00"""
    return 'B'

def q05() -> str:
    """[MC] Jika kita ingin memperkecil interval kepercayaan tanpa mengubah tingkat
kepercayaan, kita harus:

A) Memperkecil ukuran sampel.
B) Memperbesar ukuran sampel.
C) Mengabaikan data outlier.
D) Menggunakan distribusi t."""
    return 'B'

def q06() -> str:
    """[MC] Interval kepercayaan 90% untuk rata-rata dihitung menggunakan rumus:

A) X Z / n
B) X t / n
C) X Z / n
D) X + Z """
    return 'C'

def q07() -> str:
    """[MC] Estimasi titik terbaik untuk rata-rata populasi adalah:

A) Median sampel.
B) Modus sampel.
C) Rata-rata sampel (X ).
D) Rentang sampel."""
    return 'C'

def q08() -> float:
    """[Numeric] Jika rata-rata sampel adalah 100 dan Margin of Error adalah 5, berapakah
batas bawah interval kepercayaan tersebut?"""
    return 95.0

def q09() -> float:
    """[Numeric] Hitung lebar interval jika batas bawah 10 dan batas atas 12."""
    return 1.0

def q10() -> float:
    """[Numeric] Jika n = 100 dan simpangan baku 20, berapakah nilai ( / n)?"""
    return 24.0

def q11() -> float:
    """[Numeric] Berapakah nilai tengah (point estimate) jika interval kepercayaan adalah
[40, 60]?"""
    return 50.0

def q12() -> float:
    """[Numeric] Jika Margin of Error adalah 2, berapa lebar total interval kepercayaan
tersebut?"""
    return 1.0
