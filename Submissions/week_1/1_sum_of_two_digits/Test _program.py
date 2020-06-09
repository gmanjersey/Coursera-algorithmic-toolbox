import sys
n = int(sys.argv[1])
print(n)
print('_'.join([str(i * 2)  for i in range(n)]))

#Test the program:
#python3 Test_program.py 17 > input.txt
#python3 Test_program.py 17 < input.txt  - redirect input of your ptogram to the same text file.
