# Bucket sort involves creating empty buckets, distributig elements into the appropriate buckets, sorting each bucket individually (typically with insertion sort), and then concatenating the sorted buckets


def bucket_sort(arr):
    n = len(arr)
    buckets = [[] for _ in range(n)]  # 1. Create n empty buckets

    # 2. Put array elements in diff buckets
    for num in arr:
        bi = int(n * num)  # Calculate index
        buckets[bi].append(num)

    # 3. Sort individual buckets
    for bucket in buckets:
        bucket.sort()  # Using Python's built in sort is efficent here

    # 4. Concatenate all buckets
    return [num for bucket in buckets for num in bucket]


# example usage
arr = [0.78, 0.17, 0.39, 0.26, 0.72]
print(f"Sorted array: {bucket_sort(arr)}")
