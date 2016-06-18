# Intro, Divide and Conquer, Big-Oh Notation

## Optional Theory Problems
1. You are given as input an unsorted array of n distinct numbers, where n is a power of 2. Give an algorithm that identifies the second-largest number in the array, and that uses at most n+log(n)−2 comparisons.

My approach here stemmed from noticing that this required operations equal to the length of the array plus a number near how many times it took to split the array into pairs, so I decided to try and see how it would turn out if I did it in the following way:

Suppose we had the array [5,1,3,2,7,4]. We populate a second array as we traverse the first one to find the initial maximum, as follows: [],[5,1,3,2,7,4] -> [5],[3,2,7,4] -> [5,3],[7,4] -> [5,3,7],[]. Holding onto this array, we do the same thing again with the new array: [],[5,3,7] -> [5],[7] -> 7. Now, we look at what elements we compared with 7, by going back to the array we held onto, namely, [5,3,7]. Clearly, out of the elements in this array that aren't 7, 5 is the maximum, and will thus be the second-highest element in this array.

The reason this works can essentially be proven by showing that the second-maximum element is in every level of comparison except at the very end, when we end up with the maximum number.
2. You are a given a unimodal array of n distinct elements, meaning that its entries are in increasing order up until its maximum element, after which its elements are in decreasing order. Give an algorithm to compute the maximum element that runs in O(log n) time.

This is pretty much just a binary search: we look at the middle element of the array, and the element right after that. If these two elements are in sequence, recurse on the right half, else recurse on the left half.

3. You are given a sorted (from smallest to largest) array A of n distinct integers which can be positive, negative, or zero. You want to decide whether or not there is an index i such that A[i] = i. Design the fastest algorithm that you can for solving this problem.

Again, this is pretty much just a binary search: at our point of interest, a[i]-i = 0, so for all j < i, a[j] - j <= 0, and for all j > i, a[j] - j >= 0. Thus, we look at the middle, check if it's our point, and if it's not, recurse left if the difference there is > 0, and recurse right if the difference there is < 0.

Note that it can be possible that there are multiple i such that A[i] = i, we only really have to find 1, so this does it in O(log(n)).


