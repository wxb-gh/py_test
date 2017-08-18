# coding:gbk

colours = ['red', 'green', 'blue']
names = ['a', 'b', 'c']
for colour in colours:
    print colour

for i, colour in enumerate(colours):
    print i, ' -> ', colour

for colour in reversed(colours):
    print colour

for colour in sorted(colours, reverse=True):
    print colour

for name, colour in zip(names, colours):
    print name, '->',colour
