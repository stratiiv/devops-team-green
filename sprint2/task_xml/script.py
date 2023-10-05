import os
from pathlib import Path
import xml.etree.ElementTree as ET
from argparse import ArgumentParser


def find_passwords_in_xml_tree(tree):
    """
    Find and collect passwords within an XML ElementTree.
    """
    passwords = []
    for elem in tree.iter():
        if elem.tag == 'password':
            passwords.append(elem.text)
        if 'password' in elem.attrib:
            passwords.append(elem.attrib['password'])
    return passwords


def main():
    parser = ArgumentParser(description='Check if xml file contains '
                            'password element or attribute')
    parser.add_argument('path', help='XML file to search in')
    args = parser.parse_args()
    filename = args.path

    if not os.path.exists(filename):
        print(f"Error! No such file {filename}")
        return
    if not Path(filename).suffix == '.xml':
        print(f"Error! {filename} is not a xml file")
        return

    xml_tree = ET.parse(filename)
    passwords = find_passwords_in_xml_tree(xml_tree)

    if not passwords:
        print(f"No passwords found in {filename}")
    else:
        for password in passwords:
            print(password)


if __name__ == '__main__':
    main()