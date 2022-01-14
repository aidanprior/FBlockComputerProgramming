

# write a function that will take in a number,
# and then return 4 times that number plus 6
def jan11a( x ):
    # write your solution here
    return 4*x + 6


print( jan11a( 6 ) ) # Should be 30
print( jan11a( 7 ) ) # Should be 34
print( jan11a( 8 ) ) # Should be 38

print()

for x in range(10):
    print( jan11a( x ))

# Expected output
# 6
# 10
# 14
# 18
# ...