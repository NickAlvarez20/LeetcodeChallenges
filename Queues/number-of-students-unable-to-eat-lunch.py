# Intuition: The main intuition for this problem is seeing the exact word stack and queue within the problem Another thing is to be aware of a condition that arises if you loop through the entire queue and the condition that requires you to exit the loop does not exist then you need to account for that With a counter. Another key idea is to use the DQ data structure that is optimized in Python and have an understanding of how that method works where you pop the left and you have to store it in a variable in order append it to the end. Last thing is to be aware of braking conditions within your loops of a certain condition arises you need to break out of the loop like if we see at the end if all the logic goes through and then we check if counter skipped equals length of students Q then we need a break because we have not found a condition that will allow us to traverse through and implement the algorithm correctly. 

# Approach:
# 1. First we call current student declare a variable and set it equal to an empty stack/queue
# 2. Next we declare students queue and sandwiches queue and set them equal to a DQ using the list of students and sandwiches as the parameters for the argument of the method DQ
# 3. Next we declare a counter skipped variable and set it equal to zero 
# 4. Now we must traverse the students queue so we use a while loop and while it has entries within it 
# 5. we do a conditional check to see if the first element within the student's queue is equal to the first element within the sandwich's queue 
# 6. If the condition is true then we can pop the left element from the students and sandwiches queue thus removing them entirely and resetting counter skipped equal to 0 because we have found a sandwich that matches the students preference 
# 7. Next we will do an else condition.
# 8. We update the current student variable that we set equal to an empty stack earlier and we will update it with the element that we are popping from the stud Here we need this as a variable storage 
# 9. Next we will append that current student variable that's holding the value from the students and we'll append it to the end of the student's queue properly updating the queue by rotating the student who didn't receive the sandwich to the end of the line
# 10. We then update counterscript plus equals 1 This essentially says that the student has skipped the sandwich and we need to update the counterskip to keep track of this that way we can be aware of the condition that arises when no student has taken the sandwich and we have a impossible condition that will reduce the size of the students and sandwiches Q 
# 11. We want to add in one last conditional check within this At the end of each edition we want to check if counterskipped equals the length of students queue This will say that we look through the entire sandwiches and students and none of them wanted the sandwich. Then we will break out of the loop
# 12. Finally we will return the length of the students queue. 
# Complexity:
# Time: O(n) or O(N^2)
# The time complexity is linear where N is the total number of students which is the same as the total number of sandwiches. The time complexity is linear where N is the total number of students which is the same as the total number of sandwiches. In the worst case scenario the outer while loop runs all until all students have been served or a deadlock is reached. Each student who eventually gets a sandwich causes one iteration where both cues are popped and the counter skipped is reset . Students who initially prefer the other type of sandwich are moved to the back of the queue and O of one operation for a dequeue a student will only circulate around the queue of maximum number of in times before idegating their sandwich or being a part of the group that cannot be served. The total number of queue operations pops appends across the entire execution remains proportional to N
#
# Space: O(n)
# Space complexity is also linear two separate DQ data structures are used to store the students and sandwiches each potentially holding up to N elements initially. With space required grows in direct proportion to the initial size of the input list. 
#


from collections import deque


class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        current_student = []
        students_queue = deque(students)
        sandwiches_queue = deque(sandwiches)
        counter_skipped = 0
        while students_queue:
            if students_queue[0] == sandwiches_queue[0]:
                students_queue.popleft()
                sandwiches_queue.popleft()
                counter_skipped = 0
            else:
                current_student = students_queue.popleft()
                students_queue.append(current_student)
                counter_skipped += 1
                if counter_skipped == len(students_queue):
                    break

        return len(students_queue)
