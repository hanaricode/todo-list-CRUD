import unittest
from io import StringIO
from unittest.mock import patch
 
# Ubah import sesuai dengan nama berkas fungsi lihat_tugas berasal
from script import lihat_tugas
 
 
class TestLihatTugas(unittest.TestCase):
 
    def test_lihat_tugas_kosong(self):
        tugas = []
        expected_output = "Tidak ada tugas yang tersedia.\n"
 
        with patch('sys.stdout', new_callable=StringIO) as stdout:
            lihat_tugas(tugas)
            actual_output = stdout.getvalue()
 
        self.assertEqual(actual_output, expected_output)
 
    def test_lihat_tugas_satu_item(self):
        tugas = [
            {
                "id": 1,
                "title": "Belajar Python Programming",
                "description": "Mempelajari fundamentals Python",
                "status": "Selesai",
                "estimasi_waktu_pengerjaan": 60,
            }
        ]
        expected_output = """Daftar Tugas:
- 1. Belajar Python Programming
  Deskripsi: Mempelajari fundamentals Python
  Status: Selesai
  Estimasi Waktu: 60 menit
--------------------
"""
 
        with patch('sys.stdout', new_callable=StringIO) as stdout:
            lihat_tugas(tugas)
            actual_output = stdout.getvalue()
 
        self.assertEqual(actual_output, expected_output)
 
    def test_lihat_tugas_banyak_item(self):
        tugas = [
            {
                "id": 1,
                "title": "Belajar Python Programming",
                "description": "Mempelajari fundamentals Python",
                "status": "Selesai",
                "estimasi_waktu_pengerjaan": 60,
            },
            {
                "id": 2,
                "title": "Belajar Machine Learning",
                "description": "Mempelajari fundamentals Machine Learning",
                "status": "Belum Selesai",
                "estimasi_waktu_pengerjaan": 120,
            },
        ]
        expected_output = """Daftar Tugas:
- 1. Belajar Python Programming
  Deskripsi: Mempelajari fundamentals Python
  Status: Selesai
  Estimasi Waktu: 60 menit
--------------------
- 2. Belajar Machine Learning
  Deskripsi: Mempelajari fundamentals Machine Learning
  Status: Belum Selesai
  Estimasi Waktu: 120 menit
--------------------
"""
 
        with patch('sys.stdout', new_callable=StringIO) as stdout:
            lihat_tugas(tugas)
            actual_output = stdout.getvalue()
 
        self.assertEqual(actual_output, expected_output)
 
 
if __name__ == "__main__":
    unittest.main()