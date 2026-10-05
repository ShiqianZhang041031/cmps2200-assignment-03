# Assignment 03

Name: Shiqian Zhang

## 1b

The work of `isearch` is $O(n)$ because `iterate` processes each of the $n$ elements once. Since `iterate` is sequential, its span is also $O(n)$.

Therefore,

$$
W(n) = O(n)
$$

and

$$
S(n) = O(n).
$$

## 1d

The `rsearch` algorithm first maps each element to a Boolean value indicating whether it equals the search key. The map has $O(n)$ work and $O(1)$ span when performed in parallel.

The balanced `reduce` has the recurrences

$$
W(n) = 2W(n/2) + O(1)
$$

and

$$
S(n) = S(n/2) + O(1).
$$

Therefore, the reduce has $O(n)$ work and $O(\log n)$ span. Including the parallel map, the overall algorithm has

$$
W(n) = O(n)
$$

and

$$
S(n) = O(\log n).
$$

## 1e

With `ureduce`, the two recursive subproblems have sizes approximately $n/3$ and $2n/3$. Thus the work recurrence is

$$
W(n) = W(n/3) + W(2n/3) + O(1),
$$

which has solution

$$
W(n) = O(n).
$$

Since the recursive calls can run in parallel, the span is determined by the larger subproblem:

$$
S(n) = S(2n/3) + O(1),
$$

which has solution

$$
S(n) = O(\log n).
$$

Thus the resulting `rsearch` still has $O(n)$ work and $O(\log n)$ span.

## 3b

The iterative solution examines one input element at each step. Its work recurrence is

$$
W(n) = W(n-1) + O(1),
$$

so

$$
W(n) = O(n).
$$

Because `iterate` processes the elements sequentially, its span recurrence is also

$$
S(n) = S(n-1) + O(1),
$$

so

$$
S(n) = O(n).
$$

## 3d

The parallel `map` has $O(n)$ work and $O(1)$ span.

The efficient parallel `scan` from class has $O(n)$ work and $O(\log n)$ span.

The `reduce` used to find the minimum prefix value also has $O(n)$ work and $O(\log n)$ span.

Therefore, the entire scan-based parenthesis matching algorithm has

$$
W(n) = O(n)
$$

and

$$
S(n) = O(\log n).
$$

## 3f

The divide-and-conquer algorithm divides the input into two halves and does constant work to combine the two results.

The work recurrence is

$$
W(n) = 2W(n/2) + O(1),
$$

which gives

$$
W(n) = O(n).
$$

Because the two recursive calls can be executed in parallel, the span recurrence is

$$
S(n) = S(n/2) + O(1),
$$

which gives

$$
S(n) = O(\log n).
$$