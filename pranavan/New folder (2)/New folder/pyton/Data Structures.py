lst = ['Chair','Tablr','Spoon','Pen','laptop',]

print("length of list :", len(lst))
print("First Eliment:", lst[0])
print("Last Eliment:", lst[-2])

lst.append('Book')
print("updated List:",lst)

lst.remove('Pen')
print("updated List:",lst)

lst.sort()
print("sorted List:",lst)

lst.pop(3)
print("updated List:",lst)
      
lst.reverse()
print("reverseed List:",lst)

print("multiplion on list:",lst*3)

lst=lst[:4]
print("sliced List:",lst)

lst.clear()
print("updated List:",lst)



my_dict ={1:'pen',2:'book'}

my_dict ={'name':'Raj',1:[2,4,3]}

my_dict ={'name' : 'Raj','age':20}

print(my_dict['name'])

