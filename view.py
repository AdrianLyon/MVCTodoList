# view.py
import tkinter as tk

class TaskView:
    def __init__(self, root):
        self.root = root
        self.root.title("To-Do List")

        self.task_listbox = tk.Listbox(root, height=10, width=40)
        self.task_listbox.pack(pady=10)

        self.task_entry = tk.Entry(root, width=40)
        self.task_entry.pack(pady=10)

        self.add_button = tk.Button(root, text="Add Task")
        self.add_button.pack(pady=5)

        self.delete_button = tk.Button(root, text="Delete Task")
        self.delete_button.pack(pady=5)

    def get_task_entry(self):
        return self.task_entry.get()

    def add_task_to_listbox(self, task):
        self.task_listbox.insert(tk.END, task)

    def delete_task_from_listbox(self, task_index):
        self.task_listbox.delete(task_index)

    def get_selected_task_index(self):
        try:
            return self.task_listbox.curselection()[0]
        except IndexError:
            return None

    def clear_task_entry(self):
        self.task_entry.delete(0, tk.END)
