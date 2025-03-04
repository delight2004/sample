fruits=["apple","banana","orange","pear","pawpaw"]
print(fruits)
fruits.append("guava")
fruits.remove("orange")
print(fruits)

squares=[x**2 for x in range(1,5)]
print(squares)

movies=("Fast and Furious", "Batman", "Superman")
x,y,z=movies
print(x,y,z)

set_nums={34,12,18,99,100}
set_nums.add(56)
set_nums.remove(34)
set_nums2={12,99,123,67,73}
x=set_nums|set_nums2
print(x)
y=set_nums&set_nums2
print(y)
z=set_nums-set_nums2
print(z)

student_details={"name":"Delight","age":20,"grade":"A"}
student_details["grade"]="A+"
for key,value in student_details.items():
    print(key,value)