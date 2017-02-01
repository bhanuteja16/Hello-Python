import random

list1 = random.sample(range(random.randint(30,100)), random.randrange(3,30))
list2 = random.sample(range(random.randint(30,100)), random.randrange(3,30))


print("list1 is " + str(list1))
print("list2 is " + str(list2))

ov=[]

for x in list1:
	for y in list2:
		if x == y:
			if x not in ov:
				ov.append(x)

print(ov)
