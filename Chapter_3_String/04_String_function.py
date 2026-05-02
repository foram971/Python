Name = 'Foram'

print(len(Name)) # Print length of string
print(Name.endswith('am')) #Check String End with am ,if yes then TRUE 
print(Name.endswith('AM')) #Case-Sensitive
print(Name.startswith('fo')) #Check String Start with ,return boolean 
print(Name.capitalize()) #It capitalize first character of a given string
print(Name.upper()) #Uppercase for all words


#Count total number of occurrences of any character
count = Name.count("r")
print(count) 

#Returns the index of first occurrence of that word in the string
index = Name.find("m")
print(index)

#This function replace the old word with new word in the entire string.
replace_string = Name.replace('oram','ORAM')
print(replace_string)