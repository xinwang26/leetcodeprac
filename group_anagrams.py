#worsk but exceed time limit
class Solution:
    def material(self,string):
        tb = {}
        for stri in string:
            try:
                tb[stri] += 1
            except:
                tb[stri] = 1
        return tb
    def groupAnagrams(self, strs: 'List[str]') -> 'List[List[str]]':
        # print(self.groupAnagrams.__annotations__)
        if len(strs) == 0:
            return []
        result = [[strs[0]]]
        for string in strs[1:]:
            for i in range(len(result)):
                found = 0 
                if self.material(result[i][0]) == self.material(string):
                    result[i].append(string)
                    found = 1
                    break
            if not found:
                result.append([string])
        return result

#idea 1 sorted list
class Solution:
    def groupAnagrams(self, strs: 'List[str]') -> 'List[List[str]]':
        # print(self.groupAnagrams.__annotations__)
        if len(strs) == 0:
            return []
        result = {}
        for s in strs:
            try:
                result[tuple(sorted(s))].append(s)
            except:
                # print(s,sorted(s))
                result[tuple(sorted(s))] = [s]
        return list(result.values())

#idea 2: letter freq table but not dict, take advantage of the order of 26 
class Solution:
    def groupAnagrams(self, strs: 'List[str]') -> 'List[List[str]]':
        # print(self.groupAnagrams.__annotations__)
        if len(strs) == 0:
            return []
        result = {}
        for s in strs:
            dictword = [0]*26
            for l in s:
                dictword[ord(l)-ord('a')] +=1
            try:
                result[tuple(dictword)].append(s)
            except:
                result[tuple(dictword)] = [s]
        return list(result.values())

#both very slow, fast result:
class Solution:
    def groupAnagrams(self, strs: 'List[str]') -> 'List[List[str]]':
        dic = {}
        for item in strs:
            stored_string = ''.join(sorted(item))
            if stored_string not in dic: #if else faster than try except by 8ms too
                dic[stored_string] = [item]
            else:
                dic[stored_string].append(item)
        result = []
        for item in dic.values():
            result.append(item) #this is faster then directly transfer to list by 8ms
        return result
