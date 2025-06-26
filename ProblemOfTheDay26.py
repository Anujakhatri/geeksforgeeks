#Game with String
#Given a string s consisting of lowercase alphabets and an integer k, your task is to find the minimum possible value of the string after removing exactly k characters.
#The value of the string is defined as the sum of the squares of the frequencies of each distinct character present in the string.

import heapq
from collections import Counter
class Solution:
    def minValue(self, s, k):
        #code here
        freq = Counter(s)
        
        #Use a max heap (invert frequencies to simulate max heap)
        max_heap = [-count for count in freq.values()]
        heapq.heapify(max_heap)

        #Remove k characters
        for _ in range(k):
            if max_heap:
                max_count = heapq.heappop(max_heap)
                max_count += 1  # Since it's negative, this reduces the absolute value by 1
                if max_count < 0:
                    heapq.heappush(max_heap, max_count)

        #Calculate the sum of squares of remaining frequencies
        return sum((abs(count) ** 2) for count in max_heap)

