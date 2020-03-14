#Program to write data into text file T2.txt from consols
#T2.txt must be empty before running to program


while (1):
	#Opens text file T2.txt in append mode
	file2 = open("T2.txt", "a+")
	#Waits for user input
	line = input()
	#Writes the line into the text file
	file2.write(line)
	#Write a newline character
	file2.write("\n")
	#Closes the file every iteration and thus saves it
	file2.close()