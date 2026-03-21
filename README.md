# 📝 About

A terminal-based task management application built with Python (non-persistent).

## 🚀 Features

- **View Tasks** — Displays all tasks along with their description, status, and time estimate
- **Add Task** — Adds a new task with a title, description, status, and time estimate
- **Mark as Done** — Changes a task's status to "Done" based on its ID
- **Delete Task** — Removes a task from the list based on its ID

---

## 🛠️ Technologies

- Python 3.11.9
- Built-in modules: `unittest`, `io`, `unittest.mock`

---

## 📂 File Structure
```
📁 todo-list/
├── script.py                    # Main program file
├── test_tambah_tugas.py         # Unit test for add task function
├── test_tandai_selesai.py       # Unit test for mark as done function
├── test_lihat_tugas.py          # Unit test for view tasks function
├── test_hapus_tugas.py          # Unit test for delete task function
└── README.md
```

## 📖 How to Use

Once the program is running, a menu will appear as follows:
```
Welcome to the To-Do List Application
1. View All Tasks
2. Add Task
3. Mark Task as Done
4. Delete Task
5. Exit
Enter your choice:
```

Enter a number from **1–5** corresponding to the desired operation.

---

## 🧪 Unit Test Coverage

| Test File               | Function Tested     | Scenarios                              |
|-------------------------|---------------------|----------------------------------------|
| `test_tambah_tugas.py`  | `tambah_tugas()`    | Valid input                            |
| `test_tandai_selesai.py`| `tandai_selesai()`  | Valid ID, ID not found                 |
| `test_lihat_tugas.py`   | `lihat_tugas()`     | Empty list, 1 item, multiple items     |
| `test_hapus_tugas.py`   | `hapus_tugas()`     | Valid ID, ID not found                 |
