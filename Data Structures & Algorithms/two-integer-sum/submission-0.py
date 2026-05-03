class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
               hashmap= {}
               for index, value in enumerate(nums):
                hashmap[value] = index
               for index, value in enumerate(nums):
                diff = target - value
                if diff in hashmap and hashmap[diff] != index:
                    return [index,hashmap[diff] ]
               return []



               
                
