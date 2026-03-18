# Intuition: To identify the intuition we need to identify the core aspects of building out a has the hash set it acts like a set so it remove duplicates and it also uses a hash function. So we're going to need a size and we want to make sure our house set avoids collisions by using buckets and a prime number for the size When we use modulo operation for the hash that this will ensure efficient hash function is created with prime mathematics. In order to create the hash function you need to do the key modulo operator size for each specific instance of a created hash set. The other key components are the ad remove and contains methods that we'll be designing The key components that are universal is using index with the hash function to identify the correct hash key The next part is constant access to the buckets using the index that we received after calling the hash function then we need a be aware that this will access the nested bucket within it so then we can use the key that we are plugging in calling to check for its existence for the ad if it does not exist we are going to update it otherwise we don't want to update it since it is acting like a hashtag for the delete method we'd want to identify it and if we do identify we can use the dot remove method with the key within that bucket to remove it Then the last method is contains very similar logic Use the index hash function Check the and if has the key we can return true but we also need to explicitly return false

# Approach:
# 1. First thing we want to do is set up the warehouse with the initialization of the Python class constructor method in it we want to declare that each half set has a given size with a prime value and we also want to create the buckets for the size so that we avoid collisions 
# 2. Next method for our hash set is to create the hash function itself We simply take the key and divide it with the modulo operator by the size of any given hashset
# 3. Next we create the add method We use index variable and set it equal to self and call the hash function with any given key We also declare a bucket variable and set that equal to self buckets Using bracket notation we can in the index in order to identify the correct bucket using constant access This will allow us to update the bucket with the correct index Finally we check if key not in that specific bucket then we will add the key to that bucket
# 4. Very similar logic for the remove method we once again declare index and bucket using the same logic we check if the key is in the bucket this time and if it is we can use the remove method to remove that specific key 
# 5. Last method is the contains method using the same logic we create the index call the hash function create the bucket plug in the index that we have created into self top buckets Then we check if key in that bucket we're going to explicitly return true otherwise we will explicitly return false
# Complexity:
# Time: O(1)
# The magic of a Hash Set is its speed, but because we use buckets (lists) to handle collisions, there are two ways to look at the time.
# Average Case: 
#  (Constant Time)
# If your _hashfunc distributes keys evenly, each bucket will only have 0 or 1 item.
# Finding the index, jumping to the bucket, and checking for the key happens almost instantly, regardless of how many items you've stored.
# Worst Case: 
#  (where 
#  is the number of buckets)
# If you add 10,000 items and you only have 1,009 buckets, some buckets will inevitably hold multiple items.
# In the absolute worst case (e.g., all keys are multiples of 1009), every item ends up in the same bucket. At that point, add, remove, and contains become because you have to scan a regular list.
# add	
#  avg	Hashing + appending to a small bucket list.
# remove	
#  avg	Hashing + removing from a small bucket list.
# contains	
#  avg	Hashing + a quick in check on a small list.
#
# Space: O(K+M)
# Space complexity measures how much memory your data structure consumes as you add more data.
# Complexity: 
# K is the number of predefined buckets (your self.size = 1009). You "pay" for this space as soon as you initialize the class.
# M is the number of unique elements you actually insert into the set.
# In LeetCode terms: We usually simplify this to O(N), where N is the number of possible unique values you might store.

class MyHashSet:

    def __init__(self):
        self.size = 1009
        self.buckets = [[] for _ in range(self.size)]

    def _hashfunc(self, key):
        return key % self.size

    def add(self, key: int) -> None:
        index = self._hashfunc(key)
        bucket = self.buckets[index]
        if key not in bucket:
            bucket.append(key)

    def remove(self, key: int) -> None:
        index = self._hashfunc(key)
        bucket = self.buckets[index]
        if key in bucket:
            bucket.remove(key)

    def contains(self, key: int) -> bool:
        index = self._hashfunc(key)
        bucket = self.buckets[index]
        if key in bucket:
            return True
        else:
            return False


# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)
