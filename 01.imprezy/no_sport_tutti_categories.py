import meerkat
import matplotlib.pyplot as plt

t = meerkat.Table('IMPREZY_RAZEM_REFINED_AND_PYTHONED.csv', header=False)

categories = list(set(t.column(1)))
categories.remove('K')
categories.remove('S')

data = [(t, d) for t, d in zip(t.column(1), t.column(5))]
tmp  = { c: 0 for c in categories }

agg = {}

for t, y in data:
    if 2008 <= y <= 2011:

        if t == 'K':
            t = 'L'
        if t == 'S':
            t = 'I'

        agg.setdefault(y, dict(tmp))
        agg[y][t] += 1

tutti = [0] * len(categories)
for i, date in enumerate(agg, 1):
    tmp   = agg[date]
    data  = [ e for k, e in sorted(tmp.items()) ]
    tutti = [ a+b for a, b in zip(tutti, data) ]

avarage = [ e / 4.0 for e in tutti ]

plt.figure(1)
for i, date in enumerate(agg, 1):
    tmp = agg[date]
    import json
    print json.dumps(tmp['M'])

    data = [ e for k, e in sorted(tmp.items()) ]

    plt.subplot("%s1%s" % (len(agg.keys()), i))
    plt.title("Tutti %s by category" % date)
    plt.bar(range(len(data)), data, align='center')
    plt.plot(avarage, '+', color="#ff6000", lw=2)
    plt.xticks(range(len(tmp.keys())), sorted(tmp.keys()))
    plt.axis([-1, len(data), 0, 450])

plt.figure(2)
plt.title('Tutti 2008-2011 by category')
plt.bar(range(len(tutti)), tutti, align='center')
plt.plot(avarage, '+', color="#ff6000", lw=2)
plt.xticks(range(len(categories)), sorted(categories))
plt.axis([-1, len(tutti), 0, 450])
plt.show()
