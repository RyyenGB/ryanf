#
# def binarySearch(arr, l, r, x):
#
# 	while l <= r:
#
# 		mid = l + (r - l) // 2
#
# 		if arr[mid] == x:
# 			return mid
#
# 		elif arr[mid] < x:
# 			l = mid + 1
#
# 		else:
# 			r = mid - 1
#
# 	return -1
#
#
#
# arr = [2, 3, 4, 10, 40]
# x = 10
#
# result = binarySearch(arr, 0, len(arr)-1, x)
#
# if result != -1:
# 	print("Element is present at index % d" % result)
# else:
# 	print("Element is not present in array")

def binarySearch(array, x, low, high):
    while low <= high:
        mid = low + (high - low)//2
        if array[mid] == x:
            return mid
        elif array[mid] < x:
            low = mid + 1
        else:
            high = mid - 1
    return -1
array = [0, 636, 646, 656, 666, 676, 686, 696]
print ("--------Perpustakaan SMAN 1 GEGER-------"
       "1.636 - Buku Bahasa Inggris"
       "2. 646 - Buku Fisika"
       "3. 656 - Buku IPS"
       "4. 666 - Buku Matematika"
       "5. 676 - Buku PKN"
       "6. 686 - Buku Bahasa Indonesia"
       "7. 696 - Buku Kimia")
x = int(input("masukkan Kode Buku = "))
result = binarySearch(array, x, 0, len(array)-1)
if result != -1:
    print("Terdapat buku tersebut ada pada ruangan " + str(result))
else:
    print("Tidak Ditemukan")
