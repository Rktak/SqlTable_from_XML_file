
import tkinter as tk
from tkinter import ttk
import sqlite3

def show_data():
    # Connect to SQLite database
    conn = sqlite3.connect('students.db')
    file = conn.cursor()

    file.execute('SELECT name,age,grade FROM students')
    data = file.fetchall()

    conn.close()

    # Display the data in a Tkinter window with a table (Treeview)
    display_window = tk.Tk()
    display_window.title("Student Data")

    # Create a Treeview widget
    tree = ttk.Treeview(display_window, columns=('Name', 'Age', 'Grade'), show='headings')
    tree.heading('Name', text='Name')
    tree.heading('Age', text='Age')
    tree.heading('Grade', text='Grade')

    # Insert data into the Treeview
    for row in data:
        tree.insert('', 'end', values=row)


    tree.pack()

    display_window.mainloop()

# Example usage
show_data()


