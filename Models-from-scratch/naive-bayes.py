"""
1- read dataset using pandas
2- seperate the dataset based on label
3- train test split
4- Insert data in vocab, bag_of_words dictionaries
5- Calculate Prior probability
6- Calculate Conditional probability
7- Calculate tp,fn,fp,tn
8- Calculate Accuracy, Precision, Recall, F1-score
"""

import math
import pandas as pd
from collections import defaultdict



# Step 1- Read Dataset
df = pd.read_csv('data.csv')

vocab = defaultdict(int)    # An empty dictionary to store all words appearing in dataset
bow_spam = defaultdict(int) # An empty dictionary to store spam messages only
bow_ham = defaultdict(int)  #  "      "     "      "     "      "  ham messages only
cond_spam = defaultdict(int)# An empty dictionary to store P(word | spam)
cond_ham = defaultdict(int) #  "      "     "      "     " P(word | ham)



# Step 2- Seperate spam & ham messages
spam_rows = df[df['tag'] == 'spam']
ham_rows = df[df['tag'] == 'ham'][:747]
# print(spam_rows)
# print(ham_rows)



# Step 3- Train test split
train_size = int(len(spam_rows) * 0.8)

test_spam = spam_rows[train_size:]
test_ham = ham_rows[train_size:]

spam_rows = spam_rows[:train_size]
ham_rows = ham_rows[:train_size]

# print(spam_rows)
# print(ham_rows)



# Step 4- Inserting data in vocab, bag_of_words(spam\ham)
for row in spam_rows['text']:
    for word in row.split(' '):
        vocab[word.lower()] += 1        # count the no. appearence of the word in voacb
        bow_spam[word.lower()] += 1     #   "    "   "    "         "   "    "  in spam bag

# print(vocab)
# print(bow_spam)


for row in ham_rows['text']:
    for word in row.split(' '):
        vocab[word.lower()] += 1
        bow_ham[word.lower()] += 1    # count the no. appearence of the word in ham bag

# print(vocab)
# print(bow_ham)



# Step 5- Calculate Prior Prob
prior_spam = len(spam_rows) / (len(spam_rows) + len(ham_rows))
prior_ham = len(ham_rows) / (len(spam_rows) + len(ham_rows))

# print(prior_spam)
# print(prior_ham)



# Step 6- Calculate conditional prob
for word in vocab:
    cond_spam[word] = float((bow_spam[word] + 1) / (len(bow_spam) + len(vocab)))  # Performing Laplace Smoothing by adding 1 in bow_spam[word]
    cond_ham[word] = float((bow_ham[word] + 1) / (len(bow_ham) + len(vocab)))



# Step 7- Calculate tp,fn,tn,fp (Testing phase)
tp=fp=fn=tn=0

for row in test_spam['text']:
    temp_prob_spam = prior_spam
    temp_prob_ham = prior_ham
    for word in row.split(' '):
        if word in bow_spam:
            temp_prob_spam += math.log(cond_spam[word])
        if word in bow_ham:
            temp_prob_ham += math.log(cond_ham[word])
    
    if (temp_prob_spam >= temp_prob_ham):
        tp += 1
    else:
        fn += 1

for row in test_ham['text']:
    temp_prob_spam = prior_spam
    temp_prob_ham = prior_ham
    for word in row.split(' '):
        if(word in bow_ham):
            temp_prob_ham += math.log(cond_ham[word])
        if(word in bow_spam):
            temp_prob_spam += math.log(cond_spam[word])
    
    if temp_prob_spam <= temp_prob_ham:
        tn += 1
    else:
        fp += 1

# print(tp, fn, fp, tn)



# Step 8- Calculate Accuracy, Precision, Recall, F1-score
acc = (tp + tn) / (tp + fn + tn + fp)
prec = tp / (tp + fp)
rec = tp / (tp + fn)
f1 = 2 * ((prec * rec) / (prec + rec))

print(f"Accuracy: {acc}")
print(f"Precision: {prec}")
print(f"Recall: {rec}")
print(f"F1 score: {f1}")

# print("Everything is fine!")