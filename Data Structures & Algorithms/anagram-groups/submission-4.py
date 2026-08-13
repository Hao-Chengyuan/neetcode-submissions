class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # use the sorted strings as the keys
        groups = defaultdict(list)
        for s in strs:
            key = ''.join(sorted(s))
            if key in groups.keys():
                groups[key].append(s)
            else:
                groups[key] = [s]
        return list(groups.values())