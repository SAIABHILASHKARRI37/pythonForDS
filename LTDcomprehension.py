#dictionary comprehension
city=['mumbai','paris','new york']
countries=['india','france','usa']
d={city:countries for city,countries in zip(city,countries)}
print(d)
#list comprehension
l=[1,2,3,4,5,6]
li=[i*i for i in l]
print(li)
#set comprehension
s=set([1,2,3,4,5,4,5])
print(s)