# FIZZBUZZ-Obtiene múltiplos de 3, de 5 y de 3 y 5

for x in range (1,100):
	if x%5==0 and x%==0:
		print "FIZZBUZZ"

	elif x%5==0:
		print "Fizz" #Si encuentra los múltiplos de 5, imprime Fizz

	elif x%3==0:
		print "Buzz" #Si encuentra los múltiplos de 3, imprime Buzz
	
	else:
		print x #Cuando no cumple lo anterior imprime el resto

