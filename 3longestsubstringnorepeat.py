class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        longestSubstring = ""
        currentSubstring = ""

        if len(s) == 1:
            return 1

        for firstLetter in range(len(s)):
            if len(currentSubstring) > len(longestSubstring):
                longestSubstring = currentSubstring
                currentSubstring = ""
            currentSubstring = s[firstLetter]
            for y in range(firstLetter + 1, len(s)):
                if s[y] not in currentSubstring:
                    currentSubstring += s[y]
                else:
                    break

        return len(longestSubstring)


print(Solution.lengthOfLongestSubstring(Solution, "abcabcbb"))
print(Solution.lengthOfLongestSubstring(Solution, "bbbbb"))
print(Solution.lengthOfLongestSubstring(Solution, "pwwkew"))
print(Solution.lengthOfLongestSubstring(Solution, " "))
print(Solution.lengthOfLongestSubstring(Solution, "au"))
