# Step1. Initialize the constants N and d
n=4
d=0.7
# Step2. Assume that all page ranks are 1.0 at the beginning
prA = 1.0
prB = 1.0
prC = 1.0
prD = 1.0
# Step3. In a for/while loop, iteratively update the page ranks of all the pages
for x in range(100):
   prA = ((1 - d) / n) + d*((prC) / 3)
   prB = ((1 - d) / n) + d*((prA) / 2 + (prC) / 3)
   prC = ((1 - d) / n) + d*((prA) / 2 + (prD) / 1)
   prD = ((1 - d) / n) + d*((prC) / 2 + (prB) / 1)

# Step4. Print the page ranks
print("PrA= ", prA)
print("PrB= ", prB)
print("PrC= ", prC)
print("PrD= ", prD)