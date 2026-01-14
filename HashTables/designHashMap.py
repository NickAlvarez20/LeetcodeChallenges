class MyHashMap:
    def __init__(self):
        self.size = 1000
        self.table = [[] for _ in range(self.size)]

    def _hash_func(self, key):
        return key % self.size

    # updates the table
    def put(self, key: int, value: int) -> None:
        index = self._hash_func(key)
        # loop through each bucket and check if key exists in table, update old data with new, else append new object into table
        for i, (k, v) in enumerate(self.table[index]):
            if k == key:
                self.table[index][i] = (key, value)
                return
        self.table[index].append(key, value)

    def get(self, key: int) -> int:
        index = self._hash_func(key)
        for k, v in self.table[index]:
            if k == key:
                return v
        return -1

    def remove(self, key: int) -> None:
        index = self._hash_func(key)
        bucket = self.table[index]
        for i, pair in enumerate(bucket):
            if pair[0] == key:
                del bucket[i]
                return

    # Your MyHashMap object will be instantiated and called as such:
    # obj = MyHashMap()
    # obj.put(key,value)
    # param_2 = obj.get(key)
    # obj.remove(key)

# Intuition:
# Straightforward approach to implementing a hash table. We want to create a hash table with the initializer constructor in Javascript in it in Python which creates the hash table object we then set the size for the constraints to 1000 and then we set the construction of the table with a bucket implementation therefore we can prevent collisions and ensure chaining is possible with the initial structure So we create a variable self dot table when we initialize it into a list and then buckets within the list for the range of the entire size of the object which will be incrementally changed as needed but for this initial setup we do 1000. The next thing we want to do is create a hash function there is various ways we could do this using mathematical algorithms but for the sake of simplicity for this easy leak code problem we will implement it using the key divided by the self.size of any given hash table object creation. Then we want to create a method that updates the table so we are going to use the index and this will be the hash function that allows us to access an O of one time the index for any given key that we insert into the function Then we want to update by enumerating through the entire table index seeing if the key that exists within each bucket is equal to the then we can update the nested key value pairs that exist within the buckets if there are collisions and multiple values exist for any given key we want to update that based on the key otherwise we will simply add the new key value that we are inserting. The next thing we want to do is to get any given key value pair that within our hash table this will be an O of one access which is important for hash table implementations So like before we initialize an index with the hash function and any given key that we put into the function We then want to loop through the key values in the table within the buckets if the key is found we can return the value that is associated whether it be one or many different values otherwise we'll return -1. The final implementation is the remove method which follows the same kind of thinking we use the index to generate the position of the index that we are going to pass into the function So generate the index with the hash function create a bucket variable set it equal to the self table index this will be used for enumeration in the next 4 loop sequence for index pair and enumerate bucket so for key value pair in the bucket we want to see if the key is equal to the key that we have given it So this will be the keys that are associated with the buckets If we do find it we delete it at that specific index within the bucket.
#
# Approach:
# 1. So first we want to define what the structure of the hash map for any given object creation will look lies using the initialization Python object initializer we'll set the size to 1000 and then create the table attribute set that equal to list comprehension to create buckets for the entire range setting them first as empty buckets for the total range of the object size we have specified
# 2. Next we want to define the hash function which will be used with dividing the key modulo by the size This will create a unique hash function for any given index which is the main idea surrounding the hash table the hash function is one of the most important things that make a hash table A hash table will allow us to quickly access any given index based on an inserted key
# 3. Next we want to update the table with the put method that we are defining within our class AKA object We always want to start out initializing with the index and use the light using the hash function to specify based on any given key what index we will be utilizing for the function to search and update correctly within our hash table Then we enumerate through it using index value and value uses a tuple like structure to access the key value So the value is nested when we use that to enumerate the entire table all the buckets and then we see if the key is specified to the given key that we have inserted and then we can update that and if not we append it to the hash table
# 4. Then we define a Git method that allows us to retrieve the value of any given index based on the key So we once again initialize the index utilizing the hash function and insert the key as a parameter and then using the enumeration syntax we loop through the table by the index to get within the buckets and then we see if the key is equal to the key that was inserted and then we can return the values Now it's important to know that there could be multiple values if the hash table does have collisions otherwise if it does not exist we return -1
# 5. Then finally we define a remove method that once again initializes the index with the hash function and any given key that is inserted into the function itself Then we define a bucket variable and set that equal to the table index key therefore allows us to enumerate the buckets It's a way to make the code a little bit cleaner by defining the bucket and then we use enumeration syntax to look at the index in the pair in the bucket as there could be multiple that exist because of chaining and collisions so we enumerate and we check if the key of any given bucket we have and if it does then we can delete that bucket



# Time complexity: Hash Function - O(1) | Put Function - O(n) | Get Function - O(n) | Remove Function - O(n)
# The hash function is O of one since we are using a variable and simple mathematical operations. The put function is O of N since we are using enumeration to access and update and then appending since we need to look through the table this is O of N. The get function is O of N Because once again we are utilizing enumeration to go within the hash table. The remove function is O(N) since we are enumerating once again. Those are all worst case for the functions but for the most part it is going to be O of one It's important to note that the worst case will result in O but because of direct index access it is usually O 1 on average because we assume uniform hashing distribution

# Space complexity: O(N + K)
# 1. The overall space complexity is O of N + K where K is the fixed overhead of 1000 empty buckets and N is the total number of key value pairs actually stored As you call put the memory grows linearly with each unique key value pair added to the buckets Even with zero items your map consumes memory for one 1000 empty lists created and in it So space complexity is O of N + K

# Analysis: The analysis of this solution is 26MILLISECONDS and it beats 86.53% of all solutions the memory is 22.76 megabytes and it beats 33 91% of solutions this total combination places the solution within the top five percent
# Total time to solve: Total time to solve for this one was definitely a lot longer than expected about 1 to 2 hours to fully comprehend the creation the implementation from a basic hash table and the overall basic foundation to actually implementing one with class, Object syntax and initializing and understanding how to set up the hash function as well as how to implement the index within the git put and remove methods within our class for the hash table class that we have created as well as how to understand the size and table creation during the initialization of the object
# Alternative solutions
# 1. An alternative solution would be to implement a linked list and update the pointers this one is a little bit nuanced it does have some ways that it theoretically makes sense but it is definitely tougher to grasp at first when you're 1st learning and especially considering this is an easy problem
# 2. Another way to do this is not how it is supposed to be recommended you could do a simple return one liner for the any given index that one's also not recommended
# 3. You could also use a or dictionary
