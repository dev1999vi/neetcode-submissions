class Solution:

  def topKFrequent(self, nums: List[int], k: int) -> List[int]:
    freq = {}
    for num in nums:
      freq[num] = freq.get(num, 0) + 1

    # 1. Initialize each bucket as an empty list
    bucket = [[] for _ in range(len(nums) + 1)]

    # 2. Push elements directly into their frequency index: O(unique elements) <= O(N)
    for num, count in freq.items():
      bucket[count].append(num)

    # 3. Collect from highest frequency down: O(N)
    res = []
    for count in range(len(bucket) - 1, 0, -1):
      for num in bucket[count]:
        res.append(num)
        if len(res) == k:
          return res

    return res