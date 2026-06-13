def quick_sort(arr):
    """使用快速排序算法返回一个新的有序列表。"""
    if len(arr) <= 1:
        return arr

    pivot = arr[len(arr) // 2]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]

    return quick_sort(left) + middle + quick_sort(right)


if __name__ == "__main__":
    nums = [3, 6, 8, 10, 1, 2, 1]
    sorted_nums = quick_sort(nums)
    print(sorted_nums)
