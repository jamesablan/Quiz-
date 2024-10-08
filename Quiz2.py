# Create variables that will store the names of your groupmates
mem1_name= "Ablan, Angelbert James F"
mem2_name= "Ragaza, Marc Dion G 20"
mem3_name= "Rupisan, Christian F 20"
# Create variables that contains their age in whole number
mem1_age= 21
mem2_age= 20
mem3_age= 20
# Create variables that contains their weekly allowance in decimal form
mem1_allowance= 800.00
mem2_allowance= 500.00
mem3_allowance= 500.00
# Print all the results of each member
print(f"mem 1: {mem1_name}, his age is {mem1_age}, allowance per week is {mem1_allowance}")
print(f"mem 2: {mem2_name}, his age is {mem2_age}, allowance per week is {mem2_allowance}")
print(f"mem 3: {mem3_name}, his age is {mem3_age}, allowance per week is {mem3_allowance}")
# Calculate the length of the names
mem1_name_length= len(mem1_name)
mem2_name_length= len(mem2_name)
mem3_name_length= len(mem3_name)

# Perform & print math operations for age

print("The sum of their age is:", mem1_age + mem2_age)
print("The sum of their age is:", mem2_age + mem3_age)

#Create a difference of their age
print("The difference of their age is:", mem1_age - mem2_age)
print("The difference of their age is:", mem2_age - mem3_age)

# Create a product of their age
print("The product of their age is:", mem1_age * mem2_age)
print("The product of their age is:", mem2_age * mem3_age)

# Create a product of the allowance
print("The product of their allowance is:", mem1_allowance * mem2_allowance)
print("The product of their allowance is:", mem2_allowance * mem3_allowance)



# Compare values

print("The age comparison of mem1 & mem2 is:", mem1_age == mem2_age)
print("The age comparison of mem2 & mem3 is:", mem2_age == mem3_age)

# Compare the name length
print("The name length comparison of mem1 & mem2:", mem1_name_length == mem2_name_length)
print("The name length comparison of mem2 & mem3:", mem2_name_length == mem3_name_length) 
