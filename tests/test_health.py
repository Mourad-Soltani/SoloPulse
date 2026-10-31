# Tests for SoloPulse
# Author: Mourad.Soltani
# Signature: Mourad.Soltani

import unittest
from unittest.mock import patch, MagicMock
import json
from solopulse import HealthChecker, generate_status_html

class TestHealthChecker(unittest.TestCase):
    def setUp(self):
        self.checker = HealthChecker(timeout=1)
    
    @patch('urllib.request.urlopen')
    def test_check_url_up(self, mock_urlopen):
        mock_response = MagicMock()
        mock_response.getcode.return_value = 200
        mock_urlopen.return_value.__enter__.return_value = mock_response
        
        result = self.checker.check_url("https://example.com")
        self.assertEqual(result['status'], 'up')
        self.assertEqual(result['code'], 200)
        self.assertIn('latency_ms', result)
    
    @patch('urllib.request.urlopen')
    def test_check_url_down(self, mock_urlopen):
        mock_urlopen.side_effect = Exception("Connection failed")
        
        result = self.checker.check_url("https://down.example.com")
        self.assertEqual(result['status'], 'down')
        self.assertEqual(result['code'], 0)
        self.assertIn('error', result)
    
    def test_generate_html(self):
        results = [
            {'name': 'API', 'status': 'up', 'code': 200, 'latency_ms': 45.2, 'checked_at': '2026-01-01T00:00:00Z', 'url': 'https://api.example.com'},
            {'name': 'Web', 'status': 'down', 'code': 0, 'latency_ms': 5000, 'checked_at': '2026-01-01T00:00:00Z', 'url': 'https://web.example.com'}
        ]
        html = generate_status_html(results, "Test Status")
        self.assertIn("Test Status", html)
        self.assertIn("API", html)
        self.assertIn("UP", html)
        self.assertIn("DOWN", html)
        self.assertIn("Mourad.Soltani", html)
        self.assertIn("1/2 Operational", html)

if __name__ == "__main__":
    unittest.main()
