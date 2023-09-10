numbers1 = [64, 34, 25, 12, 22, 11, 90]
print("Original array:", numbers1)
def bubble_sort(arr):
    n = len(arr)
    
    # Traverse through all array elements
    for i in range(n):
        # Last i elements are already in place
        for j in range(0, n - i - 1):
            # Swap if the element found is greater than the next element
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]

number2=bubble_sort(numbers1)
print("Sorted array:", number2)
