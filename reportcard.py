# write a program to find the grade of a student

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
print("Your average marks =", avg)

if avg >= 91:
    print("Grade: O")
elif avg >= 81:
    print("Grade: A")
elif avg >= 71:
    print("Grade: B")
elif avg >= 61:
    print("Grade: C")
elif avg >= 51:
    print("Grade: D")
else:
    print("You are not promoted.")
