# #contoh penerapan queue pada bahasa python
# #membuat queue dari awal
# queue = []
#
# #Menambahkan elemen ke queue
# queue.append('a')
# queue.append('b')
# queue.append('c')
#
# print("Queue awal")
# print(queue)
#
# #mengambil queue
# print("\nElemen elemen yang diambil dari queue")
# print(queue.pop(0))
# print(queue.pop(0))
# print(queue.pop(0))
#
# print("\nQueue setelah elemen elemen diambil")
# print(queue)

daftar_nama = []

print(f'========Selamat Datang di UJANG Software=======')
print(f'========Silakan Masukkan Data Antrian Anda=======')

for i in range(1,4) :
    nama = str(input("Masukkan Nama anda = "))
    print(f'Nomor Antrian Anda Adalah = {i}')
    daftar_nama.append(nama)
    i += 1
print(f'Daftar antrian = ')

jml = len(daftar_nama)
for j in range(len(daftar_nama)) :
    print(f'{j + 1}. {daftar_nama.pop(0)}')
