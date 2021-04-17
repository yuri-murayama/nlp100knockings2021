def cipher(s):
    news = ''
    for x in s:
        if x.islower():
            news += chr(219 - ord(x))
        else:
            news += x

    return news

def main():
    s = str(input("文字列を入力:"))

    print(cipher(s))

if __name__ == '__main__':
	main()
