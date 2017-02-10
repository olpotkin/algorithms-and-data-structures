
def merge_sort(nums):
    if len(nums) == 1:
        return

    mid_index = len(nums) // 2

    left_half = nums[:mid_index]
    right_half = nums[mid_index:]

    merge_sort(left_half)
    merge_sort(right_half)

    i = 0
    j = 0
    k = 0

    while i < len(left_half) and j < len(right_half):
        if left_half[i] < right_half[j]:
            nums[k] = left_half[i]
            i += 1
        else:
            nums[k] = right_half[j]
            j += 1
        k += 1

    while i < len(left_half):
        nums[k] = left_half[i]
        k += 1
        i += 1

    while j < len(right_half):
        nums[k] = right_half[j]
        k += 1
        j += 1


if __name__ == "__main__":
    nums = [-4, 56, 1, 3, 5, 63, 12, 4, -11, 234]
    merge_sort(nums)
    print(nums)
