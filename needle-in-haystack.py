#Leetcode question #28
#Since we are asked to provide the index of the first instance of str 'needle' in str 'haystack', we can use the .index string method.
#We set n = -1 as the default value if no such 'needle' exists in the 'haystack'

class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        n = -1
        if needle in haystack:
            n = haystack.index(needle)
        return n

  #Runtime 0ms
  #Memory 17.91 mb

  #when i wrote this i was unaware of the .find() method
  #class Solution:
    #def strStr(self, haystack: str, meedle:, str) -> int:
      #return haystack.find(needle)
