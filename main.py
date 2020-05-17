def insert_sort(nums):
    for index in range(1, len(nums)):
        num = nums[index]
        hole = index
        while hole > 0 and num < nums[hole - 1]:
            nums[hole] = nums[hole - 1]
            hole -= 1
        nums[hole] = num
    return nums


def select_sort(nums):
    for index in range(len(nums) - 1):
        for i in range(index + 1, len(nums)):
            if nums[i] < nums[index]:
                nums[index], nums[i] = nums[i], nums[index]
    return nums


def bubble_sort(nums):
    for i in range(len(nums) - 1):
        for j in range(len(nums) - i - 1):
            if nums[j] > nums[j + 1]:
                nums[j + 1], nums[j] = nums[j], nums[j + 1]
    return nums


def bubble_sort_op(nums):
    last_index = len(nums)
    while last_index > 0:
        cur_index = 0
        last_index = 0
        while cur_index + 1 < last_index:
            if nums[cur_index + 1] < nums[cur_index]:
                nums[cur_index + 1], nums[cur_index] = nums[cur_index], nums[cur_index + 1]
                last_index = cur_index
            cur_index += 1
    return nums


def partition(nums, left, right):
    key = nums[left]
    while left < right:
        while left < right and key <= nums[right]:
            right -= 1
        nums[left] = nums[right]
        while left < right and key >= nums[left]:
            left += 1
        nums[right] = nums[left]
    return left


def qsort_internal(nums, start, end):
    if start < end:
        index = partition(nums, start, end)
        qsort_internal(nums, start, index - 1)
        qsort_internal(nums, index + 1, end)


def qsort(nums):
    qsort_internal(nums, 0, len(nums) - 1)
    return nums


def merge(nums, start, middle, end):
    left = start
    right = middle + 1
    nums_list = []
    while left <= middle and right <= end:
        if nums[left] <= nums[right]:
            nums_list.append(nums[left])
            left += 1
        else:
            nums_list.extend(nums[right])
            right -= 1
    if left <= middle:
        nums_list.extend(nums[left:middle+1])
    elif right <= end:
        nums_list.extend(nums[right:end+1])
    nums[start:end + 1] = nums_list


def merge_sort_internal(nums, start, end):
    if start < end:
        middle = int((start + end) / 2)
        merge_sort_internal(nums, start, middle)
        merge_sort_internal(nums, middle + 1, end)
        merge(nums, start, middle, end)


def merge_sort(nums):
    merge_sort_internal(nums, 0, len(nums) - 1)
    return nums


def down_adjust(nums, parent, num_len):
    child = 2 * parent + 1
    while child < num_len:
        if child + 1 < num_len and nums[child + 1] > nums[child]:
            child += 1
        if nums[parent] >= nums[child]:
            break
        nums[child], nums[parent] = nums[parent], nums[child]
        parent = child
        child = 2 * child + 1


def heap_sort(nums):
    index = len(nums) // 2 - 1
    while index >= 0:
        down_adjust(nums, index, len(nums))
        index -= 1

    for index in range(len(nums) - 1):
        last_index = len(nums) - index - 1
        nums[0], nums[last_index] = nums[last_index], nums[0]
        down_adjust(nums, 0, last_index)
    return nums


def count_sort(nums):
    min_num = min(nums)
    count = max(nums) - min_num

    count_list = [0] * (count + 1)

    for num in nums:
        count_list[num - min_num] += 1

    sum_num = 0
    for index in range(len(count_list)):
        sum_num += count_list[index]
        count_list[index] = sum_num

    sort_list = [0] * len(nums)
    for num in nums[::-1]:
        sort_list[count_list[num - min_num] - 1] = num
        count_list[num - min_num] -= 1
    return sort_list


def bucket_sort(nums, bucket_interval=10, sort_func=heap_sort):
    min_val, max_val = min(nums), max(nums)
    buckets = [[] for _ in range(((max_val - min_val) // bucket_interval + 1))]
    for num in nums:
        index = (num - min_val) // bucket_interval
        buckets[index].append(num)
    nums.clear()
    for bucket in buckets:
        sort_func(bucket)
        nums.extend(bucket)
    return nums


def radix_sort(nums, radix=10):
    max_len = len(str(max(nums)))
    index = 0
    while index < max_len:
        buckets = [[] for _ in range(radix)]
        for num in nums:
            buckets[(num // (radix ** index)) % radix].append(num)

        nums.clear()
        for bucket in buckets:
            nums.extend(bucket)
        index += 1

    return nums


num_list = [-10, -4, -5, -122, 4, 26, 33, 56, 2, 36, 1, 56, 7, 12, 35]
print('insert_sort: ', insert_sort(num_list))
print('select_sort: ', select_sort(num_list))
print('bubble_sort_op: ', bubble_sort_op(num_list))
print('bubble_sort: ', bubble_sort(num_list))
print('qsort: ', qsort(num_list))
print('merge_sort: ', merge_sort(num_list))
print('heap_sort: ', heap_sort(num_list))
print('count_sort: ', count_sort(num_list))
print('bucket_sort: ', bucket_sort(num_list))
print('radix_sort: ', radix_sort(num_list, 10))