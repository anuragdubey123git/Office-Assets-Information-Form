#############crud operation on list##################
print("=====CRUD opertion on list=====")
#create
my_list= []
print(my_list)
my_list.append(10)
my_list.append(20)

#after adding elements
print("after adding number:",my_list)

# read
print("read second element:",my_list[1])
# print("read all elements:",my_list)

# update
my_list[1]=211
print("updated list:",my_list)

#delete
my_list.remove(10)
print("after deletion:",my_list)

################crud operation on tuple####################
print("\n=====CRUD Operation on tuple=====")
#create tuple
my_tuple=()
print((my_tuple))
my_tuple=(10,20)
print("after adding eement:",my_tuple)

#read tuple
print("read second element:",my_tuple[1])

#update tuple
new_tuple=list(my_tuple)
new_tuple[0]=1111
print("after updating:",new_tuple)

# delete tuple
new_tuple.remove(20)
print("after delete",new_tuple)



#############crud operation on set#################
print("\n=====CRUD Operation on set=====")

#crete set
my_set=set()
print(my_set)
my_set.add("apple")
my_set.add("banana")
my_set.add("cherry")
print(my_set)

#read set
print("read all set",my_set)  # it does not show the indexing bcoz it is unoderered type.


# update set
my_set.remove("banana")      # remove and discard performs the same both of them delete the elements.
my_set.add("blueberry")
print("after updating set",my_set)

# detete the set
my_set.discard("cherry")
print("after deleting set:",my_set)


##############crud operation on dictionary############
print("\n=====CRUD Operation on dictionary=====")
#create
my_dict={}
print(my_dict)
my_dict["name"]="Anurag Dubey"
my_dict["age"]= 22
print("after create",my_dict)

#read
print("the name is",my_dict["name"],"age is",my_dict["age"])


#update
my_dict["age"]=23
print("after updation in age",my_dict)

#delete
del my_dict["name"]
print("after deleting the name only age will be there:",my_dict)
