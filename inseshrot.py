def insertion_sort(Baris):

    for i in range(1, len(Baris)):
        key_item = Baris[i]
        j = i - 1
        while j >= 0 and Baris[j] > key_item:
            Baris[j + 1] = Baris[j]
            j -= 1
        Baris[j + 1] = key_item

    return Baris

print("Kelereng Yang Sudah Diurutkan : ")
unordered = [14, 15, 16, 5, 6]
print(insertion_sort(unordered))




