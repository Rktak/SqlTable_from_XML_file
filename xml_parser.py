import xml_parser as xp
import xml.etree.ElementTree as ET

import sqlite3

def parse_xml_file(xml_file):

    tree = ET.parse(xml_file)
    root = tree.getroot()

    data_list = []
    #data frame

    # Iterate through elements in the XML file
    for item in root.findall('student'):
        data_dict = {}
        data_dict['name'] = item.find('name').text
        data_dict['age'] = item.find('age').text
        data_dict['grade'] = item.find('grade').text

        data_list.append(data_dict)

    return data_list


def save_to_sqlite(parsed_data, database_path):
    # Connect to the SQLite database
    conn = sqlite3.connect(database_path)
    cursor = conn.cursor()


    cursor.execute('''
        CREATE TABLE IF NOT EXISTS students (
            id INTEGER PRIMARY KEY,
            name TEXT,
            age INTEGER,
            grade TEXT
        )
    ''')


    for data_dict in parsed_data:
        cursor.execute('''
            INSERT INTO students (name, age, grade) VALUES (?, ?, ?)
        ''', (data_dict['name'], int(data_dict['age']), data_dict['grade']))


    conn.commit()
    conn.close()


# function to parse the data

xml_file_path = "./students.xml"
parsed_data = parse_xml_file(xml_file_path)




# function call to create database

database_path = "students.db"
save_to_sqlite(parsed_data, database_path)



