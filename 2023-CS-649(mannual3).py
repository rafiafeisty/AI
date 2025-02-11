dictionary = {
    "apple": 6,
    "grapes": 3,
    "mango": 16,
    "oranges": 7,
    "pineapple": 5,
}

#Task 1
sorted_by_values = dict(sorted(dictionary.items(), key=lambda item: item[1]))
print("Sorted by values (ascending):", sorted_by_values)


#Task 2
key_to_check = input("Enter the key to check: ")
if key_to_check in dictionary:
    print(f"The key '{key_to_check}' exists in the dictionary with value {dictionary[key_to_check]}.")
else:
    print(f"The key '{key_to_check}' does not exist in the dictionary.")

#Task 3
dict1={
    "model":"BMW",
    "color":"black"
}
dict2={
    "model":"Toyota",
    "color":"red"
}
merged = {f"dict1_{key}": value for key, value in dict1.items()}
merged.update({f"dict2_{key}": value for key, value in dict2.items()})
print(merged)

#Task 4
tup=("robotics","database")
print("Tuple: ",tup)
item="AI"
newtup=tup+(item,)
print("New tuple: ",newtup)

#Task 5
tup2=("apple",1,True,1.23,'C')
print("Tuple with different data types: ", tup2)

#Task 6
list1=[1,2,4,7,8]
print("Gven list is: ",list1)
list2=sum(list1)
print("Sum of list is: ",list2)

#Task 7
print("The largest number in the list is: ",max(list1))

#Task 8
thisset={"cherry","banana","apples"}
item2="blossom"
print("The given set elements: ",thisset)
print("item added: ",item2)
thisset.add(item2)
print("New set: ",thisset)

#Task 9
import array as arr
arr1 = arr.array('d', [6.78])
arr1.append(8.9)
arr1.append(7.0)

print("Original Array: ", arr1)
arr1.reverse()
print("Reversed Array: ", arr1)

#Task 10
array2=arr.array('i',[1,2,3,4,5])
print("Array provided: ",array2)
print("Element at index 0:", array2[0])
print("Element at index 1:", array2[1])
print("Element at index 2:", array2[2])
print("Element at index 3:", array2[3])
print("Element at index 4:", array2[4])