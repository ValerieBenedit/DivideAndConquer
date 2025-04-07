# DivideAndConquer

## Word Lookup in a Large Dictionary
You have a local offline dictionary with a massive number of entries. You frequently need to
check if a certain word exists and retrieve its definition. By keeping the dictionary in sorted
order, you can perform binary search (divide and conquer) for quick lookups.
Word Lookup in a Large Dictionary
### Requirements:
1. Generate one test case with a massive number of entries (GenAI will be helpful.)
2. The source code for both generating test case and solution to search.
3. If necessary, short discussion to introduce how to run your program.
4. Complexity analysis.


## Global Phone Directory Sorting
You manage a global phone directory with millions of entries for an international company. It must
be sorted (by name or phone number) so that lookups and reports can be done efficiently. The
dataset is large, and you have limited memory; you want the sort to finish quickly.
Global Phone Directory Sorting
### Requirements:
1. Generate one test case with a massive number of entries (GenAI will be helpful.)
2. The source code for both generating test case and solution to sort. Implement a Merge Sort or
Quick Sort solution (divide-and-conquer) to sort the directory.
3. If necessary, short discussion to introduce how to run your program.
4. You are required to use solution. A short discussion/analysis why your
implementation is .
O(n log n)
O(n log n)

## Large Matrix Multiplication
You work in image processing or big data analytics and must multiply large matrices
(representing images, correlation matrices, etc.). The classical matrix multiplication is too
slow for large . You can adopt Strassen’s divide-and-conquer to reduce the multiplication count,
potentially boosting performance for sufficiently large .
n × n
O(n 3)
n
n

### Requirements:
1. Implement Strassen’s algorithm for matrix multiplication on matrices (assume is a
power of 2 or handle padding.)
2. Implement traditional matrix multiplication method.
3. Compare the two methods above from the viewpoint of runtime. You are required to draw a
figure to show the runtime change with increasing .
4. The source code.
(n × n) n
n

## Maximum Subarray Sum (Stock Profit Analysis)
You’re analyzing stock profits: you have a numerical array (some values positive, some negative),
each representing daily (or segment) gain/loss. You want the contiguous subarray that yields the
largest sum—a “best buy-sell interval.”
While Kadane’s algorithm solves it in , this task specifically asks for a divide-and-
conquer approach.
O(n)

### Requirements:
1. Implement a D&C algorithm:
1. Divide the array into left/right halves, recursively find max subarray sum in each;
2. Find the cross-mid subarray sum by combining the right edge of the left half and the left
edge of the right half;
3. Take the maximum among these three.
2. Generate test case to show your implementation is correct.
3. The source code and complexity analysis.



