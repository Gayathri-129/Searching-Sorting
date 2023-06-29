def sort_strings(strings):
    for i in range(len(strings)):
        for j in range(i + 1, len(strings)):
            if strings[i] > strings[j]:
                strings[i], strings[j] = strings[j], strings[i]

    return strings


if __name__ == "__main__":
    strings = ["dog", "apple", "cat", "elephant", "abroad", "banana", "konaha"]
    sorted_strings = sort_strings(strings)
    print(sorted_strings)