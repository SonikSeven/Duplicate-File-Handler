import os
import sys
import hashlib as h


def question(msg_1="", msg_2="", op_1="yes", op_2="no"):
    try:
        return {op_1: True, op_2: False}[input(msg_2 + msg_1)]
    except KeyError:
        return question(msg_1, "\nWrong option\n", op_1, op_2)


def get_file_tree(file_format):
    file_tree = {}
    for root, _, names in os.walk(sys.argv[1]):
        for name in names:
            if name.endswith(file_format):
                path = os.path.join(root, name)
                size = os.path.getsize(path)
                with open(path, "rb") as file:
                    hash_value = h.md5(file.read()).hexdigest()
                if size not in file_tree:
                    file_tree[size] = {}
                if hash_value not in file_tree[size]:
                    file_tree[size][hash_value] = [path]
                else:
                    file_tree[size][hash_value] += [path]
    return file_tree


def display(file_tree, order):
    for size in sorted(file_tree, reverse=order):
        print("\n", size, " bytes", sep="")
        for hash_value in file_tree[size].values():
            print(*sorted(hash_value), sep="\n", end="\n")


def get_duplicates(file_tree, order):
    duplicates = []
    counter = 0
    for size in sorted(file_tree, reverse=order):
        print("\n", size, " bytes", sep="")
        for hash_value in file_tree[size]:
            if len(file_tree[size][hash_value]) > 1:
                print("Hash:", hash_value)
                for path in file_tree[size][hash_value]:
                    counter += 1
                    duplicates.append(path)
                    print(counter, path, sep=". ")
    return duplicates


def delete(duplicates, msg=""):
    try:
        indexes = [int(i) - 1 for i in input(msg + "\nEnter file numbers to delete:\n").split()]
        assert max(indexes) < len(duplicates) and min(indexes) >= 0
    except (ValueError, AssertionError):
        return delete(duplicates, "\nWrong format\n")
    total_size = 0
    for index in indexes:
        total_size += os.path.getsize(duplicates[index])
        os.remove(duplicates[index])
    print("\nTotal freed up space:", total_size, "bytes")


def main():
    file_tree = get_file_tree(input("Enter file format:\n"))
    order = question("\nEnter a sorting option:\n", "\nSize sorting options:\n1. Descending\n2. Ascending\n", "1", "2")
    display(file_tree, order)
    if question("\nCheck for duplicates?\n"):
        duplicates = get_duplicates(file_tree, order)
        if question("\nDelete files?\n"):
            delete(duplicates)


if __name__ == "__main__":
    main() if len(sys.argv) > 1 else print("Directory is not specified")
