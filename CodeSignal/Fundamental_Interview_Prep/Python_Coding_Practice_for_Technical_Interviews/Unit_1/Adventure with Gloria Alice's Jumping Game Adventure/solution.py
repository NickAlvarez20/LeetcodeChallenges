def solution(arrayA, arrayB):
    # create variables for index_A, hops and visited list
    index_A = 0
    hops = []  #
    visited = []

    # 1. Start a while loop that checks if index_A has been visited
    # need a list of all the values in arrayA that tell me where to jump in arrayB

    while index_A not in visited:
        visited.append(index_A)
        jump_to_B = arrayA[index_A]  # value from arrayA
        hops.append(jump_to_B)  # append this hop to the list
        jump_to_A = (
            arrayB[jump_to_B - 1] - 1
        )  # grab current value for index jump to A, based on value extracted during first jump
        index_A = jump_to_A

    return hops

    # so value at arrayA, determines the index it jumps to in B
    # so if A had 4, in B i just to index 4
    # now we i get to index 4 in B i check the value in B
    # then i use that value to jump back to A
    # the exit condition is when the character lands on an indexA that it has already visited

    # so i need to keep track of all the indices in A
    # so first upon starting i append the indexA to visited
    # next i need to update my move in array B, so i need the value extraction from A using the current index or arrayA[index_A]
    # so this becomes position
