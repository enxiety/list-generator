i1 = input("First list object: ")
i2 = input("Second list object: ")
i3 = input("Third list object: ")
i4 = input("Fourth list object: ")
i5 = input("Fifth list object: ")
is_list = True

# this is just for error demonstration
# typing error in the first input will cause the list to go invalid
if i1 == "error":
    is_list = False
    print("Invalid List")
    exit(0)


list1 = [i1, i2, i3, i4, i5]
if not is_list:
    print("Invalid list")
else:
    print("List generation complete")

if list1:
    print(list1)
else:
    print("List generation failed")
