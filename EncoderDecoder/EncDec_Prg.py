import os
import random
import csv
import shutil


def checkMultiple():
    entries = os.scandir('Files/')
    with open('Check.csv', 'w') as f:
        f.write("Class, UserName, Rest of info...\n")
        for files in entries:
            parts = files.name.split('_')
            Class = parts[0]
            try:
                UserName = parts[1]
            except:
                print("test")
            extension = files.name.split('.')[1]
            oldPath = files.path
            newPath = 'Files/' + UserName + '.' + extension
            os.rename(oldPath, newPath)
            Rest = parts[1:len(parts)]
            f.write("%s,%s,%s\n" % (Class, UserName, Rest))


def clean():
    entries = os.scandir('Files/')
    for files in entries:
        parts = files.name.split('_')
        parts1 = files.name.split('.')
        extension = parts1[len(parts1) - 1]  # Gets last . for extension
        if len(parts) > 1:
            newPath = 'Files/' + parts[1] + '.' + extension
            os.rename(files.path, newPath)


def encode():
    clean()
    entries = os.scandir('Files/')
    keys = dict()
    usedNum = list()

    for files in entries:
        oldPath = files.path

        while True:  # This loop ensures that the key hasn't been used previously
            num = random.randrange(1, 1000, 1)
            if num not in usedNum:
                usedNum.append(num)
                break

        keys[files.name] = num  # sets the key to the new random number
        newPath = 'Files' + "/" + str(num) + "((Grade((FB((." + str(files.name.split('.')[1])
        os.rename(oldPath, newPath)

    # Write keys to CSV file
    with open('Keys.csv', 'w') as f:
        for key in keys:
            f.write("%s,%s\n" % (key, keys[key]))


def decode():
    fileName = dict()
    grade_Enc = dict()
    feedback_Enc = dict()
    grade_Dec = dict()
    feedback_Dec = dict()

    # Open Keys.csv file and create the fileName dictionary so we can decode files
    with open('Keys.csv', newline='') as f:
        reader = csv.reader(f, delimiter=',')
        for rows in reader:
            userName = rows[0].split('.')[0]
            fileName[rows[1]] = userName
        f.close()

    # Extract Grade & Feedback values from Files directory
    path = "Files/"
    dirs = os.scandir(path)

    for files in dirs:
        string = files.name
        string = string.split("((")  # Split file name into parts
        grade_Enc[string[0]] = string[1]
        feedback_Enc[string[0]] = string[2]
        grade_Dec[fileName[string[0]]] = grade_Enc[string[0]]
        feedback_Dec[fileName[string[0]]] = feedback_Enc[string[0]]

    Feedback_list = dict()
    with open('Feedback.csv', newline='') as f:
        reader = csv.reader(f, delimiter=',')
        for rows in reader:
            Feedback_list[rows[0]] = rows[1]
        for key in grade_Dec.keys():
            feedback_Dec[key] = Feedback_list[feedback_Dec[key]]

    # Turn into graded file w/ netID's
    with open('Upload.csv', 'w') as f:
        f.write("%s,%s,%s,%s,%s,%s\n" % (
            'Username', 'Input', 'Grading Notes', 'Notes Format', 'Feedback to Learner', 'Feedback Format'))
        for key in grade_Dec.keys():
            if grade_Dec[key] == "Grade":
                grade_Dec[key] = "You forgot to enter a grade!"
            f.write("%s,%s,%s,%s,%s,%s\n" % (key.split('.')[0], grade_Dec[key], '', '', feedback_Dec[key], 'HTML'))


def clearDirectory():
    print("Clearing...")
    try:
        shutil.rmtree('Files')
    except OSError:
        print("Files doesnt exist")
    try:
        os.mkdir('Files')
    except OSError:
        print("Files already exists")
    try:
        os.remove('Upload.csv')
    except OSError:
        print("Upload.csv does not exist")
    try:
        os.remove('Keys.csv')
    except OSError:
        print("Keys.csv does not exist")


def main():
    print("*" * 30)
    print("Welcome to the anonymous grading program!")
    print("\t1. Check for multiple submissions from same user")
    print("\t\t (There should only be one submission from each user!)")
    print("\t2. Encode")
    print("\t3. Decode")
    print("\t4. Clear")
    print("\t5. Open Readme File")
    print("*" * 30 + "\n")
    ch = int(input("Select an option to continue: "))

    if ch == 1:
        print("Checking for multiples and exporting data...")
        checkMultiple()
    if ch == 2:
        print("Encoding Files...")
        clean()
        encode()
    if ch == 3:
        print("Decoding Files...")
        decode()
    if ch == 4:
        print("Clearing Directories")
        clearDirectory()
    if ch == 4:
        os.open("README.txt")


if __name__ == '__main__':
    main()