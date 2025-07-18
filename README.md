# 🎉 Birthday Reminder Desktop App (Python + Tkinter)

A lightweight, cross-platform desktop application to help you manage and get notified of birthdays — built using Python and Tkinter. This user-friendly tool works seamlessly on both Windows and Linux, ensuring you never forget an important birthday again.

---

## 🚀 Features

- ✅ **Add Birthdays Easily**  
  Enter names and birthdays with input validation (`DD/MM/YYYY` format).

- 📋 **View All Birthdays**  
  Scrollable list to view, manage, or backup birthdays.

- 🔔 **Custom Notifications**  
  Get system tray alerts (via `plyer`) — for today, tomorrow, or custom days in advance.

- 🎨 **Modern Tkinter UI**  
  Clean, intuitive interface for a better user experience.

- 📝 **Plaintext Data Storage**  
  All birthdays and preferences are saved in `.txt` files for simplicity and portability.

- 🖥️ **Cross-Platform**  
  Compatible with both **Linux** and **Windows**.

---

## 🛠️ Installation

### 1. Clone the Repository

```bash
git clone https://github.com/whitedevilprogrammer/birthday-reminder-tkinter.git
cd birthday-reminder-tkinter
```

### 2. Install Requirements

* ✅ Python 3.x
* ✅ Tkinter

  * **Windows:** Included with Python.
  * **Linux (Ubuntu/Debian):**

    ```bash
    sudo apt-get install python3-tk
    ```
* ✅ Plyer for notifications:

  ```bash
  pip install plyer
  ```

---

## 💻 Usage

### Run the App

```bash
python main2.0.py
```

or

```bash
python Birthday_remainder_app.py
```

### Add a Birthday

* Type name and date (`DD/MM/YYYY`).
* Click **"Add"** to save.
* Receive confirmation on success.

### Set Reminders

* Customize when to be notified: same day, 1 day before, etc.

### View/Edit Birthdays

* All birthdays stored in `all_brithday_list.txt`.
* Preferences in `remind_setting.txt`.

---

## 📁 File Structure

```
birthday-reminder-tkinter/
│
├── main2.0.py
├── Birthday_remainder_app.py
├── all_brithday_list.txt         # Stores birthday entries
├── remind_setting.txt            # Notification settings
├── colour less/birthday_remainder/
│   └── *.pyw, *.txt              # Alternate UI and data
```

---

## 🧪 Sample Entry Format

```
HARIHARAN.A:18/1/2003
JEBA SUGANTHI.J:9/2/2002
```

---

## 🧑‍💻 Contributing

Feel free to open an issue or PR for:

* Bugs 🐞
* Features 💡
* UI Enhancements 🎨
* Code Cleanup 🧹

---

## 📜 License

This project is currently unlicensed. You may fork, use, or contribute — attribution appreciated.

---

## 👤 Author

Developed with ❤️ by [whitedevilprogrammer](https://github.com/whitedevilprogrammer)

```

Let me know if you want badges (like Python version, platform, etc.) or screenshots/gif previews added at the top!
