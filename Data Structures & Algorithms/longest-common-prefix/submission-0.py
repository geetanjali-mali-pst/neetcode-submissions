class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        min_len = float('inf')
        cnt = 0
        for st in strs:
            min_len = min(min_len, len(st))
        for i in range(min_len):
            is_same = True
            for st in strs:
                if st[i] != strs[0][i]:
                    is_same = False
                    break
            if is_same:
                cnt += 1
            else:
                break
        return strs[0][:cnt]