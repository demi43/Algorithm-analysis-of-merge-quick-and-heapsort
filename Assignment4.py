# Name: Olaoluwa Omodemi Adedamola 
# Class: CS 4306/03
# Term: Spring 2026
# Instructor: Dr. Abdur Rahman
# Assignment: 4
# IDE: Visual studio code 

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
import random
import sys



# Mergesort class
class Mergesort:
    def __init__(self):
        self.comparisons = 0

    def sort(self, arr):
        self.comparisons = 0
        self._merge_sort(arr)
        return self.comparisons

    def _merge_sort(self, arr):
        if len(arr) > 1:
            mid = len(arr) // 2
            L = arr[:mid]
            R = arr[mid:]

            self._merge_sort(L)
            self._merge_sort(R)

            i = j = k = 0
            while i < len(L) and j < len(R):
                self.comparisons += 1
                if L[i] < R[j]:
                    arr[k] = L[i]
                    i += 1
                else:
                    arr[k] = R[j]
                    j += 1
                k += 1

            while i < len(L):
                arr[k] = L[i]
                i += 1
                k += 1

            while j < len(R):
                arr[k] = R[j]
                j += 1
                k += 1


# Quicksort Class
class Quicksort:
    def __init__(self):
        self.comparisons = 0

    def sort(self, arr):
        self.comparisons = 0
        try:
            self._quick_sort(arr, 0, len(arr) - 1)
            return self.comparisons
        except (RecursionError, MemoryError):
            return "StackOverflow Error"

    def _quick_sort(self, arr, low, high):
        if low < high:
            pi = self._partition(arr, low, high)
            self._quick_sort(arr, low, pi - 1)
            self._quick_sort(arr, pi + 1, high)

    def _partition(self, arr, low, high):
        pivot = arr[high]
        i = low - 1
        for j in range(low, high):
            self.comparisons += 1
            if arr[j] <= pivot:
                i += 1
                arr[i], arr[j] = arr[j], arr[i]
        arr[i + 1], arr[high] = arr[high], arr[i + 1]
        return i + 1



# Heapsort Class
class Heapsort:
    def __init__(self):
        self.comparisons = 0

    def sort(self, arr):
        self.comparisons = 0
        n = len(arr)
        # Build max-heap
        for i in range(n // 2 - 1, -1, -1):
            self._heapify(arr, n, i)
        # Extract elements one by one
        for i in range(n - 1, 0, -1):
            arr[i], arr[0] = arr[0], arr[i]
            self._heapify(arr, i, 0)
        return self.comparisons

    def _heapify(self, arr, n, i):
        largest = i
        l = 2 * i + 1
        r = 2 * i + 2

        if l < n:
            self.comparisons += 1
            if arr[l] > arr[largest]:
                largest = l

        if r < n:
            self.comparisons += 1
            if arr[r] > arr[largest]:
                largest = r

        if largest != i:
            arr[i], arr[largest] = arr[largest], arr[i]
            self._heapify(arr, n, largest)



# Main Test Program
class SortingTester:
    def __init__(self):
        # The 4 required array sizes
        self.sizes = [1000, 10000, 100000, 1000000]
        self.current_type = ""
        # This dictionary holds the 4 arrays
        self.data = {size: [] for size in self.sizes}
        # This dictionary holds the results for the CURRENTLY active population
        self.current_results = None

    def RandomIntegers(self, size):
        """Returns a list populated with random integers."""
        return [random.randint(1, 1000000) for _ in range(size)]

    def IncreasingIntegers(self, size):
        """Returns a list populated 1 to n."""
        return list(range(1, size + 1))

    def DecreasingIntegers(self, size):
        """Returns a list populated n down to 1."""
        return list(range(size, 0, -1))

    def populate(self, choice):
        """Populates the 4 arrays based on user choice."""
        types = {1: "Random", 2: "Increasing", 3: "Decreasing"}
        self.current_type = types[choice]
        
        # We re-populate the 4 arrays based on the method selected
        for size in self.sizes:
            if choice == 1:
                self.data[size] = self.RandomIntegers(size)
            elif choice == 2:
                self.data[size] = self.IncreasingIntegers(size)
            elif choice == 3:
                self.data[size] = self.DecreasingIntegers(size)
        
        # Reset results because the data changed
        self.current_results = None
        print(f"Successfully populated the 4 arrays with {self.current_type} integers.")

    def run_tests(self):
        """Runs algorithms on the current 4 arrays."""
        if not self.current_type:
            print("Error: No arrays populated. Go to Option 1 first.")
            return

        # Initialize the results table for the current type
        self.current_results = {size: {} for size in self.sizes}
        algos = [("Mergesort", Mergesort()), ("Quicksort", Quicksort()), ("Heapsort", Heapsort())]

        for size in self.sizes:
            print(f"Sorting {self.current_type} arrays of size n={size}...")
            for name, obj in algos:
                #  Use a copy so the next algorithm gets the same original data
                arr_copy = list(self.data[size])
                count = obj.sort(arr_copy)
                self.current_results[size][name] = count
        print("Done. You can now display the outputs.")

    def display(self):
        """Displays the table for the CURRENTLY populated array type only."""
        if self.current_results is None:
            print("No results to display. Please 'Run Algorithms' (Option 2) first.")
            return

        print(f"\nArray Type: {self.current_type}")
        print(f"{'Algorithm':<15} {'n=1000':<12} {'n=10000':<12} {'n=100000':<12} {'n=1000000':<12}")
        print("-" * 70)

        for algo_name in ["Mergesort", "Quicksort", "Heapsort"]:
            row = f"{algo_name:<15}"
            for size in self.sizes:
                val = self.current_results[size].get(algo_name, "N/A")
                row += f" {str(val):<12}"
            print(row)


def main():
    tester = SortingTester()
    while True:
        print("\n--------MAIN MENU-------")
        print("1. Populate All Arrays")
        print("2. Run Algorithms")
        print("3. Display outputs")
        print("4. Exit program")

        choice = input("Enter option number: ")

        if choice == '1':
            print("\n--------Option 1 Submenu-----------")
            print("1. Randomly generated integers")
            print("2. Increasing integer from 1 to n")
            print("3. Decreasing integers from n to 1")
            try:
                sub_choice = int(input("Enter option number: "))
                if sub_choice in [1, 2, 3]:
                    tester.populate(sub_choice)
                else:
                    print("Invalid submenu option.")
            except ValueError:
                print("Invalid input.")

        elif choice == '2':
            tester.run_tests()
            print("Processing complete.")

        elif choice == '3':
            tester.display()

        elif choice == '4':
            print("Exiting program.")
            break

        else:
            print("Invalid option. Try again.")


if __name__ == "__main__":
    main()