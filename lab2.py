# car=["ford","BMW","mercedese"]

# car[0]="toyota"

# car.append("Honda")

# car.remove("toyota")

# x=len(car)

# print(car)

# list1=['physics','chemistry',1997,2000]
# list2=[6,5,4,3,2,1]
# list3=["a","b","c","d"]

# print ("list[0]: ",list1[0])
# print("list2[1:5]: ", list2[1:5])

# print("Value at index 2: ", list2[1])
# list2[1]=1997
# print("Value at index 2: ", list2[1])

# del list1[2]

# print("list1: ",list1)

# print(len([1,2,3]))

# print([1,2,3]+[4,5,6])
# print(['Hi!']*4)
# print(3 in[1,2,3])
# for x in [1,2,3]:print(x)

# L=['spam','Spam','SPAM!']
# print(L[2])
# print(L[-2])
# print(L[1:])

# print(len(list1))
# print(max(list2))
# print(min(list2))
# print(list1.count("physics"))
# print(list1.index("physics"))
# print(list2.reverse())

# tup1 = ('physics', 'chemistry',
# 1997, 2000); tup2 = (1, 2, 3, 4, 5
# ); tup3 = "a", "b", "c", "d";
# tup4=tup1+tup2
# print(tup4)

# list1.reverse()
# list2.sort()
# list1.insert(4,10001)
# print(list2)
# print(list1)

# thisset={"apple","banana","cherry"}
# print(thisset)
# thisset.add("orange")
# print(thisset)
# print(len(thisset))
# thisset.remove("banana")
# print(thisset)
# thisset.discard("cherry")
# print(thisset)
# thisset.pop()
# print(thisset)
# thisset.clear()
# print(thisset)

# thisdict={
#     "model":"Mustang",
#     "brand":"Ford",
#     "year":1964
# }
# print(thisdict)
# x=thisdict["model"]
# print(x)
# x=thisdict.get("year")
# print(x)
charset = ('0', '1')  # Define the valid character set
dictionary = {        # Define the state transitions of the DFA
    "q0": {"0": "q1", "1": "q0"},
    "q1": {"0": "q1", "1": "q2"},
    "q2": {"0": "q2", "1": "q2"},
}

# Function to check if the input string is valid according to the DFA
def is_valid_string(s):
    current_state = "q0"  # Start state
    for char in s:
        if char not in charset:  # Check if the character is in the valid charset
            return False
        current_state = dictionary[current_state][char]  # Transition to the next state

    # The string is valid if it ends in state "q2"
    return current_state == "q2"

# Input from the user
s2 = str(input("Enter a string: "))

# Check if the string is valid and print the result 
if is_valid_string(s2):
    print("True")  # The string matches the regular expression
else:
    print("False")  # The string does not match the regular expression
