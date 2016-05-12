grades = [[100,99,98,99,100],
		  [95,0,85,70],
		  [90,91,95,97,99,92]]
		  

rowAverages = []

for row in grades:
	sum = 0.0
	mean = 0.0
	howMany = 0.0
	for number in row:
		sum += number
		howMany += 1
	mean = sum/howMany
	rowAverages.append(mean)

	
howMany = 0.0
total = 0.0

for row in grades:
	for number in row:
		total += number
		howMany += 1
		
	
		
average = total/howMany

average = round(average, 1)

print('The average score for student 1 is {}. The average score for student 2 is {}. The average score for student 3 is {}.'.format(rowAverages[0],rowAverages[1],rowAverages[2]))
print("The average score of all of the grades is {}.".format(average))


