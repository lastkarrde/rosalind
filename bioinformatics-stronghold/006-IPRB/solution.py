"""
Pretty horrible. Worked out the probabilities by hand.
"""

k = 25
m = 18
n = 28
p = k + m + n

s1 = ((k/p) * ((k-1) / (p-1))) + ((k/p) * (m / (p-1))) + ((k/p) * (n / (p-1)))

s2 = ((m/p) * (k / (p-1))) + ((m/p) * ((m-1) / (p-1)) * (3/4)) + ((m/p) * (n / (p-1)) * (1/2))

s3 = ((n/p) * (k / (p-1))) + ((n/p) * (m / (p-1)) * (1/2))

print(round(s1+s2+s3, 5))