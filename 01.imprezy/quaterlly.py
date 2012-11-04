import matplotlib.pyplot as plt
import meerkat

t = meerkat.Table('IMPREZY_RAZEM_REFINED_AND_PYTHONED.csv', header=False)

agg = {}
for m, y in zip(t.column(4), t.column(5)):
    if m and 2008 <= y <= 2011:

        if m < 4:
            q = '%s-01' % y
        elif m < 7:
            q = '%s-02' % y
        elif m < 10:
            q = '%s-03' % y
        else:
            q = '%s-04' % y

        agg.setdefault(q, 0)
        agg[q] += 1

data = [ v for k, v in sorted(agg.items()) ]
keys = [ k for k, v in sorted(agg.items()) ]

import json 
print sorted(agg.items())

plt.title("Tutti - quaterly 2008-2011")
plt.bar(range(len(data)), data, align='center')
plt.xticks(range(0, len(keys), 4), keys[::4])
plt.show()
