
import numpy as np

exams = np.asarray([[100, 200, 50, 400], [50, 0, 0, 100], [350, 100, 50, 200]])
print(exams)


u_a = [100,200,50,400]
u_b = [50,0,0,100]
u_c = [350,100,50,200]
exams = [u_a,u_b,u_c]

print(exams)

#Speed Test

my_list = [i for i in range(1000000)]
my_array = np.arange(1000000)

#%time for _ in range(10): my_list2 = [x**2 for x in my_list]


#%time for _ in range(10):my_array_2 = my_array **2

#print(my_array)
#print(my_list)

one_dim = np.array([1,2,3,4])
print(type(one_dim))

print(one_dim.shape) # kształt

print(one_dim.ndim) # liczba wymiarów – w tym przypadku 1 wymiar


two_dim = np.array([[100, 200, 50, 400], [50, 0, 0, 100], [350, 100, 50, 200]])

print("len: " + str(len(two_dim)))
print("shape: " + str(two_dim.shape))
print("ndim: " + str(two_dim.ndim))


print(two_dim.size) # rozmiar tablicy - ilość elementów
print(two_dim.itemsize) # rozmiar elementu tablicy - w bajtach

print(one_dim)

print(one_dim.reshape(2,2))
print("")


print(two_dim)
print("")
print(two_dim.reshape(4,3))
print("")


# print(two_dim.reshape(4,4))
print(two_dim.transpose())

print("")

my_list = [1,2,3,4,5]
print(np.array(my_list))


my_nested_list = [[1,2,3],[4,5,6],[7,8,9]]
print(np.array(my_nested_list))
print("")
print(np.arange(0,20))
print("")
print(np.arange(0,20,2))
print("")
print(np.zeros(3))
print("")
print(np.zeros((5,3)))
print("")
print(np.ones(6))
print(np.ones((2,3)))
print("")
print("")
#print(np.ones((2,3),dtype=np.int8))

print (np.linspace(0,6,10))
print("")
print(np.eye(4))

print("")
print("")

