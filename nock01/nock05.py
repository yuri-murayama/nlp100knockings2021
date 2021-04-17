def Ngram(s,n):
    list = []

    for i in range(0,len(s)-1):
        list.append(s[i:i+n])
           
    return list


def main():
    s = str(input("文字を入力:"))
    n = int(input("n-gram:"))

    ws = s.split()
    print(Ngram(ws,n))

    ls = s.replace(' ','')
    print(Ngram(ls,n))

if __name__ == '__main__':
	main()
