#Calculating factors of an integer: 

def is_factor(a, b):
	if b % a == 0:
		return True
	else:
		return False


print(is_factor(4, 1024))


#Calculating a multiplication table: 
def multip_table(a):
	for i in range (1, 13):
		print("{0} x {1} = {2}" .format(a, i, a*i))

multip_table(5)

#Converting kilometers to miles calculator:

def miles_km(c):
	km = c * 1.609
	print("Distance in miles: {0} " .format(km))


miles_km(25)


#Quadratic Equation Roots Calculator: 
#Ax^2 + Bx + C = -b +/- sqrt(b^2 - 4ac)/(2a)

def Qroots(a, b, c):

	D= (b**2 - 4*a*c)**0.5 #**0.5 = sqrt
	x_1 = (-b + D)/(2*a)
	x_2 = (-b - D)/(2*a)

	print("x1: {0}" .format(x_1))
	print("x2: {0}" .format(x_2))
