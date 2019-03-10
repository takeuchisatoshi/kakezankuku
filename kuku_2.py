def main():
    y_size = int(input("行数を入力してください: "))
    x_size = int(input("列数を入力してください: "))
    y_1 = list(range(1, y_size + 1))
    x_1 = list(range(1, x_size + 1))
    for y_n in y_1:
        for x_n in x_1:
            xy = y_n * x_n
            print(xy, end=" ")
        print()


if __name__ == '__main__':
    main()
