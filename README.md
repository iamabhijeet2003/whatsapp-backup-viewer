# 📱 WhatsApp Backup Viewer

A simple Python-based GUI tool to read and view messages from a decrypted `msgstore.db` WhatsApp backup file.

This tool is built for forensic analysts or anyone who wants to examine WhatsApp messages stored in a SQLite database, with an easy-to-use interface.

---

## 🚀 Features

- Load and read `msgstore.db` files (SQLite format)
- View message timestamp, sender ("Me"/"Other"), and content
- Simple and clean interface using Tkinter
- No internet or account login required

---

## 🛠 Requirements

- Python 3.7+
- Tkinter (usually comes preinstalled)
- No external dependencies required

---

## 🔧 Installation

```bash
git clone https://github.com/iamabhijeet2003/whatsapp-backup-viewer.git
cd whatsapp-backup-viewer
python3 whatsapp_viewer.py
````

---

## 📂 How to Use

1. Make sure your `msgstore.db` is **decrypted** (not `.crypt12`).
2. Launch the viewer using the command above.
3. Go to `File > Open DB` and select your `msgstore.db`.
4. View the messages in the table (up to 1000 latest messages).

---

## 🧠 Notes

* The tool assumes the WhatsApp database contains a `message` table with standard columns like `timestamp`, `from_me`, and `text_data`.
* If your database structure is different, you may need to adjust the SQL query in the script.

---

## 📝 License

MIT License

---

## 💻 Author

[Abhijeet Singh](https://github.com/iamabhijeet2003)

