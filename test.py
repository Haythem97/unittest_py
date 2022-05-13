import unittest
import requests


class test(unittest.TestCase): 
     def test_connection(self):
        response = requests.get('http://localhost:5000/api/products')
        response.status_code
        self.assertEqual(response.status_code, 200 )

     def test_delete_data(self):
         response = requests.delete('http://127.0.0.1:5000/api/products/1')
         self.assertEqual(response.status_code, 200)
    
     def test_update(self):
         response = requests.put('http://127.0.0.1:5000/api/products/155')
         self.assertEqual(response.status_code, 500)

     def test_create(self):
         response = requests.post('http://127.0.0.1:5000/api/create_product')
         self.assertEqual(response.status_code, 201)
         
if __name__ == '__main__':
    unittest.main() 
