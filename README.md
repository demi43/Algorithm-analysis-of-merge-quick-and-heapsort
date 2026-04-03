## Algorithm Design & Experimental Analysis

### Overview
This project evaluates three classical sorting algorithms — **Mergesort, Quicksort, and Heapsort** — across:

- **Input sizes:** 1,000; 10,000; 100,000; 1,000,000  
- **Input types:** Random, Increasing (sorted), Decreasing (reverse sorted)  

Each algorithm was tested on all **12 combinations** (4 sizes × 3 input types).  
The number of comparisons was recorded to analyze performance behavior.

---

### Mergesort — O(n log n) (Best, Average, Worst)

Mergesort demonstrates **consistent and predictable performance** across all input types.

- Always splits the array evenly, regardless of input order  
- Comparisons scale proportionally to **n log₂(n)**  
- Slightly fewer comparisons for sorted inputs due to efficient merging  

**Key Insight:**  
Mergesort is **input-independent**, making it highly reliable.

---

### Quicksort — O(n log n) Average/Best, O(n²) Worst

Quicksort performs well on random data but degrades significantly on sorted inputs.

- Uses **last-element pivot**
- Sorted arrays produce **unbalanced partitions**:
  - One subarray of size (n − 1)
  - One subarray of size 0

This leads to the worst-case comparison count:
n(n-1)/2


**Observed Results:**

- n = 1,000 → ~499,500 comparisons  
- n = 10,000 → ~49,995,000 comparisons  

For larger inputs (100,000 and 1,000,000), the recursion depth exceeds Python’s stack limit, causing a **Stack Overflow Error (SOE)**.

**Key Insight:**  
Quicksort’s worst case is **real and reproducible**, not just theoretical.

**Improvement:**  
Using a **random pivot** or **median-of-three** strategy avoids this issue.

---

### Heapsort — O(n log n) (Best, Average, Worst)

Heapsort maintains consistent performance across all inputs.

- Comparison counts are stable regardless of ordering  
- Typically performs more comparisons than Mergesort  
- Less cache-friendly due to heap operations  

**Key Insight:**  
Heapsort is **robust and reliable**, but slightly less efficient in practice.

---

### Recursion Limitation (Quicksort)

Increasing Python’s recursion limit did not resolve performance issues.

- Worst-case recursion depth is **O(n)**  
- Leads to:
  - Stack overflow errors  
  - Extremely long runtimes  

**Conclusion:**  
The issue lies in the algorithm design (pivot choice), not just recursion limits.

---

### Final Conclusion

- **Mergesort** → Most **consistent and predictable**  
- **Heapsort** → Most **robust (no recursion issues)**  
- **Quicksort** → Fastest on average, but **risky with naive pivot selection**

Mergesort provides the best balance of **performance, stability, and reliability**, while Quicksort requires careful implementation to avoid worst-case behavior.
