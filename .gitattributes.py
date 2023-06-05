def find_pairs(numbers):
    pairs = []
    for n in range(len(numbers)):
        for k in range(n+1, len(numbers)):
            if numbers[n] + numbers[k] == 10:
                pairs.append((numbers[n], numbers[k]))
    return pairs

numbers = [1, 2, 3, 4, 5, 5, 6, 7]
pair = find_pairs(numbers)
for pair in pair:
    print(f"{pair[0]} + {pair[1]}")