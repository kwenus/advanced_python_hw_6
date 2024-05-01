import unittest
from unittest import TestCase
from unittest_parametrize import parametrize
from unittest_parametrize import ParametrizedTestCase
from secretary import get_name, get_directory, all_directories, all_documents, add_docs


class TestSecretary(ParametrizedTestCase):
    # проверяем, что имя соответствует введенному номеру
    @parametrize(('expected_name', 'documents', 'doc_number'),
                 [("Геннадий Покемонов", all_documents, "11-2"),
                           ("Пабло Пикассо", all_documents, "48765-av"),
                           ("Казимир Малевич", all_documents, "54513")])
    def test_get_name_correct_output(self, expected_name, documents, doc_number):
        actual_name = get_name(documents, doc_number)
        self.assertEqual(actual_name, expected_name)

    # проверяем, что имя не цифра
    @parametrize(('documents', 'doc_number'),
        [(all_documents, "2207 876234"),
                  (all_documents, "54513")])
    def test_get_name_not_number(self, documents, doc_number):
        name = get_name(documents, doc_number)
        self.assertIsInstance(name, str)

    # проверяем, что имя не пустое
    @parametrize(('documents', 'doc_number'),
                 [(all_documents, "10006"),
                           (all_documents, "48765-av")])
    def test_get_name_not_empty(self, documents,  doc_number):
        name = get_name(documents, doc_number)
        self.assertIsNotNone(name)

    # проверяем, что возвращается правильный номер полки
    @parametrize(('expected_number', 'directories', 'doc_number'),
                 [('2', all_directories, "10006"),
                           ('5', all_directories, "48765-av")])
    def test_get_directory_shelf_number(self, expected_number, directories, doc_number):
        actual_number = get_directory(directories, doc_number)
        self.assertEqual(actual_number, expected_number)


    # проверяем, что документ попадает на указанную полку
    @parametrize(('expected_document_type', 'expected_number', 'expected_name', 'expected_shelf_number',
                           'documents', 'directories', 'document_type', 'number', 'name', 'shelf_number'),
                 [('passport', 'i-777-0-g', 'Robert Gore', '3', all_documents, all_directories,
                            'passport', 'i-777-0-g', 'Robert Gore', '3'),
                           ('driving license', '78 78 14 4', 'Савелий Волчий', '4', all_documents, all_directories,
                            'driving license', '78 78 14 4', 'Савелий Волчий', '4')])
    def test_add_correct(self, expected_document_type, expected_number, expected_name, expected_shelf_number,
                         documents, directories, document_type, number, name, shelf_number):
        add_docs(documents, directories, document_type, number, name, shelf_number)
        self.assertEqual(documents[-1].get('type'), expected_document_type)
        self.assertEqual(documents[-1].get('number'), expected_number)
        self.assertEqual(documents[-1].get('name'), expected_name)
        self.assertEqual(get_directory(directories, number), expected_shelf_number)