'''
I make an improvement on the bubble sort algorithm.
While it is well known that you do not have to iterate to the end of the list each time, it is
also better if you do not start at the beginning of the list for each iteration unless it is necessary.

If you have a list of length n that you wish to sort, and the first switch you need to make is at element x, then
the iteration for each run of the algorithm can never be larger than (n-1) - (x-1) = n - x

'''


# ORIGINAL BUBBLE SORT
def bubble_sort_1(a_list):
    count = 0
    list_length = len(a_list) - 1
    for i in range(list_length):
        no_swaps = True
        for j in range(list_length):
            count = count + 1
            if a_list[j] > a_list[j+1]:
                a_list[j], a_list[j+1] = a_list[j+1], a_list[j]
                no_swaps = False
        if no_swaps:
            print(f"Sample list of length {len(a_list)} made {count} comparisions in the original bubble sort.")
            return 
    print(f"Sample list of length {len(a_list)} made {count} comparisions in the original bubble sort.")
    return 


# KNOWN IMPROVEMENT WHERE YOU DON'T GO TO THE END EACH TIME
def bubble_sort_2(a_list):
    count = 0
    list_length = len(a_list) - 1
    for i in range(list_length):
        no_swaps = True
        for j in range(list_length - i):
            count = count + 1
            if a_list[j] > a_list[j+1]:
                a_list[j], a_list[j+1] = a_list[j+1], a_list[j]
                no_swaps = False
        if no_swaps:
            print(f"Sample list of length {len(a_list)} made {count} comparisions in the bubble sort with the well-known improvement.")
            return
    print(f"Sample list of length {len(a_list)} made {count} comparisions in the bubble sort with the well-known improvement.")          
    return 

# MY IMPROVEMENT FOR BUBBLE SORT
def bubble_sort_3(a_list):
    count = 0
    start_at = 0
    list_length = len(a_list) - 1
    for i in range(list_length):
        no_swaps = True
        #start_at = 0
        start_at_set = 'no'
        for j in range(start_at,list_length - i):
            count = count + 1
            #start_at = 0
            if a_list[j] > a_list[j+1]:
                if start_at_set == 'no':
                    if j > 0:
                        start_at = j - 1
                    #else:
                        #start_at = j
                        #start_at = 0
                    start_at_set = 'yes'
                a_list[j], a_list[j+1] = a_list[j+1], a_list[j]
                no_swaps = False
        if no_swaps:
            print(f"Sample list of length {len(a_list)} made {count} comparisions in the bubble sort with the new improvement.")
            return 
    print(f"Sample list of length {len(a_list)} made {count} comparisions in the bubble sort with the new improvement.")
    return 





# Create three lists unordered lists for testing.
my_list = [2,3,4,10,6,7,8,9,5,1]
my_list_2 = [7,9,12,22,35,36,37,38,40,41,42,43,45,46,91,90,2,55,50,51]

#Create a list of 500 elements and switch some of the elements so that the list is out of order.
def createList(r1, r2):
    return [item for item in range(r1, r2+1)]
     
r1, r2 = 1, 500
my_list_3 = createList(r1, r2)
my_list_3[4], my_list_3[7] = my_list_3[7], my_list_3[4]
my_list_3[45], my_list_3[17] = my_list_3[17], my_list_3[45]
my_list_3[61], my_list_3[9] = my_list_3[9], my_list_3[61]
my_list_3[322], my_list_3[401] = my_list_3[401], my_list_3[322]




#Run each of the three functions for lists of three different lengths to get sample results.

bubble_sort_1(my_list[:])
bubble_sort_2(my_list[:])
bubble_sort_3(my_list[:])

print("\n")
bubble_sort_1(my_list_2[:])
bubble_sort_2(my_list_2[:])
bubble_sort_3(my_list_2[:])

print("\n")
bubble_sort_1(my_list_3[:])
bubble_sort_2(my_list_3[:])
bubble_sort_3(my_list_3[:])






