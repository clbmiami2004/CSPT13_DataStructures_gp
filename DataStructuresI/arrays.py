# Linear time iterate over all items
arr = [12, 23, 56, 87, 14]  # n = 5

for num in arr: # O(n * 1) ==> O(n)
    print(num) # O(1)
for num in arr: # O(n * 1) ==> O(n)
    print(num) # O(1)

    # O(n) + O(1) => O(n)
    # O(n * 1) + O(n * 1) + O(1)
    # O(2n) + O(1) => O(n) + O(1) => O(n)

# constant time lookup
print(arr[3]) # O(1)

# quadratic time nested iteration
for x in arr: # O(n)
    for y in arr: # O(n) => O(n^2)  This becomes a n^2 becuase is nested in the loop
        print(x, y) # O(1) => O(1 * n^2)

# O(n^2) + O(n) + O(1 * n^2)
# O(2n^2) + O(n) => O(n^2) + O(n^2)

# O(n^2) Cuadratic 
# If we add another loop to it will be elevated to the n^3 => O(n^3)

# ===============================================================================================
# We have to make sure to keep this in mind when using so many nested loops when writing code.
# If we had 10 items in an array, and we have 3 different loops, this would look like this:
# 10 * 10 * 10 = 1000
# So we would have to do 1000 operations in order to be able to get our results.


# can we do better?

