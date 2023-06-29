def insertion_sort(list):
    for i in range(1, len(list)):
        key = list[i]
        j = i - 1
        while j >= 0 and list[j] > key:
            list[j + 1] = list[j]
            j -= 1
        list[j + 1] = key


if __name__ == "__main__":
    list = [1, 3, 5, 7, 9, 2, 4, -10, -1, 6, 8, 0]
    insertion_sort(list)
    print(list)