import random
import sys
import os

# accept the number of tests as a command line parameter:
test = int(sys.argv[1])
# accept the parameter for the tests as a command line parameter:
n = int(sys.argv[2])


for i in range(tests):
    print("Test #" + str(i))
    # run the generator gen.py with parameter n and  the seed i
    os.system("python3_gen.py_" + str(n) + "_" + str(i) + "_>_input.txt")
    #run the model solution model.py
    # Notice that it is not necessary that solution is implemented in python, you can as well run
    # ./model <input.txt > model.txt for a C++ solution
    os.system("python3_model.py_<input.txt_>model.txt")
    # run the main solution
    os.system("python3_main.py_<input.txt_>main.txt")

    # read the output of the model solution:
    with open('model.txt') as f: model 