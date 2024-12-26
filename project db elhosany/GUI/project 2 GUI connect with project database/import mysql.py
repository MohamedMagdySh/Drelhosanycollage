import mysql.connector
import tkinter as tk
from tkinter import messagebox
from tkinter import ttk

def connect_to_db():
    return mysql.connector.connect(
        host="localhost",
        user="root",
        password="01023904417",
        database="elhosanydb"
    )


def add_student():
    student_id = student_id_entry.get()
    fname = fname_entry.get()
    mname = mname_entry.get()
    lname = lname_entry.get()
    data_birth = data_birth_entry.get()
    year_enrollment = year_enrollment_entry.get()
    address = address_entry.get()
    college_name = college_name_entry.get()
    prog_id = prog_id_entry.get()

    if student_id and fname and lname:  
        try:
            connection = connect_to_db()
            cursor = connection.cursor()
            query = ("INSERT INTO students (student_id, fname, mname, lname, data_birth, yearenrrow, address, collage_name, prog_id) "
                     "VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)")
            cursor.execute(query, (student_id, fname, mname, lname, data_birth, year_enrollment, address, college_name, prog_id))
            connection.commit()
            cursor.close()
            connection.close()

            messagebox.showinfo("Success", "Student added successfully!")
            show_students()  
        except mysql.connector.Error as err:
            messagebox.showerror("Error", f"Error: {err}")
    else:
        messagebox.showwarning("Input Error", "Please fill in all the mandatory fields.")

def show_students():
    try:
        connection = connect_to_db()
        cursor = connection.cursor()
        cursor.execute("SELECT * FROM students")
        rows = cursor.fetchall()

        for row in tree.get_children():
            tree.delete(row)

        for row in rows:
            tree.insert("", "end", values=row)

        cursor.close()
        connection.close()
    except mysql.connector.Error as err:
        messagebox.showerror("Error", f"Error: {err}")

##shape
root = tk.Tk()
root.title("Student Management")
root.geometry("800x600")  # Set window size
root.config(bg="#f0f0f0")  # Set background color

# Create the Notebook (tab control)
notebook = ttk.Notebook(root)
notebook.grid(row=0, column=0, sticky="nsew", padx=10, pady=10)

# Create a frame for the Add Student tab
add_student_frame = ttk.Frame(notebook)
notebook.add(add_student_frame, text="Add Student")

# Define a common style for labels and entries
label_style = {"font": ("Helvetica", 12), "background": "#f0f0f0", "anchor": "w"}
entry_style = {"font": ("Helvetica", 12), "width": 30}

# Create labels and entry widgets for student details (Add Student Tab)
tk.Label(add_student_frame, text="Student ID:", **label_style).grid(row=0, column=0, pady=5, sticky="w")
student_id_entry = tk.Entry(add_student_frame, **entry_style)
student_id_entry.grid(row=0, column=1, pady=5)

tk.Label(add_student_frame, text="First Name:", **label_style).grid(row=1, column=0, pady=5, sticky="w")
fname_entry = tk.Entry(add_student_frame, **entry_style)
fname_entry.grid(row=1, column=1, pady=5)

tk.Label(add_student_frame, text="Middle Name:", **label_style).grid(row=2, column=0, pady=5, sticky="w")
mname_entry = tk.Entry(add_student_frame, **entry_style)
mname_entry.grid(row=2, column=1, pady=5)

tk.Label(add_student_frame, text="Last Name:", **label_style).grid(row=3, column=0, pady=5, sticky="w")
lname_entry = tk.Entry(add_student_frame, **entry_style)
lname_entry.grid(row=3, column=1, pady=5)

tk.Label(add_student_frame, text="Date of Birth (YYYY-MM-DD):", **label_style).grid(row=4, column=0, pady=5, sticky="w")
data_birth_entry = tk.Entry(add_student_frame, **entry_style)
data_birth_entry.grid(row=4, column=1, pady=5)

tk.Label(add_student_frame, text="Year of Enrollment:", **label_style).grid(row=5, column=0, pady=5, sticky="w")
year_enrollment_entry = tk.Entry(add_student_frame, **entry_style)
year_enrollment_entry.grid(row=5, column=1, pady=5)

tk.Label(add_student_frame, text="Address:", **label_style).grid(row=6, column=0, pady=5, sticky="w")
address_entry = tk.Entry(add_student_frame, **entry_style)
address_entry.grid(row=6, column=1, pady=5)

tk.Label(add_student_frame, text="College Name:", **label_style).grid(row=7, column=0, pady=5, sticky="w")
college_name_entry = tk.Entry(add_student_frame, **entry_style)
college_name_entry.grid(row=7, column=1, pady=5)

tk.Label(add_student_frame, text="Program ID:", **label_style).grid(row=8, column=0, pady=5, sticky="w")
prog_id_entry = tk.Entry(add_student_frame, **entry_style)
prog_id_entry.grid(row=8, column=1, pady=5)

# Add button to submit the student information
add_button = tk.Button(add_student_frame, text="Add Student", command=add_student, font=("Helvetica", 14), bg="#4CAF50", fg="white", relief="raised", width=15)
add_button.grid(row=9, column=0, columnspan=2, pady=10)

# Create a frame for the Show Students tab
show_students_frame = ttk.Frame(notebook)
notebook.add(show_students_frame, text="Show Students")

# Style for the Treeview widget (students table)
style = ttk.Style()
style.configure("Treeview",
                font=("Helvetica", 12),
                rowheight=30,
                background="#f9f9f9",
                foreground="black")
style.configure("Treeview.Heading", font=("Helvetica", 14, "bold"), background="#4CAF50", foreground="white")
style.map("Treeview", background=[('selected', '#6ABF57')])

# Create a treeview to display students (Show Students Tab)
tree = ttk.Treeview(show_students_frame, columns=("Student ID", "First Name", "Middle Name", "Last Name", "DOB", "Enrollment Year", "Address", "College Name", "Program ID"), show="headings", height=15)
tree.grid(row=0, column=0, sticky="nsew", padx=10, pady=10)

# Define column headings
tree.heading("Student ID", text="Student ID")
tree.heading("First Name", text="First Name")
tree.heading("Middle Name", text="Middle Name")
tree.heading("Last Name", text="Last Name")
tree.heading("DOB", text="DOB")
tree.heading("Enrollment Year", text="Enrollment Year")
tree.heading("Address", text="Address")
tree.heading("College Name", text="College Name")
tree.heading("Program ID", text="Program ID")

# Show students when the program starts
show_students()

# Configure row and column weights for proper resizing
show_students_frame.grid_rowconfigure(0, weight=1)
show_students_frame.grid_columnconfigure(0, weight=1)

# Run the application
root.mainloop()
