from random import randint
from pprint import pprint


rand_bits = [ randint(0,1) for i in range(12)]
sum_bit = sum(rand_bits)

rand_strs = [str(bit) for bit in rand_bits]
inlined_strs = "".join(rand_strs)

max_pos = inlined_strs.find('1')

print("{} = {} ({})".format(rand_bits, sum_bit, max_pos))
print(inlined_strs)
