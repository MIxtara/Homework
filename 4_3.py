n = int(input())
data = {
    i: {
        'name': input(f'name {i}: '),
        'email': input(f'email {i}: ')
    } for i in range(n)
}
print(data)