from django.test import TestCase
from django.db import connections

class DatabaseConnectionTestCase(TestCase):
    def test_database_connection(self):
        """
        Veritabanına bağlanabilirliği test eder.
        """
        db_conn = connections['default']
        try:
            db_conn.ensure_connection()
            self.assertTrue(db_conn.is_usable())
        except Exception as e:
            self.fail(f"Veritabanı bağlantı testi başarısız oldu: {e}")

    def test_database_query(self):
        """
        Basit bir sorgu çalıştırarak veritabanını test eder.
        """
        with connections['default'].cursor() as cursor:
            cursor.execute("SELECT 1;")
            result = cursor.fetchone()
            self.assertEqual(result[0], 1)
