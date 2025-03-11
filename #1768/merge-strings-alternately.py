def mergeAlternately(word1: str, word2: str) -> str:
    output = ""
    min_length = min(len(word1), len(word2))
    for i in range(min_length):
        output += word1[i] + word2[i]
    # Add remaining letters of the longer word.
    output += word1[i+1:] + word2[i+1:]
    return output
