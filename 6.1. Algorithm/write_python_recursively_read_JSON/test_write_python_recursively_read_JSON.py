from write_python_recursively_read_JSON import read_json_recursively
import unittest

class TestJsonReader(unittest.TestCase):

    def setUp(self):
        # Contoh data JSON
        self.data = {
            "name": "John",
            "age": 30,
            "children": [
                {
                    "name": "Anna",
                    "age": 10
                },
                {
                    "name": "Ben",
                    "age": 8
                }
            ],
            "address": {
                "city": "New York",
                "zip": "10001"
            }
        }

    def test_read_json(self):
        # Hasil yang diharapkan berdasarkan input JSON di atas
        expected_output = [
            "Key: name, Value: John",
            "Value: John",
            "Key: age, Value: 30",
            "Value: 30",
            "Key: children, Value: [{'name': 'Anna', 'age': 10}, {'name': 'Ben', 'age': 8}]",
            "Key: name, Value: Anna",
            "Value: Anna",
            "Key: age, Value: 10",
            "Value: 10",
            "Key: name, Value: Ben",
            "Value: Ben",
            "Key: age, Value: 8",
            "Value: 8",
            "Key: address, Value: {'city': 'New York', 'zip': '10001'}",
            "Key: city, Value: New York",
            "Value: New York",
            "Key: zip, Value: 10001",
            "Value: 10001"
        ]

        # Panggil fungsi buat baca JSON secara rekursif
        result = read_json_recursively(self.data)
        self.assertEqual(result, expected_output)

if __name__ == "__main__":
    unittest.main()