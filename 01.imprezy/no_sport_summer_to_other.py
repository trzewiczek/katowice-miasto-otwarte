import meerkat
import math
import matplotlib.pyplot as plt

t = meerkat.Table('IMPREZY_RAZEM_REFINED_AND_PYTHONED.csv', header=False)

categories = list(set(t.column(1)))
categories.remove('K')
categories.remove('S')

tmp  = { k: 0  for k in sorted(categories) }

agg = {}
for c, m, y in zip(t.column(1), t.column(4), t.column(5)):
    if m and 2008 <= y <= 2011:
        if c == 'K':
            c = 'L'
        if c == 'S':
            c = 'I'

        q = 'summer' if m in [7, 8, 9] else 'other'

        agg.setdefault(q, dict(tmp))
        agg[q][c] += 1

import json
print json.dumps(agg, indent=4)

plt.figure(1)
for i, title in enumerate(agg, 1):
    data = [ e / 4.0 for k, e in sorted(agg[title].items()) ]
    keys = [ k for k, e in sorted(agg[title].items()) ]

    plt.subplot("21%s" % i)
    plt.title("Avarage in %s by category" % title)
    plt.bar(range(len(data)), data, align='center')
    plt.axis([-1, len(data), 0, 150])
    plt.xticks(range(len(keys)), keys)

plt.show()
        
