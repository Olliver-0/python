nums = []
maior = 0
menor = 0
for c in range(0, 5):
    nums.append(int(input(f'Digite um valor para a posição {c}')))
    if c == 0:
        maior = menor = nums[c]
    else:
        if nums[c] > maior:
            maior = nums[c]
        if nums[c] < menor:
            menor = nums[c]
print(f'O maior valor foi {maior} nas posições ', end='')
for i, v in enumerate(nums):
    if v == maior:
        print(f'{i}...', end='')
