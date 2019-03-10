def main():
    y_size = int(input("行数を入力してください: "))
    x_size = int(input("列数を入力してください: "))

    y_n = 1
    while y_n <= y_size:
        x_n = 1
        while x_n <= x_size:
            xy = y_n * x_n
            x_n += 1
            print(xy, end=" ")
        y_n += 1
        print()


if __name__ == '__main__':
    main()
