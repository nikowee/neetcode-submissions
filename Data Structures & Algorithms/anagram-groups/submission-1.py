class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        seen = {} # unique anagram combination: index in output
        output = [] # list of list of unique anagrams

        for i, s in enumerate(strs):
            # Create new entry
            key = "".join(sorted(s))

            # Check if seen this anagram combination before
            if key in seen:
                # Add the new word to output
                output[seen[key]].append(s)
            else: # Not seen before
                # Store new entry in seen
                seen[key] = len(output)

                # Add the new word to output
                output.append([s])
               

        return output



        