#Martha Moreno Gonzalez
#03/11/2025

#CREATE A LIST THAT HAS VALUES DIVISABLE BY TEN 
#AS WELL AS HAVE IT REACH UP UNTIL 50 

tens = []
counter = 0

while counter < 50:
    if counter % 10 == 0:
        tens.append(counter)
    counter += 1

print(tens)


