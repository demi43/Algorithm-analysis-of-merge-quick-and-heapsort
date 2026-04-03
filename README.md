# Algorithm Design Block
#
# Overview:
# We tested three advanced sort algorithms — Mergesort, Quicksort, and Heapsort —
# across four array sizes (n = 1000, 10000, 100000, 1000000) and three input
# types (Random, Increasing, Decreasing), for 12 total variations per algorithm.

# Mergesort — O(n log n) best, average, and worst case:
#   Mergesort always splits the array exactly in half regardless of the values,
#   so its comparison count is essentially the same across all three input types
#   for a given n. The Increasing and Decreasing cases are actually slightly
#   lower than Random because already-ordered merge runs require fewer comparisons
#   per merge step. Overall the counts scale predictably with n*log2(n).

# Quicksort — O(n log n) average,best, O(n^2) worst case:
#   On Random data, Quicksort performs comparably to Mergesort (~n log n).
#   On Increasing and Decreasing data, however, the last-element pivot is always
#   the maximum or minimum of the subarray, creating maximally unbalanced
#   partitions of size (n-1) and 0 at every level. This is the textbook worst
#   case. The quadratic behavior is directly visible in the output: at n=1000
#   on sorted data, Quicksort makes exactly 499,500 comparisons — precisely
#   n*(n-1)/2 — compared to roughly 10,000-11,000 for random input. At n=10,000
#   it reaches ~49,995,000 comparisons. For n=100,000 and n=1,000,000 on sorted
#   input, the recursion depth exceeds Python's stack limit and results in a
#   Stack Overflow Error (SOE). This confirms that Quicksort's quadratic worst
#   case is not merely theoretical — it is reproducible and measurable.

# Heapsort — O(n log n) best, average, and worst case:
#   Heapsort never degrades to quadratic behavior. Its comparison counts are
#   consistent across all input types for a given n, though generally higher
#   than Mergesort because each sift-down traverses a full heap path and the
#   access pattern is less cache-friendly. No SOE risk since it is iterative.

# Conclusion:
#   After testing all 12 variations, Mergesort offers the most predictable and
#   consistent performance. Heapsort is reliable but makes more comparisons in
#   practice. Quicksort is fastest on random data but catastrophically slow on
#   sorted input with a naive last-element pivot — the n*(n-1)/2 comparison
#   count and SOE results confirm the O(n^2) worst case is real and significant.
#   A random pivot or median-of-three strategy would eliminate this vulnerability.

# ALGORITHM 1: Mergesort(arr)
#     Input: Array of size n
#     Output: Sorted array and count of comparisons
#     1. If length of arr > 1:
#     2.    mid = length / 2
#     3.    L = arr[0...mid], R = arr[mid...n]
#     4.    Mergesort(L), Mergesort(R)
#     5.    While i < len(L) and j < len(R):
#     6.       Increment comparison_count
#     7.       If L[i] < R[j]: arr[k] = L[i]; i++
#     8.       Else: arr[k] = R[j]; j++
#     9.    Append remaining elements from L and R to arr

# ALGORITHM 2: Quicksort(arr, low, high)
#     Input: Array, starting index low, ending index high
#     Output: Sorted array and count of comparisons
#     1. If low < high:
#     2.    pivot_index = Partition(arr, low, high)
#     3.    Quicksort(arr, low, pivot_index - 1)
#     4.    Quicksort(arr, pivot_index + 1, high)
    
#     SUB-ALGORITHM Partition(arr, low, high):
#     1. pivot = arr[high]
#     2. For j from low to high - 1:
#     3.    Increment comparison_count
#     4.    If arr[j] <= pivot: swap arr[i] and arr[j]; i++
#     5. Swap arr[i+1] and arr[high]
#     6. Return i + 1

# ALGORITHM 3: Heapsort(arr)
#     Input: Array of size n
#     Output: Sorted array and count of comparisons
#     1. Build Max-Heap: For i from n/2 down to 0: Heapify(arr, n, i)
#     2. Extract: For i from n-1 down to 1:
#     3.    Swap arr[0] and arr[i]
#     4.    Heapify(arr, i, 0)
    
#     SUB-ALGORITHM Heapify(arr, n, i):
#     1. largest = i, left = 2i + 1, right = 2i + 2
#     2. If left < n: Increment comparison_count; If arr[left] > arr[largest]: largest = left
#     3. If right < n: Increment comparison_count; If arr[right] > arr[largest]: largest = right
#     4. If largest != i: Swap arr[i] and arr[largest]; Heapify(arr, n, largest)

# ALGORITHM: RandomIntegers(arr, size)
#     INPUT: Array name 'arr', integer 'size'
#     OUTPUT: 'arr' populated with random values
#     1. For i from 0 to size - 1:
#     2.    arr[i] = GENERATE random integer between 1 and 1,000,000
#     3. Return arr

# ALGORITHM: IncreasingIntegers(arr, size)
#     INPUT: Array name 'arr', integer 'size'
#     OUTPUT: 'arr' populated with 1 to size
#     1. For i from 0 to size - 1:
#     2.    arr[i] = i + 1
#     3. Return arr

# ALGORITHM: DecreasingIntegers(arr, size)
#     INPUT: Array name 'arr', integer 'size'
#     OUTPUT: 'arr' populated with size down to 1
#     1. For i from 0 to size - 1:
#     2.    arr[i] = size - i
#     3. Return arr

# ALGORITHM: PopulateSelectedArrays(choice)
#     INPUT: User choice (1, 2, or 3)
#     1. Define sizes = [1000, 10000, 100000, 1000000]
#     2. For each n in sizes:
#     3.    If choice is 1: 
#     4.       data[n] = RandomIntegers(empty_list, n)
#     5.    Else If choice is 2: 
#     6.       data[n] = IncreasingIntegers(empty_list, n)
#     7.    Else If choice is 3: 
#     8.       data[n] = DecreasingIntegers(empty_list, n)
#     9. Print "Arrays Populated"

# Note: i tried increasing my recursion setlimit but it just caused a long and maybe unending wait time due to it trying to sort quick sort so i believe my recursion limit is probably set lower thanm 1000 
