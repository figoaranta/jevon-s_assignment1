number = ""
with open("patients.txt", "r") as file:
    lines = file.read().splitlines()
    last_line = lines[-1]
    for char in last_line:
    	if char == "-":
    		break
    	number = number + char
