from tabnanny import check
from urllib import response


try:
    from main import app
    import unittest
except Exception as e: 
    print('Modulos faltantes {}'.format(e))

class FleskTest(unittest.TestCase):
    
    #checar get lista de libros
    def test__get_list(self):
        tester = app.test_client(self)
        response = tester.get('/books/list')
        statcode = response.status_code
        self.assertEqual(statcode,200)
    
    ######################################################################################

    #checar get book sin parametros
    def test__get_without_parameters(self):
        tester = app.test_client(self)
        response = tester.get('/books')
        statcode = response.status_code
        self.assertEqual(statcode,200)

    #checar get book con parametros
    def test__get_with_parameters(self):
        tester = app.test_client(self)
        response = tester.get('/books?name=prueba 8')
        statcode = response.status_code
        self.assertEqual(statcode,200)
    
    ######################################################################################

    #Checar post book sin parametros
    def test__post_without_parameters(self):
        tester = app.test_client(self)
        response = tester.post('/books')
        statcode = response.status_code
        self.assertEqual(statcode,200)
    
    #Checar post book sin parametros
    def test__post_without_parameters(self):
        tester = app.test_client(self)
        response = tester.post('/books')
        statcode = response.status_code
        self.assertEqual(statcode,200)
    
    #Checar post book con parametros incorrectos
    def test__post_with_wrong_parameters(self):
        tester = app.test_client(self)
        response = tester.post('/books?name=prueba N&date=28-21-2222')
        statcode = response.status_code
        self.assertEqual(statcode,200)

    #Checar post book con parametros correctos
    def test__post_with_rigth_parameters(self):
        tester = app.test_client(self)
        response = tester.post('/books?name=prueba N&date=28-04-2022')
        statcode = response.status_code
        self.assertEqual(statcode,200)

    ######################################################################################

    #Checar put book sin parametros
    def test__post_without_parameters(self):
        tester = app.test_client(self)
        response = tester.put('/books')
        statcode = response.status_code
        self.assertEqual(statcode,200)
    
    #Checar post book sin parametros
    def test__post_without_parameters(self):
        tester = app.test_client(self)
        response = tester.put('/books')
        statcode = response.status_code
        self.assertEqual(statcode,200)
    
    #Checar put book con parametros incorrectos
    def test__post_with_wrong_parameters(self):
        tester = app.test_client(self)
        response = tester.put('/books?name=prueba 8&date=28-21-2222')
        statcode = response.status_code
        self.assertEqual(statcode,200)

    #Checar put book con parametros correctos
    def test__post_with_rigth_parameters(self):
        tester = app.test_client(self)
        response = tester.put('/books?name=prueba 8&date=28-04-2022')
        statcode = response.status_code
        self.assertEqual(statcode,200)

    ###########################################################################


    #checar delete book sin parametros
    def test__get_without_parameters(self):
        tester = app.test_client(self)
        response = tester.delete('/books')
        statcode = response.status_code
        self.assertEqual(statcode,200)

    #checar get book con parametros
    def test__get_with_parameters(self):
        tester = app.test_client(self)
        response = tester.delete('/books?name=prueba N')
        statcode = response.status_code
        self.assertEqual(statcode,200)    

if __name__ == '__main__':
    unittest.main()