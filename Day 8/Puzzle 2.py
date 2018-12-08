with open('d8-inputs') as txtfile:
    for row in txtfile:
        a = row.split(' ')
        for n, x in enumerate(a):
            a[n] = int(a[n])



def parse(data):
    children, metas = data[:2]
    data = data[2:]
    scores = []
    totals = 0

    for i in range(children):
        total, score, data = parse(data)
        totals += total
        scores.append(score)

    totals += sum(data[:metas])

    if children == 0:
        return (totals, sum(data[:metas]), data[metas:])
    else:
        return (
            totals,
            sum(scores[k - 1] for k in data[:metas] if k > 0 and k <= len(scores)),
            data[metas:]
        )

total, value, remaining = parse(a)

print('part 2:', value)