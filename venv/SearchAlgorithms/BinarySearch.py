
"""
Binary Search Algorithm

Search a sorted list by halving it to see if target # is bigger or smaller than the median

repeat until target found

Time cost spoken of as the common question:

" How many times must we double 1 before we get to n OR how many times must be divide n in order to get back down to 1"
"""

def binary_search(target, nums):

    """ See if target appears in nums """

    # we think of floor_index and ceiling_index as "walls" around
    # the possible positions of our target so by -1 below we mean
    # to start our wall "to the left" of the 0th index
    # we *don't* mean "the last index

    floor_index = -1
    ceiling_index = len(nums)

    # If there isn't at least 1 index between floor and ceiling,
    # we've run out of guesses and the number must not be present

    while floor_index + 1 < ceiling_index:
        # Find the index ~halfway between the floor and ceiling
        # we use integer division, so we'll never get a "half index"

        distance = ceiling_index - floor_index
        half_distance = distance // 2 # // is the "Floor Division" operator that divides and returns the integer value of the quotient. It dumps digits after the decimal
        guess_index = floor_index + half_distance # this is where the -1 is important, placing it to the left

        guess_value = nums[guess_index]
        if guess_value == target:
            return True

        if guess_value > target:
            # if the guess value is greater, the target is to the left, so we move the ceiling to the left
            ceiling_index = guess_index
        else:
            # Target is to the right, so move floor to the right
            floor_index = guess_index



        return False


"""

Time cost = O(log2n)

- only non-constant part is # of times the while loop runs

Solve:

1) n * (1/2)^x = 1
2) minimize to n: = 2^x
3) Take log of both slides: log2n = log2(2^x)
4) log2n = x

A: O(log2n)

"""