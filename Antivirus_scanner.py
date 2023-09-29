import tkinter as tk
from tkinter import filedialog
from tkinter import ttk
import os
import time
import random


class AntivirusScanner:
    def __init__(self, root):
        self.root = root
        self.root.title("Antivirus Scanner")

        # Variables
        self.files_to_scan = []
        self.scan_results = {}

        # UI components
        self.file_tree = ttk.Treeview(root, columns=('File', 'Status'), show='headings')
        self.file_tree.heading('File', text='File')
        self.file_tree.heading('Status', text='Status')
        self.file_tree.pack(padx=10, pady=10)

        self.scan_button = tk.Button(root, text='Scan', command=self.scan_files)
        self.scan_button.pack(pady=10)

        # Menubar
        menubar = tk.Menu(root)
        file_menu = tk.Menu(menubar, tearoff=0)
        file_menu.add_command(label="Open File", command=self.add_file_to_scan)
        file_menu.add_command(label="Open Folder", command=self.add_folder_to_scan)
        menubar.add_cascade(label="File", menu=file_menu)
        root.config(menu=menubar)

    def add_file_to_scan(self):
        file_path = filedialog.askopenfilename(filetypes=[("All Files", "*.*")])
        if file_path:
            self.files_to_scan.append(file_path)
            self.update_file_tree()

    def add_folder_to_scan(self):
        folder_path = filedialog.askdirectory()
        if folder_path:
            for root, dirs, files in os.walk(folder_path):
                for file in files:
                    self.files_to_scan.append(os.path.join(root, file))
            self.update_file_tree()

    def update_file_tree(self):
        self.file_tree.delete(*self.file_tree.get_children())
        for file_path in self.files_to_scan:
            self.file_tree.insert('', 'end', values=(file_path, 'Waiting'))

    def scan_files(self):
        for item in self.file_tree.get_children():
            file_path = self.file_tree.item(item, 'values')[0]
            self.update_scan_status(item, 'Scanning...')
            time.sleep(0.5)  # Simulate scanning delay
            result = 'Safe' if random.choice([True, False]) else 'Infected'  # Simulate scan result
            self.update_scan_status(item, result)

    def update_scan_status(self, item, status):
        self.file_tree.item(item, values=(self.file_tree.item(item, 'values')[0], status))


if __name__ == "__main__":
    root = tk.Tk()
    antivirus_scanner = AntivirusScanner(root)
    root.mainloop()
