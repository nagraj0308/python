from module2 import my_function

print("Always executed")
# my_function()
if __name__ == "__main__":
    print("Executed when invoked directly")
else:
    print("Executed when imported")
"""
Conclusion:-
1. every .py file in python is called as module
2. Before executing code, Python interpreter reads source file and define few special 
    variables/global variables. If the python interpreter is running that module 
    (the source file) as the main program, it sets the special __name__ variable to 
    have a value “__main__”. If this file is being imported from another module, 
    __name__ will be set to the module’s name. 
3. when we import a file, all statement at indentation gets executed even without calling.

"""