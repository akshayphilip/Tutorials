import numpy as np

#Array from list
list1=[1,2,3,4,5,6]

arr11=np.array(list1)

print(arr11)


tuple12=[10,11,12,13]
arr12=np.array(tuple12)
print(tuple12)

#numpy.zeros():create an array with all zeros

arr20=np.zeros(5)
print(arr20)

arr21=np.zeros((5,6))
print(arr21)

#numpy.ones():all the values in the array will be 1
arr30=np.ones(5)

print(arr30)

arr31=np.ones((5,2))
print(arr31)

#numpy.arrange():Create an array with regularly incrementing values
arr40=np.arange(10)
print(arr40)

arr41=np.arange(1,100)
print(arr41)

arr42=np.arange(20,100,5)
print(arr42)

arr43=np.arange(1.5,100,.2)
print(arr43)


#numpy.linspace():create an array with equally spaced numbers

arr50 = np.linspace(1,50)
print(arr50)


arr51 = np.linspace(1,50,3)
print(arr51)


#numpy.eye():creates a 2d with main dianal values as one and zeros eleswhere similar to an identity materix
arr60=np.eye(4)
print(arr60)

arr61=np.eye(6,4)
print(arr61)

#numpy.full():creates an array filled with specific value
print(np.full(5,0))

print(np.full(5,10))

print(np.full((4,4),3))


#numpy.random.randit() and numpy.random.random()

print(np.random.randint(1,100,5))
print(np.random.randint(1,100,(5,4)))

print(np.random.random(6))
print(np.random.random((6,10)))