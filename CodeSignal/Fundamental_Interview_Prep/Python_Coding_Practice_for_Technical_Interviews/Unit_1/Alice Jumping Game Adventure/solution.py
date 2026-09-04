def solution(roadA, roadB):
    # Declare starting vars: result, indexes
    result = []
    indexA = 0
    indexB = 0

    # look at each index, and loop the game for each index
    for start_node in range(len(roadA)):
        # create variables that refresh for each game within the index
        curr_total_dist = 0
        visited = set()
        has_visited = False
        curr_step = 0
        position = start_node
        visited.add((position, "A"))  # add the starting node before each run
        while has_visited is not True:
            if curr_step == 0:  # roadA
                indexB = roadA[
                    position
                ]  # look at value of index 0 -> value is 1 -> jump to 1 index in B, so indexB = 1 for jump sequence
                if (
                    (indexB, "B")
                ) in visited:  # before jumping, check if it exists in set and increment dist by 1
                    curr_total_dist += 1
                    has_visited = True
                else:
                    visited.add((indexB, "B"))
                    curr_total_dist += 1
                    position = indexB  # update new position
                    curr_step = 1  # switch to roadB
            elif curr_step == 1:  # roadB
                indexA = roadB[
                    position
                ]  # look at value of index 1 within b -> value is 0 -> jump to 0 index in A, so indexA = 0 for jump sequence
                if ((indexA, "A")) in visited:  # repeat logic
                    curr_total_dist += 1
                    has_visited = True
                else:
                    visited.add((indexA, "A"))
                    curr_total_dist += 1
                    position = indexA
                    curr_step = 0

        result.append(
            curr_total_dist
        )  # every iteration, append curr_total_dist after loop runs

    return result
