# 🧑‍🎓 Student Management System

The **Student Management System** is a robust desktop application developed using Python's Tkinter library and SQLite database. It provides an intuitive graphical user interface (GUI) to manage student records, fee structures, and payment tracking efficiently. This project is ideal for educational institutions such as schools, colleges, and coaching centers that require a simplified digital solution for administrative tasks.

---

## 📚 Overview

This application helps institutions manage the following:

- Student information: name, roll number, class, section, contact, address, etc.
- Academic details: course, subjects, admission date, etc.
- Fee details: total fees, amount paid, due amount, payment status
- CRUD operations: Create, Read, Update, Delete student records
- Search and filter capabilities based on student attributes

The project was developed as part of a final year academic requirement and demonstrates the ability to design a full-featured local database system with a functional GUI.

---

## 🧰 Technologies Used

| Component        | Technology          |
|------------------|----------------------|
| Programming Lang | Python 3.x           |
| GUI Framework    | Tkinter              |
| Database         | SQLite3              |
| IDE              | Visual Studio Code / IDLE |
| OS               | Windows (tested)     |

---

## 🚀 Features

- 🎓 Add, edit, and delete student records easily
- 🔍 Search students by ID, name, or roll number
- 💰 Add and update fee payments
- 📈 View outstanding balances and payment status
- 🗃️ All data stored locally using SQLite (no internet needed)
- 🧩 Modular code structure for maintainability
- 🖥️ GUI interface is easy to navigate for non-technical users
- 📤 (Upcoming) Export data to CSV or PDF

---

## 📁 Project Structure

```
student_management_system/
├── main.py                  # Main GUI application
├── student.py               # Logic for student record form
├── database.py              # Handles SQLite connections and queries
├── fee.py                   # Fee management window
├── utils/                   # (Optional) utility functions or validators
├── requirements.txt         # Python package dependencies
└── README.md                # Documentation
```

---

## 🛠️ Installation & Usage

### 📥 Clone the Repository

```bash
git clone https://github.com/Maha5343/student_management_system.git
cd student_management_system
```

### 💾 Install Dependencies

Most dependencies (Tkinter, SQLite3) are built-in with Python. But to be safe:

```bash
pip install -r requirements.txt
```

### ▶️ Run the Application

```bash
python main.py
```

---

## 📸 Screenshots

*Add images of the UI screens here:*
- Dashboard view
- ![image](https://github.com/user-attachments/assets/4c921af8-2671-4bb9-ad08-ce471771d780)

- Add/Edit student form
- ![image](https://github.com/user-attachments/assets/6b7eecaa-5d6b-4288-891e-a12f2dea58fb)

- Fee payment section
- ![image](https://github.com/user-attachments/assets/417a89e6-6b99-412a-8a7f-82136cbccb3b)

---

## 🔒 Security & Limitations

- No login/authentication (yet)
- Only runs locally; no online sync or remote DB
- Not optimized for large datasets
- Currently supports single-user access

---

## 💡 Future Enhancements

- 🧑‍💼 Admin login and user authentication
- 🌐 Switch to MySQL or Firebase for cloud storage
- 📤 Export records as Excel or PDF files
- 📱 Web or mobile app integration
- 📊 Analytics dashboard for performance tracking

---

## 🧪 Testing

Manual testing was performed on Windows 10 with Python 3.11. Basic operations like insert, update, delete, and search were verified for both student and fee modules.

---

## 📜 License

This project is for educational use only and may be reused or extended with credit to the author.

---

## 👩‍💻 Author

**Maha Lakshmi**  
B.Tech Student – Computer Science  
GitHub: [@Maha5343](https://github.com/Maha5343)  
