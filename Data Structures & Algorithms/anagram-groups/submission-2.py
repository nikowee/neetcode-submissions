from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # defaultdict(list) creates an empty list if we try to assign to a key that doesnt exist
        # Does not raise KeyError like normal dicts
        result = defaultdict(list)

        for s in strs: # for each string
            # List of count of each of 26 alphabets
            count = [0] * 26

            for c in s: # for each character
                # Add 1 count for each char in count
                # Fetch indices using unicode value
                count[ord(c) - ord("a")] += 1

            # Lists arent hashable so they cannot be dict keys so we convert to tuples instead
            # Append this word according to the unique count value
            result[tuple(count)].append(s)

        # convert the result values to a python list
        return list(result.values())

        