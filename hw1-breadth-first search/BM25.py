import numpy as np
dataset = np.genfromtxt('table.csv', delimiter=',', skip_header=True)
import math

k = 1.2
b = 0.75
n = 40
print(dataset)
word1_frequency = 0
word2_frequency = 0
sums = dataset.sum(0)
print(sums)
print(sums[2])
print("________________")
#counts if word 1 and word2 appears in each document
for row in dataset:
    if row[2] != 0:
        word1_frequency = word1_frequency + 1
    if row[3] != 0:
        word2_frequency = word2_frequency + 1

print("df(word1) = ", word1_frequency)
print("df(word2) = ", word2_frequency)


# Step 1: for loops to calculate IDF for Word1 and Word2
print("________________")
#get idf for each word
idf_word1 = math.log((n - word1_frequency + 0.5)/(word1_frequency + 0.5))
idf_word2 = math.log((n - word2_frequency + 0.5)/(word2_frequency + 0.5))
print("idf for word1 = ", idf_word1)
print("idf for word2 = ", idf_word2)
# Step 2: for loop to calculate L
print("________________")
avg_document_length = sums[1]/n #gets average document length
print("avg document length = ", avg_document_length)
# Step 3: create a dictionary/list to maintain BM25 for each document
bm25 = [n]

# Step 4: for loop to calculate BM25 for each document
print("________________")
for row in dataset:
    bm25.append(((row[2]*(k+1))/(row[2]+(k*(1-b+b*(row[1]/avg_document_length))))) + ((row[3]*(k+1))/(row[3]+(k*(1-b+b*(row[1]/avg_document_length))))))#bm25 formula for each document
# Step 5: display documents sorted by score
bm25.sort()#sort scores ascending
print(bm25)