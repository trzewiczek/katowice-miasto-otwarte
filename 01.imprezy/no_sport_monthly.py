import matplotlib.pyplot as plt
import meerkat

t = meerkat.Table('IMPREZY_RAZEM_REFINED_AND_PYTHONED.csv', header=False)

agg = {}
for m, y in zip(t.column(4), t.column(5)):
    if 2008 <= y <= 2011 and m:
        q = '%s-%2s' % (y, m)

        agg.setdefault(q, 0)
        agg[q] += 1


data = [ v for k, v in sorted(agg.items()) ]
keys = [ k for k, v in sorted(agg.items()) ]

print sorted(agg.items())

plt.title("Tutti - monthly 2008-2011")
plt.bar(range(len(data)), data, align='center')
plt.xticks(range(0, len(keys), 12), keys[::12])
plt.show()
