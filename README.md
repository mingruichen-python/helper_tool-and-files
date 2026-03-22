# Helper 1.0 — Python Command-Line Utility Tool

Helper 1.0 is a multifunctional command-line tool designed to simplify everyday tasks such as file management, folder operations, weather lookup, and diary writing. It provides an interactive menu and a clean workflow suitable for both beginners and experienced users.

---

## 🚀 Features

### 📁 File & Folder Management
- Sort file names in a folder (rename as file1, file2, etc.)
- Delete folders
- Delete files
- Create new folders
- Move folders
- Move files
- Create empty files

### 🌤 Weather Lookup
- Fetch real-time weather information using the wttr.in API  
- Simple and fast text-based weather output

### 📓 Diary Writer
- Write diary entries directly in the terminal  
- Or import content from an existing text file  
- Automatically formats and saves the diary to a user-defined filename

### 🎬 Visual Feedback
- Includes a simple “processing…” animation for better user experience

---

## 📁 Project Structure

.
├── helper_1.0.py   # Main script containing all features
├── image.png       # Optional image resource
├── README.md       # Project documentation



---

## ▶️ How to Run

Run the script from the terminal:

python helper_1.0.py



You will see the main menu:

exit

sort the name of the files

delete folder

delete file

add folder

move folder

move file

add file

weather

write a diary



Type either the number or the command name to use a feature.

---

## 🌤 Weather Example

Please enter the place you want to search:
Tokyo



Example output:

Tokyo: ☀️ +18°C



---

## 📓 Diary Example

You can choose:
- “text file” → import content from an existing file  
- “write it now” → type your diary directly in the terminal  

The diary will be saved as a `.txt` file with your chosen name.

---

## 📦 Requirements

This script uses only standard Python libraries except:

- `requests`

Install it with:

pip install requests



---

## 🛠 Compatibility

- Python 3.8+
- Works on Windows, macOS, and Linux  
- Automatically clears the terminal using `cls` or `clear`

---

## 📜 License

MIT License  
Feel free to modify or extend the tool.
