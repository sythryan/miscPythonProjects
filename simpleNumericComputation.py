# Some calculations.
fred = 18
barney = FRED = 44;   #note: case sensitive
bill = (fred + barney * FRED - 10)
alice = 10 + bill / 100
frank = 10 + float(bill) / 100
print "fred = ", fred
print "bill = ", bill
print "alice = ", alice
print "frank = ", frank
print

# Each variable on the left is assigned the corresponding value on the right.
fred, alice, frank = 2*alice, fred - 1, bill + frank
print "fred = ", fred
print "alice = ", alice
print "frank = ", frank
print

# Exchange w/o a temp.
fred, alice = alice, fred
print "fred = ", fred
print "alice = ", alice
print

# Python allows lines to be continued by putting a backslash at the end of
# the first part. 
fred = bill + alice + frank - \
       barney
print "fred = ", fred
print

# The compiler will also combine lines when the line break in contained
# in a grouping pair, such as parens.
joe = 3 * (fred + 
        bill - alice)
print "joe = ", joe