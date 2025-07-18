# Birthday Reminder (Tkinter)

A cross-platform desktop application for managing and receiving reminders about birthdays, built with Python and Tkinter. Designed for both Linux and Windows users, the app provides an intuitive interface for storing birthdays and customizing notification settings to ensure you never miss an important date.

---

## Features

- **Add Birthdays Efficiently:**  
  Save names and dates in a straightforward form. Input validation ensures correct date formats (DD/MM/YYYY) and provides instant feedback.

- **Comprehensive Birthday List:**  
  Browse all stored birthdays in a scrollable list, making it easy to view upcoming events or manage entries.

- **Customizable Notifications:**  
  Set reminders for birthdays occurring today, one day before, or at intervals of your choice. Notifications are delivered using system tray alerts (via `plyer`), compatible with both Linux and Windows.

- **User-Friendly Interface:**  
  Clean, modern design powered by Tkinter for easy navigation and operation.

- **Easy Data Editing:**  
  Birthday and reminder settings are stored in plain text files (`all_brithday_list.txt`, `remind_setting.txt`), allowing for manual editing or backup.

- **Cross-Platform Compatibility:**  
  Fully supports both Linux and Windows environments.

---

## Installation

### 1. Clone the Repository

```bash
git clone https://github.com/whitedevilprogrammer/birthday-reminder-tkinter.git
cd birthday-reminder-tkinter
```

### 2. Install Dependencies

- **Python 3.x** is required.
- **Tkinter:**  
  - **Windows:** Usually included with Python installation.
  - **Linux (Debian/Ubuntu):**  
    ```bash
    sudo apt-get install python3-tk
    ```
- **plyer:** For desktop notifications.
  ```bash
  pip install plyer
  ```

---

## Usage

### Run the Application

```bash
python main2.0.py
```
or
```bash
python Birthday_remainder_app.py
```

### Add a Birthday

- Enter the name and the date (`DD/MM/YYYY`).
- Click "Add" to save.
- A confirmation message will notify you of success.

### View and Manage Birthdays

- Open the birthday list to view all entries.
- Scroll through the list with the built-in navigation.

### Set Reminder Preferences

- Adjust notification settings in the app to receive alerts for birthdays today, one day before, or per your schedule.

---

## File Structure

- `main2.0.py`, `Birthday_remainder_app.py`, `.pyw` files: Application entry points.
- `all_brithday_list.txt`: Stores all birthday records.
- `remind_setting.txt`: Stores user notification preferences.
- `colour less/birthday_remainder/`: Alternate UI scripts and data files.

---

## Example: Birthday List Entry

```
HARIHARAN.A:18/1/2003
JEBA SUGANTHI.J:9/2/2002
...
```

---

## Supported Platforms

- **Linux:** Fully supported; notifications via plyer.
- **Windows:** Fully supported; notifications via plyer.

---

## Contributing

We welcome contributions!  
To report bugs, request features, or improve documentation, please open an issue or submit a pull request.

---

## License

This project currently does not specify a license.

---

## Author

Developed by [whitedevilprogrammer](https://github.com/whitedevilprogrammer)
