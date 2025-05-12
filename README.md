# Day 30 - Search in Rotated Sorted Array 🔍

## Problem Statement 📄
Given a sorted and rotated array arr[] of distinct elements, your task is to find the index of a given target key.
If the key is not present in the array, return -1.

This is a classic Binary Search variation problem often asked in interviews.

## Approach 🚀
1. Apply a modified Binary Search.

2. At each step:

- Check if the middle element is the target.

- Determine if the left half is sorted:

    - If yes, check if the target lies within the sorted half.

- Else, check if the right half is sorted:

    - If yes, check if the target lies within the sorted half.

3. Narrow the search space accordingly.

4. If no match found, return -1.

---

## Key Concepts Applied 💡
- Binary Search in Rotated Sorted Array.

- Divide and Conquer.

- Optimized searching.

## Time and Space Complexity ⏱
- Time Complexity: O(log N)

- Space Complexity: O(1) (Iterative approach, no extra space)

---

## Reflection 💭
This problem reinforces the importance of adapting binary search to different scenarios, especially in rotated or modified arrays.
Perfect for practicing variations of divide-and-conquer techniques.
