"""
File: weather_master.py
Name: Karen Wong
-----------------------
This program should implement a console program
that asks weather data from user to compute the
average, highest, lowest, cold days among the inputs.
Output format should match what is shown in the sample
run in the Assignment 2 Handout.

"""

EXIT = -100

def main():
	"""
	This program is used to calculate the highest, lowest, average temperature
	and the total cold day (temperature < 16 ) of the given sequences.
	"""

	print('stanCode "Weather Master 4.0"!')
	temp = int(input('Next Temperature(or ' + str(EXIT) + ' to quit)? '))
	if temp == EXIT:
		print('No temperature were entered.')
	else:
		highest = temp
		lowest = temp
		average = temp
		if temp < 16:
			cold = 1
		else:
			cold = 0
		total_num = 1
		while True:
			temp1 = int(input('Next Temperature(or ' + str(EXIT)+' to quit)? '))
			if temp1 == EXIT:
				break
			else:
				total_num += 1
				if temp1 > highest:
					highest = temp1

				if temp1 < lowest:
					lowest = temp1
				if temp1 <= 16:
					cold += 1
				average = (temp1+average*(total_num-1))/total_num
				temp = temp1

		print('Highest temperature = ' + str(highest))
		print('Lowest temperature = ' + str(lowest))
		print('Average temperature = ' + str(average))
		print(str(cold)+' cold days!')


if __name__ == "__main__":
	main()
