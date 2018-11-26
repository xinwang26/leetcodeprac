def perm(char):
    for i in range(len(char)):
        for j in range(i,len(char)):
            print(i,j)
            print(char)
            char[i],char[j] = char[j],char[i]
            if i == len(char)-1:
                print(char)
            else:
                char[j],char[i] = char[i],char[j]
if __name__ == '__main__':
	perm([1, 2, 3,4])