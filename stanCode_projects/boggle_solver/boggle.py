"""
File: boggle.py
Name: Kare Wong
----------------------------------------
This file is a boggle game, which automatically find words in sequences of adjacent letters.
"""

# This is the file name of the dictionary txt file
# we will be checking if a word exists by searching through it
FILE = 'dictionary.txt'


N = 4                # The number of row
boggle_lst = []      # The list to store each row of input character
ans_lst = []         # The list to store all the boggle words
word_count = 0       # Int to count the total amount of words in ans_lst


ALPHABET = 'abcdefghijklmnopqrstuvwxyz'
dic_lst = [set()for i in range(26)] # The list to store all the words in dictionary.txt


def main():
	"""
	This program used to find out all word that make up with 16 letter on the grid.
	Users are asked to 16 characters into a grid by sequence

	"""

	for i in range(N):
		row = input(str(i+1)+' row of letters: ').split()
		if len(row) != N:
			print("Illegal Format")
			break
		boggle_lst.append(row)

	read_dictionary()
	current_lst = []           # list that store the current string for searching
	index_lst = []             # list to store index number of input word
	for i in range(N):
		for j in range(N):
			start_x = i
			start_y = j
			index_lst.append((start_x, start_y))
			helper(start_x, start_y, current_lst, index_lst)
			# reset index_lst for next word
			index_lst = []
	print('There are ', word_count, 'in  total.')



def helper(start_x, start_y, current_lst, index_lst):
	"""
	:param start_x: int, the x coordinate of current element
	:param start_y: int, the x coordinate of current element
	:param current_lst: list, the string in the searching process
	:param index_lst: list, The index list for the string list, to separate same characters
	"""
	global word_count

	for i in range(-1, 2, 1):
		for j in range(-1, 2, 1):
			x = start_x + i
			y = start_y + j
			if 0 <= x < N:
				if 0 <= y < N:
					if (x, y) not in index_lst:
						index_lst.append((x, y))
						current_lst.append(boggle_lst[x][y])
						w = ''
						for ch in current_lst:
							w += ch
						if has_prefix(w):
							if len(current_lst) >= N:
								if w not in ans_lst:
									if w in dic_lst[ALPHABET.find(w[0])]:
										ans_lst.append(w)
										word_count += 1
										print('Found ', w)
							helper(x, y, current_lst, index_lst)
						# Un-choose
						current_lst.pop()
						index_lst.pop()


def read_dictionary():
	"""
	This function reads file "dictionary.txt" stored in FILE
	and appends words in each line into a Python list
	"""
	with open(FILE, 'r') as f:
		for line in f:

			dic_lst[ALPHABET.find(line[0])].add(line.strip('\n'))


def has_prefix(sub_s):
	"""
	:param sub_s: (str) A substring that is constructed by neighboring letters on a 4x4 square grid
	:return: (bool) If there is any words with prefix stored in sub_s
	"""
	for item in dic_lst[ALPHABET.find(sub_s[0])]:
		if item.startswith(sub_s):
			return True


if __name__ == '__main__':
	main()
