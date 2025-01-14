class Solution:
    def countWords(self, words1, words2):
        """Counts the number of words that appear exactly once in both
        lists of words.
        
        Args:
            words1 (list[str]): The first list of words.
            words2 (list[str]): The second list of words.
        
        Returns:
            count (int): The number of words that appear exactly once in both
            lists.
        """
        # Ensures iteration through the fewest words possible
        if len(set(words1)) < len(set(words2)):
            words2, words1 = words1, words2
        count = 0
        for word in set(words2):
            if words1.count(word) == 1 and words2.count(word) == 1:
                count += 1
        return count
