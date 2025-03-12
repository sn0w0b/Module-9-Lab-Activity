#Martha Moreno Gonzalez
#03/11/2025

#asjk for a number until it is greater than 100

numbers = []
the_sum = 0  

while the_sum < 100: 
    numeros = int(input("Please enter youre numbers: "))
    numbers.append(numeros) 
    the_sum += numeros

print("The sum of the list is greater than 100, this is the sum: ", the_sum)
