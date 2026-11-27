# Student Performance Analysis System
subjects = ["Maths", "Physics", "Python", "English", "Chemistry"]
names = []
marks = []

# Load data from file
try:
    f = open("students.csv", "r")
    lines = f.readlines()
    f.close()
    for line in lines[1:]:
        parts = line.strip().split(",")
        names.append(parts[0])
        marks.append([float(x) for x in parts[1:]])
    print("Data loaded.")
except FileNotFoundError:
    print("File not found. Starting with an empty table.")


def grade(avg):
    if avg >= 90:
        return "A+"
    elif avg >= 80:
        return "A"
    elif avg >= 70:
        return "B"
    elif avg >= 60:
        return "C"
    elif avg >= 50:
        return "D"
    else:
        return "F"


while True:
    print("\n--- STUDENT PERFORMANCE ANALYSIS ---")
    print("1. Add marks")
    print("2. Averages")
    print("3. Grades")
    print("4. Highest / Lowest")
    print("5. Weak subjects")
    print("6. Class summary")
    print("7. Exit")
    choice = input("Enter choice: ")

    if choice == "7":
        break
    elif choice == "1":
        name = input("Student name: ")
        row = []
        for s in subjects:
            m = float(input(s + " marks: "))
            while m < 0 or m > 100:
                print("Marks must be between 0 and 100.")
                m = float(input(s + " marks: "))
            row.append(m)
        names.append(name)
        marks.append(row)
    elif choice in ["2", "3", "4", "5", "6"]:
        if len(names) == 0:
            print("No data yet. Add students first.")
            continue
        if choice in ["2", "3", "6"]:
            total = 0
            for i in range(len(names)):
                avg = sum(marks[i]) / len(subjects)
                total = total + avg
                if choice == "2":
                    print(names[i], "average:", round(avg, 2))
                elif choice == "3":
                    print(names[i], "grade:", grade(avg))
            if choice == "2":
                for j in range(len(subjects)):
                    t = 0
                    for row in marks:
                        t = t + row[j]
                    sub_avg = t / len(names)
                    print(subjects[j], "average:", round(sub_avg, 2))
            if choice == "6":
                print("Total students:", len(names))
                print("Class average:", round(total / len(names), 2))
        if choice in ["4", "6"]:
            best = 0
            worst = 0
            for i in range(len(names)):
                if sum(marks[i]) > sum(marks[best]):
                    best = i
                if sum(marks[i]) < sum(marks[worst]):
                    worst = i
            best_avg = sum(marks[best]) / len(subjects)
            worst_avg = sum(marks[worst]) / len(subjects)
            print("Highest:", names[best], round(best_avg, 2))
            print("Lowest :", names[worst], round(worst_avg, 2))
        if choice in ["5", "6"]:
            found = False
            for j in range(len(subjects)):
                t = 0
                for row in marks:
                    t = t + row[j]
                sub_avg = t / len(names)
                if sub_avg < 60:
                    print("Weak subject:", subjects[j], round(sub_avg, 2))
                    found = True
            if not found:
                print("No weak subjects.")
    else:
        print("Invalid choice. Enter 1 to 7.")

# Save data to file
f = open("students.csv", "w")
f.write("Name," + ",".join(subjects) + "\n")
for i in range(len(names)):
    f.write(names[i] + "," + ",".join(str(m) for m in marks[i]) + "\n")
f.close()
print("Data saved. Program ended.")
