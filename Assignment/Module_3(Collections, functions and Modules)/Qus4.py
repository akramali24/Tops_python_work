'''Python function to get the largest number, smallest num and sum of all from a list.'''

def largest_smallest_sum(in_list):
    
    largest_num=in_list[0]
    smallest_num=in_list[0]
    

    for num in in_list:
        if num > largest_num:
            largest_num=num
        elif num < smallest_num:
            smallest_num = num
            
    total_sum = sum(in_list)
    
    print(f"largest in the in_list : {largest_num}")
    print(f"smallest in the in_list : {smallest_num}")
    print(f"sum of all number in_list : {total_sum}")
    
my_list=[-1,-2,-5,10,25,0,100]
largest_smallest_sum(my_list)