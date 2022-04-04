p = int(input("Enter p value: "))
q = int(input("Enter q value: "))
e = int(input("Enter e value: "))
plain = int(input("Enter the plaintext: "))
n = p*q
N = plain ** e
C = N % n

print("p: ", p)
print("q: ", q)
print("e: ", e)
print("n: ", n)
print("C: ", C)