with open('D11I.txt') as f:
    l = f.read().split()

numbers = [int(i) for i in l]

def process(numbers, count):
    memo = {}
    total_count = {n: 1 for n in numbers}

    for _ in range(count):
        next_count = {}
        for n, current_count in total_count.items():
            if n in memo:
                nxt = memo[n]
            elif n == 0:
                nxt = [1]
            elif len(str(n)) % 2 == 0:
                s = str(n)
                mid = len(s) // 2
                left = int(s[:mid])
                right = int(s[mid:])
                nxt = [left, right]
            else:
                nxt = [n * 2024]

            memo[n] = nxt

            for i in nxt:
                next_count[i] = next_count.get(i, 0) + current_count

        total_count = next_count

    return sum(total_count.values())

print(process(numbers, 75))
