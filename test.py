import unittest
import requests


class test(unittest.Test): 
     def test_connection(self):
        response = requests.get('http://localhost:5000/api/products')
        if response.status_code == 200:
            print("Le test est passé")
        else:
            print("Le test n'est pas passé")

     def test_delete(self):
         response = requests.delete('http://127.0.0.1:5000/api/products/1')
         if response.status_code == 500:
                print("Le test est passé")
         else:
            print("Le test n'est pas passé")
    
     def test_update(self):
         response = requests.put('http://127.0.0.1:5000/api/products/155')
         if response.status_code == 500:
            print("Le test est passé")
         else:
            print("Le test n'est pas passé")

     def test_create(self):
         response = requests.post('http://127.0.0.1:5000/api/create_product')
         if response.status_code == 201:
                print("Le test est passé")
         else:
            print("Le test n'est pas passé")
         
if __name__ == '__main__':
    unittest.main() 
