import os, shutil, time, requests

def processing():
    s = "processing..."
    for _ in range(5):
        print(s)
        s += "."
        time.sleep(0.3)
        os.system("cls" if os.name=="nt" else "clear")
    print("succeeded!!")

def weather(location):
    url = "https://wttr.in/" + location + "?format=4"
    try:
        r = requests.get(url, timeout=5)
        return r.text.strip()
    except requests.exceptions.RequestException as e:
        return f"Connection error: {e}"

print("dear user, how can I help you today?   /1.exit/2.sort the name of the files/3.delete folder/4.delete file/5.add folder/6.move folder/7.move file/8.add file/9.weather/10.write a diary/")

while True:
    choice = input().strip().lower()

    if choice == "exit" or choice == "1":
        os.system("cls")
        break

elif choice == "sort the name of the files" or choice == "2":
    os.system("cls")
    folder = input("Where are the files you are talking about? ").strip()
    try:
        new_name = input("The new files will be named as file1, file2 etc. What name do you want to use? ").strip()
        
        for i, filename in enumerate(os.listdir(folder), start=1):
            old_path = os.path.join(folder, filename)
            if not os.path.isfile(old_path):
                print(f"Skipping {filename}, not a file.")
                continue

            ext = os.path.splitext(filename)[1]
            new_filename = f"{new_name}{i}{ext}"
            new_path = os.path.join(folder, new_filename)

            os.rename(old_path, new_path)
            print(f"Renamed: {filename} → {new_filename}")

        processing()

    except Exception as e:
        print("Error:", e)

    elif choice == "delete folder" or choice == "3":
        os.system("cls")
        folder_name = input("Folder name? ").strip()
        confirm = input("Are you sure? Yes(Y)/No(N): ").strip().lower()
        if confirm in ("yes", "y"):
            try:
                shutil.rmtree(folder_name)
                processing()
            except Exception as e:
                print("Error:", e)
        else:
            print("OK, your folder is saved.")
    elif choice == "delete file" or choice == "4":
        os.system("cls")
        file_name = input("File name? ").strip()
        confirm = input("Are you sure? Yes(Y)/No(N): ").strip().lower()
        if confirm in ("yes", "y"):
            try:
                os.remove(file_name)
                processing()
            except Exception as e:
                print("Error:", e)
        else:
            print("OK, your file is saved.")

    elif choice == "add folder" or choice == "5":
        os.system("cls")
        folder_name = input("Folder name? ").strip()
        try:
            os.makedirs(folder_name)
            processing()
        except Exception as e:
            print("Error:", e)

    elif choice == "move folder" or choice == "6":
        os.system("cls")
        folder_name = input("Folder name? ").strip()
        destination = input("Destination? ").strip()
        try:
            shutil.move(folder_name, destination)
            processing()
        except Exception as e:
            print("Error:", e)

    elif choice == "move file" or choice == "7":
        os.system("cls")
        file_name = input("File name? ").strip()
        destination = input("Destination? ").strip()
        try:
            shutil.move(file_name, destination)
            processing()
        except Exception as e:
            print("Error:", e)

    elif choice == "add file" or choice == "8":
        os.system("cls")
        file_name = input("File name? ").strip()
        try:
            open(file_name, 'w').close()
            processing()
        except Exception as e:
            print("Error:", e)

    elif choice == "weather" or choice == "9":
        os.system("cls")
        location = input("Please enter the place you want to search: ")
        print(weather(location))

    elif choice == "write a diary" or choice == "10":
        os.system("cls")
        date = input("What is the date? (weekday/day/month/year): ")
        weather_info = input("What is the weather? (optional): ")
        method = input("How will you write the content? text file/write it now: ").lower()

        content = ""
        if method == "text file" or method=="1":
            path = input("Paste the file path: ").strip()
            try:
                with open(path, "r", encoding="utf-8") as f:
                    content = f.read()
            except Exception as e:
                print("Error:", e)
        elif method == "write it now" or method=="2":
            print("double click enter to finish")
            lines = []
            while True:
                line = input()
                if line == "":
                    break
                lines.append(line)
            content = "\n".join(lines)
        diary = f"{date}                                              {weather_info}\n{content}"
        file_name = input("What file name do you want to save your diary as? (e.g. my_diary.txt): ").strip()
        try:
            with open(file_name, 'w', encoding='utf-8') as f:
                f.write(diary)
            processing()
        except Exception as e:
            print("Error:", e)
        print(f"The file has been saved as {file_name}. You can check or rename it anytime.")

    else:
        print("Unknown command. Please try again.")
