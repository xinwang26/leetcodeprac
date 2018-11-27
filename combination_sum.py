#my 76ms slow solution
class Solution:
    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        results = []
        def rec_search(target, candidates, found):
            # print(found)
            for i in reversed(range(len(candidates))):
                if target == candidates[i]:
                        results.append(found +[target])
                elif target < candidates[i]:
                    continue
                else:
                    rec_search(target - candidates[i],candidates[i:],found+[candidates[i]])
        rec_search(target, candidates, [])
        return results

#after change to append and pop, reduced to 72ms
class Solution:
    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        results = []
        def rec_search(target, candidates, found):
            # print(found)
            for i in range(len(candidates)):
                if target == candidates[i]:
                    results.append(found +[target])
                elif target < candidates[i]:
                    continue
                else:
                    found.append(candidates[i])
                    rec_search(target - candidates[i],candidates[i:],found)
                    found.pop()
        rec_search(target, candidates, [])
        return results

#my fixed solution, 64ms:
class Solution:
    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        results = []
        candidates= sorted(candidates)
        def rec_search(target, candidates, found, last):
            for n in candidates:
                if n < last:
                    continue
                if target == n:
                    results.append(found+[n])
                    return
                elif target < n:
                    return 
                else:
                    rec_search(target - n,candidates,found+[n], n)
        rec_search(target, candidates, [], -1)
        return results

#my 60ms solution:
class Solution:
    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        results = []
        candidates= sorted(candidates)
        if target< candidates[0]:
            return []
        def rec_search(target, candidates, found, last):
            if target ==0:
                results.append(found)
            for n in candidates:
                if target < n:
                    return
                if n < last:
                    continue
                rec_search(target - n,candidates,found+[n], n)
        rec_search(target, candidates, [], -1)
        return results

#sampled 60ms fastest solution:

class Solution:
    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        self.resList = []
        candidates = sorted(candidates)
        self.dfs(candidates,[],target,0)
        return self.resList
    def dfs(self, candidates, sublist, target, last):
        if target == 0:
            self.resList.append(sublist[:])
        if target< candidates[0]:
            return 
        for n in candidates:
            if n > target:
                return
            if n < last:
                continue #make sure no duplicates, latter always greater or equal than former
            sublist.append(n)
            self.dfs(candidates,sublist,target - n, n)
            sublist.pop()

#further optimized 56ms solution:
class Solution:
    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        self.resList = []
        candidates = sorted(candidates)
        if target< candidates[0]:
            return []
        self.dfs(candidates,[],target,0)
        return self.resList
    def dfs(self, candidates, sublist, target, last):
        if target == 0:
            self.resList.append(sublist[:])
        for n in candidates:
            if n > target:
                return
            if n < last:
                continue #make sure no duplicates, latter always greater or equal than former
            sublist.append(n) #using append and pop seems slightly faster than passing with sublist = [n], no idea why
            self.dfs(candidates,sublist,target - n, n)
            sublist.pop()

#time consumption seems quite random, this also goes for 56ms once
class Solution:
    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        results = []
        candidates= sorted(candidates)
        if target< candidates[0]:
            return []
        def rec_search(target, candidates, found, last):
            if target ==0:
                results.append(found)
            else:
                for n in candidates:
                    if target < n:
                        return
                    if n < last:
                        continue
                    rec_search(target - n,candidates,found +[n], n)
        rec_search(target, candidates, [], -1)
        return results