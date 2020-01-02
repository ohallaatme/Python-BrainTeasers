"""
Merge Sort

Idea is to divide the list in half, sort the halves,
then merge two sorted halves back into one

"""

def merge_sort(list_to_sort):

    # Base case: list with fewer than 2 elements are sorted
    # Base case returns a vlaue without making any subsequent recursive calls
    if len(list_to_sort) < 2:
        return list_to_sort

    # Step 1 - divide the list in half
    # We use integer division (// operator) so we do not get a "half index"

    mid_index = len(list_to_sort) // 2
    left = list_to_sort[:mid_index]
    right = list_to_sort[mid_index:]


    # Step 2 - Sort each half
    ## RECURSIVE
    sorted_left = merge_sort(left)
    sorted_right = merge_sort(right)

    # Step 3 - merge the sorted halves
    sorted_list = []
    current_index_left = 0
    current_index_right = 0


    # sorted_left's first element comes next
    # if it's less than sorted_right's first
    # element or if sorted_right is exhuasted

    while len(sorted_list) < len(left) + len(right):
        if ((current_index_left < len(left)) and
                (current_index_right == len(right) or
                 sorted_left[current_index_left] < sorted_right[current_index_right])):
            sorted_list.append(sorted_left[current_index_left])
            current_index_left += 1
        else:
            sorted_list.append(sorted_right[current_index_right])
            current_index_right += 1
    return sorted_list


"""
Time complexity: O(nlog2n)

log2n comes from the number of times we have to cut n in half to get down to sublists of just 1 element (base case)

The additional n comes from the time cost of merging all n items together each time we merge to sorted sublists

Note: in computer science, it's usually implied that the base is 2, so log n generally means log2n - special notation:

lg n or n log n for sorting



differs from other maths where base is implied as 10 or the special constant e (natural log)


In big O notation, base is considered a constant, so we say O(log n) vs O(log2n)

"""

