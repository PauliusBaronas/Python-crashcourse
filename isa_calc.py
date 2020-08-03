import math


while True:
	h = input("Please input the height, in meters (or write 'quit' to end): ")
	if str(h) == 'quit':
		break
	h = int(h)
	while h > 47000:
		print("sorry, maximum limit for the calculation is 47 km")
		h = input("Please input the height, in meters: ")
		h = int(h)
		while h < 0:
			print("sorry, height can't be negative number")
			h = input("Please input the height, in meters: ")
			h = int(h)
	while h < 0:
		print("sorry, height can't be negative number")
		h = input("Please input the height, in meters: ")
		h = int(h)
		while h > 47000:
			print("sorry, maximum limit for the calculation is 47 km")
			h = input("Please input the height, in meters: ")
			h = int(h)



	a1 = float(-0.0065)
	a3 = float(0.001)
	a4 = float(0.0028)
	p0 = int(101325)
	T0 = float(288.15)
	rho0 = float(1.225)
	h0 = int(0) 
	g = float(9.81)
	R = int(287)


	if h <= 11000:
		T1 = T0 + a1 * (h-h0)
		p1 = ((T1/T0)**(-g/(a1*R)))*p0
		print("The pressure is "+ str(round(p1, 4)) + " Pa")
		print("The temperature is "+ str(T1) + " K")
		t1 = T1-273
		print ("or" + str(t1) + "C")
		rho1 = p1/(R*T1)
		print ("The density of the air is " + str(rho1) + " kg/m3")
	elif h <= 20000:
		h1 = int(11000)
		T1 = T0 + a1 * (h1-h0)
		p1 = ((T1/T0)**(-g/(a1*R)))*p0
		print(p1)
		print(T1)
		power = (-g/(R*T1))*(h-h1)
		power = float(power)
		p2 = ((math.e)**power)*p1
		print("The pressure is "+ str(p2) + " Pa")
		print("The temperature is "+ str(T1) + " K")
		t1 = T1-273
		print ("or" + str(t1) + "C")
		rho2 = p2/(R*T1)
		print ("The density of the air is " + str(rho2) + " kg/m3")
	elif h <= 32000:
		h1 = int(11000)
		h2 = int(20000)
		T1 = T0 + a1 * (h1-h0)
		p1 = ((T1/T0)**(-g/(a1*R)))*p0
		power = (-g/(R*T1))*(h2-h1)
		power = float(power)
		p2 = ((math.e)**power)*p1
		h2 = int(20000)
		T3 = T1 + a3 * (h-h2)
		p3 = ((T3/T1)**(-g/(a3*R)))*p2
		print("The pressure is "+ str(p3) + " Pa")
		print("The temperature is "+ str(T3) + " K")
		t3 = T3-273
		print ("or" + str(t3) + "C")
		rho3 = p3/(R*T3)
		print ("The density of the air is " + str(rho3) + " kg/m3")
	elif h <= 47000:
		h1 = int(11000)
		h2 = int(20000)
		h3 = int(32000)
		T1 = T0 + a1 * (h1-h0)
		p1 = ((T1/T0)**(-g/(a1*R)))*p0
		power = (-g/(R*T1))*(h2-h1)
		power = float(power)
		p2 = ((math.e)**power)*p1
		T3 = T1 + a3 * (h3-h2)
		p3 = ((T3/T1)**(-g/(a3*R)))*p2
		T4 = T3 + a4 * (h-h3)
		p4 = ((T4/T3)**(-g/(a4*R)))*p3

		print("The pressure is "+ str(p4) + " Pa")
		print("The temperature is "+ str(T4) + " K")
		t4 = T4-273
		print ("or" + str(t4) + "C")
		rho4 = p4/(R*T4)
		print ("The density of the air is " + str(rho4) + " kg/m3")


