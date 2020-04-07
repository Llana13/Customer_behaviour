from simulation import simulated_list, full_simullation
import multiprocessing

list_locations = []
for i in range(3):
    list_locations.append(simulated_list())



def r_1():
    full_simullation(list_locations[0])
def r_2():
    full_simullation(list_locations[1])
def r_3():
    full_simullation(list_locations[2])

p1 = multiprocessing.Process(target=r_1)
p2 = multiprocessing.Process(target=r_2)
p3 = multiprocessing.Process(target=r_3)

p1.start()
p2.start()
p3.start()
