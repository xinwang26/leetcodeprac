#I had no idea on this problem, folowing is "traceback method"
class Solution(object):
    def generateParenthesis(self, N):
        if N == 0: return ['']
        ans = []
        def gen(seq='',left=0,right=0):
            # print(left,right,seq)
            if len(seq) == 2*N:
                ans.append(seq)
                return 
            else:
                if right < left:
                    gen(seq+')',left,right+1)
                if left <N:
                    gen(seq+'(',left+1,right)
                
        
        gen()
        return ans
