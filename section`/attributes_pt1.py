class program:
    language="python"  #attribute
    version= "3.3"      #attribute

print("1) program.__name__ =", program.__name__)

print("2)", type(program))

print(program.version)

#mutate the attribute in the program class
program.version="3.7"
print(program.version)


###
print("geattr", getattr(program, "version"))


print(program.__dict__)