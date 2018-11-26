def perm(char, i):
    if i == len(char) - 1:
        print(char)
    else:
        for j in range(i, len(char)):
            print('0 ',i,j,char)
            char[i], char[j] = char[j], char[i]
            print('1 ',i,j,char)
            perm(char, i + 1)
            char[i], char[j] = char[j], char[i] # swap back, for the next loop
            print('2 ',i,j,char)
if __name__ == '__main__':
	perm([3,2,1], 0)