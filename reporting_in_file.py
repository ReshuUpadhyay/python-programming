math = int(input("Enter the term marks of math out of 100: "))
if math < 0 or math > 100:
    print("Invalid input for math marks.")
    exit()

chem = int(input("Enter the term marks of chemistry out of 100: "))
if chem < 0 or chem > 100:
    print("Invalid input for chemistry marks.")
    exit()

elec = int(input("Enter the term marks of electronics out of 100: "))
if elec < 0 or elec > 100:
    print("Invalid input for electronics marks.")
    exit()

py = int(input("Enter the term marks of python out of 100: "))
if py < 0 or py > 100:
    print("Invalid input for python marks.")
    exit()

eng = int(input("Enter the term marks of english out of 100: "))
if eng < 0 or eng > 100:
    print("Invalid input for english marks.")
    exit()

avg = (math + chem + elec + py + eng) / 5


if avg >= 91:
    grade = "O"
elif avg >= 81:
    grade = "A"
elif avg >= 71:
    grade = "B"
elif avg >= 61:
    grade = "C"
elif avg >= 51:
    grade = "D"
else:
    grade = "You are not promoted."

with open("report.txt", "w+") as file:
    file.write("Subject\t\tMarks\n")
    file.write("-------------------\n")
    file.write(f"Math\t\t{math}\n")
    file.write(f"Chemistry\t{chem}\n")
    file.write(f"Electronics\t{elec}\n")
    file.write(f"Python\t\t{py}\n")
    file.write(f"English\t\t{eng}\n")
    file.write("-------------------\n")
    file.write(f"Average Marks:\t{avg:.2f}\n")
    file.write(f"Grade:\t\t{grade}\n")

print("Report generated and saved in report.txt")

print("\nReading the contents of report.txt:")
with open("report.txt", "r") as file:
    print(file.read())
