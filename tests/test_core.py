import unittest
from unittest.mock import Mock, MagicMock
from src.data_cleanup_automation.core import cleanup_stale_data, Config

class TestCleanupStaleData(unittest.TestCase):
    def setUp(self):
        self.db_conn = Mock()
        self.config = Config()

    def test_cleanup_stale_data_deletes_old_records(self):
        # Mock cursor and its methods
        cursor = MagicMock()
        self.db_conn.cursor.return_value.__enter__.return_value = cursor
        
        # Define behavior for cursor.execute
        cursor.execute.side_effect = None
        
        # Call the function
        cleanup_stale_data(self.db_conn, self.config)
        
        # Assert that execute was called with expected parameters
        self.assertTrue(cursor.execute.called)
        
    def test_cleanup_stale_data_handles_errors(self):
        # Simulate an error during execute
        cursor = MagicMock()
        self.db_conn.cursor.return_value.__enter__.return_value = cursor
        cursor.execute.side_effect = Exception('Database error')

        # Call the function and check for logging of the error
        with self.assertLogs('src.data_cleanup_automation.core', level='ERROR') as cm:
            cleanup_stale_data(self.db_conn, self.config)
            self.assertIn('Error during cleanup:', cm.output[0])
            
    def test_configurable_threshold(self):
        self.config.threshold_days = 15
        cleanup_stale_data(self.db_conn, self.config)
        # Check the behavior based on new threshold

    def test_no_records_deleted_if_none_stale(self):
        cursor = MagicMock()
        self.db_conn.cursor.return_value.__enter__.return_value = cursor
        cursor.execute.side_effect = None
        
        cleanup_stale_data(self.db_conn, self.config)
        self.assertEqual(cursor.execute.call_count, 0)

    def test_successful_cleanup_logs_correctly(self):
        cursor = MagicMock()
        self.db_conn.cursor.return_value.__enter__.return_value = cursor
        cursor.execute.side_effect = None
        
        with self.assertLogs('src.data_cleanup_automation.core', level='INFO') as cm:
            cleanup_stale_data(self.db_conn, self.config)
            self.assertIn('Cleanup complete.', cm.output[0])

if __name__ == '__main__':
    unittest.main()