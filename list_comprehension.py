#1. list comprehension

list=["jaysir","jigarsir","hardik","kishor","manav"]
new_list=[]

for i in list:
    if "j" in i:
        new_list.append(i)
print("new_list :",new_list)

#2. Without list comprehension you will have to write a for statement with a conditional test inside:

fruits = ["apple", "banana", "cherry", "kiwi", "mango"]

newlist = [x for x in fruits if "a" in x]

print("newlist :",newlist)

#3

l1=[i for i in range(1,100) if i%3==0]
print("new l1 :",l1)

#4.vovel

n1='tops technologies ahmedabad'
n2=[i for i in n1 if i not in 'aeiou']
print(n2)
