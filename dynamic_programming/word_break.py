# Given a string s and a dictionary of strings wordDict, return true if s can be segmented into a space-separated sequence of one or more dictionary words.

# Note that the same word in the dictionary may be reused multiple times in the segmentation.

# Input: s = "leetcode", wordDict = ["leet","code"]
# Output: true


# Input: s = "applepenapple", wordDict = ["apple","pen"]
# Output: true

# Input: s = "catsandog", wordDict = ["cats","dog","sand","and","cat"]
# Output: false


def word_break(s, wordDict):

    # looking up an element in a set is O(1)
    words = set(wordDict)

    dp = [False] * (len(s)+1)
    dp[0] = True

    for i in range(len(s)):
        for j in range(i, len(s)):
            if dp[i] and s[i:j+1] in words:
                dp[j+1] = True

    return dp[len(s)]

print(word_break("applepenapple", ["apple","pen"]))
print(word_break("leetcode", ["leet","code"]))
print(word_break("catsandog", ["cats","dog","sand","and","cat"]))