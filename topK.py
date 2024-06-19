def topK(nums, k):
    temp_dict = dict()

    for number in nums:
        if number in temp_dict:
            temp_dict[number] += 1
        else:
            temp_dict[number] = 1

    my_list = sorted(temp_dict.items(), key=lambda x: x[1], reverse=True)
    
    to_return = []
    for i in range(k):
        to_return.append(my_list[i][0])
    return to_return    

print(topK([1,2,2,3,3,3], 2))