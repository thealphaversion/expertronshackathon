def merge_lists(list1, list2):
    merged_list = []
    for value in list1:
        if value not in list2:
            merged_list.append(value)
    
    for value in list2:
        if value not in list1:
            merged_list.append(value)

    return merged_list

if __name__ == "__main__":
    A = ["Raj", "Pankaj", "Shreyas"]
    B = ["Sandeep", "Vikas", "Raj"] 

    C = ["A", "B", "C"]
    D = ["D", "E", "F"]

    result = merge_lists(A, B)
    second_result = merge_lists(C, D)
    print(result)
    print(second_result)