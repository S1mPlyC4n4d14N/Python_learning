## Unit 7 Exercise 6
## Write a function called sum_first_odd(n), That calculates the sum of the first n odd integers and prints the result.
## Kole McDougall
## 01/19/2022

#Functions
def sum_first_odd(n):
	x = 0
	y = 1
	z = 0
	while (x < n):
		z += y
		y = y+2
		x += 1
	return z

#Program
print(sum_first_odd(0))
print(sum_first_odd(1))
print(sum_first_odd(3))
print(sum_first_odd(10))
print(sum_first_odd(30))
