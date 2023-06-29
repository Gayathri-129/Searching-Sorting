def quick_sort(list, low, high):
    if low < high:
        pivot = partition(list, low, high)
        quick_sort(list, low, pivot - 1)
        quick_sort(list, pivot + 1, high)


def partition(list, low, high):
    pivot = list[high]
    i = low - 1
    for j in range(low, high):
        if list[j] <= pivot:
            i += 1
            list[i], list[j] = list[j], list[i]
    list[i + 1], list[high] = list[high], list[i + 1]
    return i + 1


if __name__ == "__main__":
    list = [1, 3, 5, 7, 9, 2, 4, -1, 6, 8, 0]
    quick_sort(list, 0, len(list) - 1)
    print(list)