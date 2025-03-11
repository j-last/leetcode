
class Solution:
    def maximumSubsequenceCount(self, text, pattern):
        """Counts the maximum number of subsequences of the pattern 
        that can be made in 'text' by adding one letter to the text.

        Args:
            text (str): The text to add a letter to.
            pattern (str): The pattern to make subsequences of.

        Returns:
            int: The maximum number of subsequences that can be made.
        """
        letter1, letter2 = pattern
        # Count how many subsequences there currently are.
        subsequences = 0
        num_letter2_to_right = text.count(letter2)
        for letter in text:
            if letter == letter2:
                num_letter2_to_right -= 1
                if num_letter2_to_right == 0: break
            if letter == letter1:
                subsequences += num_letter2_to_right
        # Add on how many subsequences that can be made by adding the
        # first letter at the start or the second letter at the end.
        max_new_subsequences = max(text.count(letter1), text.count(letter2))
        return subsequences + max_new_subsequences
