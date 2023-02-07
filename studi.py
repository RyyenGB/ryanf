stack_kok = ['kok 1', 'kok 2', 'kok 3', 'kok 4', 'kok 5']
print(stack_kok)
diambil = int(input('masukan jumlah kok yang diambil = '))
kok = 0
while kok < diambil:
    print(f'{stack_kok.pop()} telah di pakai')
    kok += 1
print(f'tersisa {stack_kok} dengan jumlah kok diwadah ada {len(stack_kok)}')