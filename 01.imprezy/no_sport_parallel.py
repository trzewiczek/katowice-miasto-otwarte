# coding: utf-8
import meerkat
import matplotlib.pyplot as plt

colors = [
    (0.0, 0.0, 0.0),
    (0.4, 0.4, 0.0),
    (0.0, 0.4, 0.4),
    (0.4, 0.0, 0.4),
    (0.7, 0.0, 0.0),
    (0.0, 0.7, 0.0),
    (0.0, 0.0, 0.7),
    (0.9, 0.0, 0.9)
]

t = meerkat.Table('IMPREZY_RAZEM_REFINED_AND_PYTHONED.csv', header=False)

categories = list(set(t.column(1)))
categories.remove('K')
categories.remove('S')

data = [(t, d) for t, d in zip(t.column(1), t.column(5))]
tmp  = { c: 0 for c in categories }

agg = {}
for t, d in data:
    if 2008 <= d <= 2011:
        if t == 'K':
            t = 'L'
        if t == 'S':
            t = 'I'

        agg.setdefault(d, dict(tmp))
        agg[d][t] += 1

import json
print json.dumps(agg, indent=4)

sorts = {}
for date in agg:
    priorities = [ k for k in sorted(agg[date], key=agg[date].get) ]
    for i, p in enumerate(priorities):
        sorts.setdefault(p, [])
        sorts[p].append(i)

print json.dumps(sorts, indent=4)

for c, (t, v) in zip(colors, sorts.items()):
    plt.plot(v, label=t, color=c, lw=2)

plt.axis([-1, 5, -1, len(categories)])
plt.title(u"Udział dziedzin w rynku wydarzeń w Katowicach")
plt.xticks(range(len(v)), sorted(agg.keys()))
plt.yticks(range(len(categories)), [u"Niezauważalny", u"Marginalny", 
           u"Przeciętny", u"Istotny", u"Ważny", u'Dominujący', u"Kluczowy"])
plt.legend(loc='upper right')
plt.show()
