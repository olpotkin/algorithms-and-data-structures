
def insertion_sort(nums):
    for i in range(len(nums)):
        j = i
        while j > 0 and nums[j-1] > nums[j]:
            swap(nums, j, j-1)
            j -= 1
    return nums


def swap(nums, i, j):
    temp = nums[i]
    nums[i] = nums[j]
    nums[j] = temp


if __name__ == "__main__":
    nums = [-4, 56, 1, 3, 5, 63, 12, 4, -11, 234]
    print(insertion_sort(nums))
