class Solution:
    def mostWordsFound(self, sentences:list[str]) -> int:
        maxwords = 0
        for sentence in sentences:
            words = sentence.count(" ") + 1
            maxwords = max(maxwords, words)
        return maxwords
