def perm(n,begin,end):
    if begin>=end: #end -1 is enough
        print(n)
    else:
        i=begin
        for num in range(begin,end):
            print('0 ',i,num,n)
            n[num],n[i]=n[i],n[num]
            print('1 ',i,num,n)
            perm(n,begin+1,end)
            n[num],n[i]=n[i],n[num]
            print('2 ',i,num,n)

n=[1,2,3]
perm(n,0,len(n))