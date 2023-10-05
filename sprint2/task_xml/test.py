import xml.etree.ElementTree as ET
import unittest
from script import find_passwords_in_xml_tree


class ParserTest(unittest.TestCase):
    def test_no_password_attribute(self):
        tree = ET.parse('examples/no_password_attr.xml')
        actual = find_passwords_in_xml_tree(tree)
        self.assertEqual(len(actual), 0)

    def test_no_password_elem(self):
        tree = ET.parse('examples/no_password_elem.xml')
        actual = find_passwords_in_xml_tree(tree)
        self.assertEqual(len(actual), 0)
    
    def test_password_attr_exists(self):
        tree = ET.parse('examples/has_password_attr.xml')
        actual = find_passwords_in_xml_tree(tree)
        self.assertIn('somepassword', actual)

    def test_password_elem_exists_nested(self):
        tree = ET.parse('examples/nested_password_elem.xml')
        actual = find_passwords_in_xml_tree(tree)
        self.assertIn('somepassword', actual)

    def test_multiply_passwords(self):
        tree = ET.parse('examples/multiply_passwords.xml')
        actual = find_passwords_in_xml_tree(tree)
        self.assertEqual(len(actual), 2)
        self.assertIn('somepassword1', actual)
        self.assertIn('somepassword2', actual)


if __name__ == '__main__':
    unittest.main()