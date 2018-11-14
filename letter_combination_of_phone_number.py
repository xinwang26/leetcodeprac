class Solution:
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        mapping = {'2' :['a','b','c'],'3' :['d','e','f'],'4' :['g','h','i'],'5' :['j','k','l'],'6' :['m','n','o'],'7' :['p','q','r','s'],'8' :['t','u','v'],'9' :['w','x','y','z']}
        last = []
        this = []
        for d in digits:
            if len(this)<1:
                this = mapping[d]  
            else:
                last = this
                # print(last,this)
                this = []
                for substr in last:
                    for new in mapping[d]:
                        this.append(substr+new)
        return this

#simpler solution but almost same speed
class Solution:
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        if digits == "":
            return []
        store = [""]
        num = ["", "1", "abc", "def", "ghi", "jkl", "mno", "pqrs", "tuv", "wxyz"]
        for d in digits:
            tmpStore = []
            for val in store:
                for c in num[int(d)]:
                    tmpStore.append(val + c)
            store = tmpStore
        return store