

string="Hello World"

newstring=""
odd=True 
for c in string:
    if odd:
        newstring = newstring + c.upper()
    else:
        newstring = newstring + c.lower()
    odd = not odd
print (newstring)



def secondwords(string2):
    
    words = string2.split()
    
    
    for i in range(len(words)):
        if i % 2 == 1:  
            words[i] = words[i].upper()
    
    
    output_string = ' '.join(words)
    
    return output_string



string2 = "I am learning to code"
output_string = secondwords(string2)
print(output_string)


