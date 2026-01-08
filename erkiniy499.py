import tkinter as tk
from tkinter import messagebox
import matplotlib.pyplot as plt

# Global file name
MY_FILE = "students.txt"

# Function to get students from the text file
def get_data():
    my_students = []
    try:
        f = open(MY_FILE, "r")
        for line in f:
            # removing spaces and splitting by comma
            info = line.strip().split(",")
            if len(info) == 2:
                name = info[0]
                score = int(info[1])
                my_students.append({"name": name, "score": score})
        f.close()
    except:
        # If file is not there, just return empty
        return []
    return my_students

# Function to save our list back to the file
def save_to_file(the_list):
    f = open(MY_FILE, "w")
    for s in the_list:
        f.write(s['name'] + "," + str(s['score']) + "\n")
    f.close()

# Sorting Algorithm: Bubble Sort
# I used the logic from our lecture slides here and watched additional yotube videos (in general for this code).
def my_bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n - i - 1):
            # Sort from high to low score
            if arr[j]['score'] < arr[j+1]['score']:
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return arr

# Function for adding a student
def add_new():
    s_name = name_in.get()
    s_score = score_in.get()
    
    # Validation with try-except
    try:
        s_score = int(s_score)
        if s_score >= 0 and s_score <= 100:
            all_data = get_data()
            all_data.append({"name": s_name, "score": s_score})
            save_to_file(all_data)
            
            messagebox.showinfo("Done", "Added successfully!")
            name_in.delete(0, tk.END)
            score_in.delete(0, tk.END)
            show_list_in_ui()
        else:
            messagebox.showwarning("Wait", "Score must be 0 to 100!")
    except:
        messagebox.showerror("Error", "Please enter a number for the score!")

# Searching function
def search_now():
    find_this = search_in.get().lower()
    all_data = get_data()
    
    # Clear the listbox first
    listbox.delete(0, tk.END)
    
    for s in all_data:
        if find_this in s['name'].lower():
            listbox.insert(tk.END, s['name'] + " - Grade: " + str(s['score']))

# Showing the graph
def draw_graph():
    data = get_data()
    if len(data) == 0:
        messagebox.showwarning("Empty", "No data to show!")
        return
    
    x_names = []
    y_scores = []
    for item in data:
        x_names.append(item['name'])
        y_scores.append(item['score'])
    
    plt.bar(x_names, y_scores, color='green')
    plt.title('My Class Grades')
    plt.show()

# Refreshing the main list on screen
def show_list_in_ui():
    listbox.delete(0, tk.END)
    data = get_data()
    # Apply our sorting algorithm
    sorted_data = my_bubble_sort(data)
    for s in sorted_data:
        listbox.insert(tk.END, s['name'] + " - Grade: " + str(s['score']))

# UI SETUP
window = tk.Tk()
window.title("My Student Tracker")
window.geometry("350x500")

tk.Label(window, text="Student Name:").pack()
name_in = tk.Entry(window)
name_in.pack()

tk.Label(window, text="Grade:").pack()
score_in = tk.Entry(window)
score_in.pack()

tk.Button(window, text="Save Student", command=add_new).pack(pady=5)

tk.Label(window, text="Search Name:").pack()
search_in = tk.Entry(window)
search_in.pack()
tk.Button(window, text="Search", command=search_now).pack(pady=5)

tk.Button(window, text="Show My Chart", command=draw_graph, bg="yellow").pack(pady=10)

tk.Label(window, text="Sorted List:").pack()
listbox = tk.Listbox(window, width=40)
listbox.pack(pady=5)

# Initialize the list on startup
show_list_in_ui()

window.mainloop()