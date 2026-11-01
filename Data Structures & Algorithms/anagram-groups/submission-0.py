class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hashed = {}
        output_list =[]
        for str in strs:
            temp_sort = ''.join(sorted(str))
            if not temp_sort in hashed:
                hashed[temp_sort] = [str]
            else:
                hashed[temp_sort].append(str)
        for key in hashed:
            output_list.append(hashed[key])
        return output_list