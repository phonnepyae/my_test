import random

print("This is from random.random fun generate between 0 and 1 in  float. =>",random.random())


# for integer number


randint_num = random.randint(10,100)

print("The generated number of randint fun is ",randint_num)


randrange_num = random.randrange(10,100,3)

print("The generated number of randrange fun is  ",randrange_num)


#for float number


uniform_number = random.uniform(1,10)

print("The generated number of random.uniform fun is ",uniform_number)

triangular_number = random.triangular(10,30,3)

print("The generated number of random.triangular fun is ",round(triangular_number,3))


#for iterator(list,tuple,etc)


list1 = [1,2,3,4,5,6,'aung','maung','kyaw','myo','ko']

random.shuffle(list1) # non_return_type

print("After shuffling the list =>",list1)


choice_object = random.choice(list1)

print("This is choisen objuect  from list1 ",choice_object)

print("This is from random.sample fun =>",random.sample(list1,2))

random.seed(5)

print("This is from random.seed fun =>",round(random.random(),3))