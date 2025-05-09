import tkinter as tk
from tkinter import filedialog, messagebox, ttk
import sqlite3
import os

class WhatsAppViewer:
    def __init__(self, root):
        self.root = root
        self.root.title("WhatsApp msgstore.db Viewer")
        self.create_widgets()

    def create_widgets(self):
        self.menu = tk.Menu(self.root)
        self.root.config(menu=self.menu)

        file_menu = tk.Menu(self.menu, tearoff=0)
        file_menu.add_command(label="Open DB", command=self.open_db)
        file_menu.add_separator()
        file_menu.add_command(label="Exit", command=self.root.quit)
        self.menu.add_cascade(label="File", menu=file_menu)

        self.tree = ttk.Treeview(self.root, columns=("timestamp", "sender", "message"), show='headings')
        self.tree.heading("timestamp", text="Timestamp")
        self.tree.heading("sender", text="Sender")
        self.tree.heading("message", text="Message")
        self.tree.column("timestamp", width=150)
        self.tree.column("sender", width=100)
        self.tree.column("message", width=600)
        self.tree.pack(expand=True, fill=tk.BOTH)

    def open_db(self):
        db_path = filedialog.askopenfilename(
            title="Select msgstore.db file",
            filetypes=[("SQLite Database", "*.db *.sqlite *.sqlite3")]
        )
        if db_path and os.path.exists(db_path):
            try:
                self.conn = sqlite3.connect(db_path)
                self.load_messages()
            except Exception as e:
                messagebox.showerror("Error", f"Failed to open DB: {e}")

    def load_messages(self):
        try:
            cursor = self.conn.cursor()
            cursor.execute("""
                SELECT 
                    datetime(timestamp / 1000, 'unixepoch') AS msg_time,
                    from_me,
                    text_data
                FROM message
                WHERE text_data IS NOT NULL
                ORDER BY timestamp DESC
                LIMIT 1000
            """)
            rows = cursor.fetchall()
            self.tree.delete(*self.tree.get_children())
            for row in rows:
                direction = "Me" if row[1] == 1 else "Other"
                self.tree.insert("", tk.END, values=(row[0], direction, row[2]))
        except Exception as e:
            messagebox.showerror("Error", f"Failed to load messages: {e}")

if __name__ == "__main__":
    root = tk.Tk()
    app = WhatsAppViewer(root)
    root.geometry("900x600")
    root.mainloop()
