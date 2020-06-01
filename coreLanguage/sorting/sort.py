li = [56, 6, 1, 32, 64, 4, 989, 61, 312, 32, 64, 651]

print(f'original List ==> {li}\n')
li.sort(reverse=True)
print(f'li.sort() Method Using List ==> {li}')

sortedli = sorted(li, reverse=True)
print(f'sorted(li) using the function ==> {sortedli}')
