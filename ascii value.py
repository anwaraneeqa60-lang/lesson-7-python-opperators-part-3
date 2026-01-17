
char = input("enter a sinngle character: ")
if type(char)is str and len (char) == 1:
    print("valid input")
else:
    print("please enter exactly one charecter")

ascii_value = ord(char)
print(f"character: {char}")
print(f"ascii value: {ascii_value}")
