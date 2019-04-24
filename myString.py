table = str.maketrans('t', 'T')
print(table)
print('this is an incredible test'.translate(table))
a = "The Middle by Jimmy Eat World"
print(a.center(113))
print(a.find('By'))

# width = int(input('Please enter width: '))
# price_width = 10
# item_width = width - price_width

# header_fmt = '{{:{}}}{{:>{}}}'.format(item_width, price_width)
# fmt        = '{{:{}}}{{:>{}.2f}}'.format(item_width, price_width)

# print('=' * width)

# print(header_fmt.format('Item', 'Price'))

# print('-' * width)

# print(fmt.format('Apples', 0.4))
# print(fmt.format('Pears', 0.5))
# print(fmt.format('Cantaloupes', 1.92))
# print(fmt.format('Dried Apricots (16 oz.)', 8))
# print(fmt.format('Prunes (4 lbs.)', 12))

# print('=' * width)
# import math
# pi=math.pi
# print('012345678901234567890')
# print('{0:+.2}\n{0:+.2}'.format(pi,-pi))

# format = "Hello, %s. %s enough for ya%s"
# values = ('Sir', 'world','!')
# print(format % values)
# print("{}, {} and {}".format("first", "second", "third"))
# print("{2}, {1} and {0}".format("first", "second", "third"))
# import string
# import math
# tmpl = "The {mod.__name__} module defines the value {mod.ascii_lowercase} for π"
# print(tmpl.format(mod=string))
# fullName=['balamurugan','ravikumar']
# caption='Mr.' + fullName[0]
# print(caption)
# print(math.pi) 