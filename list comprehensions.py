# LIST COMPREHENSIONS
l1 = [i for i in range(100) if i%3==0]
print(l1)

l2=[i for i in range(50)]
print(l2)

#in comprehension method condition are optional
#list comprehension k sath sath dict,set and genrater comprehension bhi hoti hai

# DICT COMPREHENSIONS

d2= {i:f'item{i}' for i in range(100)}
print(d2)

# set comprehension

s1= {dress for dress in ["dress1","dress2","dress1","dress3","dress2"]}
print(s1)
