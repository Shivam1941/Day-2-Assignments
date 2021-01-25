
inp_str = "Blastersss"
out = {x : inp_str.count(x) for x in set(inp_str )}  
print ("Occurrence of all characters is :\n "+ str(out))  
