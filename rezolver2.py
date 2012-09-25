filename = "dict.csv"

lookup = {}

with open(filename,"r") as file:
    for line in file:
    	(key, value) = line.split(" ")[0:2]
    	lookup[key] = value

while(True):
	address = raw_input("Enter <address> to lookup (Enter to exit): ")
	if(address == ""): 
		break
	if address in lookup:
		print(lookup[address])
	else:
		print("No key found: ")

print("End!")