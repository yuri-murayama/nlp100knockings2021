def template(x,y,z):

    return print(x, "時の" + y + "は", z)

def main():
    x = int(input("x:"))
    y = str(input("y:"))
    z = float(input("z:"))

    template(x,y,z)

if __name__ == '__main__':
	main()
