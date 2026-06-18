"""Jawaban w12 — STUB (MAHASISWA)

Aturan pengisian:
- Implementasikan fungsi q01()..q12() sesuai soal di weeks/w12/quiz.qmd
- Jangan ubah nama fungsi.

Format jawaban:
- T/F    -> bool  (True=Benar, False=Salah)
- MC     -> str   ("A"/"B"/"C"/"D")
- Numeric-> int/float (desimal pakai '.')
"""
from __future__ import annotations
def q01() -> bool:
    """[T/F] Hipotesis nol (H0) biasanya merupakan pernyataan yang ingin kita buktikan
kebenarannya."""
    return False

def q02() -> bool:
    """[T/F] Kesalahan Tipe I terjadi ketika kita menolak H0 padahal H0 benar."""
    return True

def q03() -> bool:
    """[T/F] P-value adalah probabilitas mendapatkan hasil sampel yang ekstrim jika H0
benar."""
    return True

def q04() -> str:
    """[MC] Jika p-value < (tingkat signifikansi), maka keputusan kita adalah:

A) Gagal menolak H0.
B) Menolak H0.
C) Menolak H1.
D) Menambah sampel."""
    return 'B'

def q05() -> str:
    """[MC] Pada uji satu arah (one-tailed) dengan H1 : > 0, daerah penolakan berada di:

A) Ekor kiri.
B) Kedua ekor.
C) Ekor kanan.
D) Tengah distribusi."""
    return 'C'

def q06() -> str:
    """[MC] Tingkat signifikansi yang umum digunakan adalah:

A) 0,05
B) 0,50
C) 0,95
D) 1,00"""
    return 'A'

def q07() -> str:
    """[MC] Kesalahan Tipe II terjadi jika:

A) Menolak H0 yang benar.
B) Gagal menolak H0 yang salah.
C) Menolak H1 yang benar.
D) P-value terlalu kecil."""
    return 'B'

def q08() -> float:
    """[Numeric] Jika = 0,05 dan p-value = 0,03, berikan angka 1 jika kita menolak H0, dan
0 jika tidak."""
    return 1.0

def q09() -> float:
    """[Numeric] Berapakah probabilitas Kesalahan Tipe I jika kita menggunakan = 0,01?"""
    return 0.01

def q10() -> float:
    """[Numeric] Dalam uji Z, jika statistik uji Z = 2,33 dan Z kritis = 1,96, berikan angka 9
untuk "Tolak H0" dan 0 untuk "Gagal Tolak H0"."""
    return 9.0

def q11() -> float:
    """[Numeric] Jika H0 : = 100 dan H1 : 100, berapa banyak ekor (tails) dalam uji
ini?"""
    return 1.0

def q12() -> float:
    """[Numeric] Jika p-value = 0,12 dan = 0,05, berikan angka 1 jika kita menolak H0,
dan 0 jika tidak."""
    return 1.0
