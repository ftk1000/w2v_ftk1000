# -*- coding: utf-8 -*-
"""w2v_pytorch.ipynb


w2v_pytorch.ipynb

Implementing word2vec in PyTorch (skip-gram model)

https://towardsdatascience.com/implementing-word2vec-in-pytorch-skip-gram-model-e6bae040d2fb

2021.03.11
"""

import torch
from torch.autograd import Variable
import numpy as np
import torch.functional as F
import torch.nn.functional as F

corpus = [
    'he is a king',
    'she is a queen',
    'he is a man',
    'she is a woman',
    'warsaw is poland capital',
    'berlin is germany capital',
    'paris is france capital',
]

def tokenize_corpus(corpus):
    tokens = [x.split() for x in corpus]
    return tokens

tokenized_corpus = tokenize_corpus(corpus)

print('tokenized_corpus=',tokenized_corpus)

vocabulary = []
for sentence in tokenized_corpus:
    for token in sentence:
        if token not in vocabulary:
            vocabulary.append(token)

word2idx = {w: idx for (idx, w) in enumerate(vocabulary)}
idx2word = {idx: w for (idx, w) in enumerate(vocabulary)}

vocabulary_size = len(vocabulary)

print('vocabulary_size=',vocabulary_size)
print('vocabulary=',vocabulary)



# We can now generate pairs center word, context word. 
# Let’s assume context window to be symmetric and equal to 2.
window_size = 2
idx_pairs = []
# for each sentence
for sentence in tokenized_corpus:
    indices = [word2idx[word] for word in sentence]
    # for each word, threated as center word
    for center_word_pos in range(len(indices)):
        # for each window position
        for w in range(-window_size, window_size + 1):
            context_word_pos = center_word_pos + w
            # make soure not jump out sentence
            if context_word_pos < 0 or context_word_pos >= len(indices) or center_word_pos == context_word_pos:
                continue
            context_word_idx = indices[context_word_pos]
            idx_pairs.append((indices[center_word_pos], context_word_idx))

idx_pairs = np.array(idx_pairs) # it will be useful to have this as numpy array

N=3
print(f'number of idx_pairs={len(idx_pairs)};  first {N} idx_pairs=',idx_pairs[:N])

def get_input_layer(word_idx):
    x = torch.zeros(vocabulary_size).float()
    x[word_idx] = 1.0
    return x
get_input_layer(5)

embedding_dims = 2
W1 = Variable(torch.randn(embedding_dims, vocabulary_size).float(), requires_grad=True)
W2 = Variable(torch.randn(vocabulary_size, embedding_dims).float(), requires_grad=True)
num_epochs = 200
learning_rate = 0.001

for epo in range(num_epochs):
    loss_val = 0
    for data, target in idx_pairs:
        x = Variable(get_input_layer(data)).float()
        y_true = Variable(torch.from_numpy(np.array([target])).long())

        z1 = torch.matmul(W1, x)
        z2 = torch.matmul(W2, z1)
    
        log_softmax = F.log_softmax(z2, dim=0)

        loss = F.nll_loss(log_softmax.view(1,-1), y_true)
        # loss_val += loss.data[0]
        # see a comment from yogi-bp commented on Oct 17, 2019 in https://gist.github.com/mbednarski/da08eb297304f7a66a3840e857e060a0
        # Please change loss_val += loss.data[0] to loss_val += loss.item() to avoid the error IndexError: 
        # invalid index of a 0-dim tensor. Use tensor.item() to convert a 0-dim tensor to a Python number
        loss_val += loss.item()
        loss.backward()
        W1.data -= learning_rate * W1.grad.data
        W2.data -= learning_rate * W2.grad.data

        W1.grad.data.zero_()
        W2.grad.data.zero_()
    if epo % 10 == 0:    
        print(f'Loss at epo {epo}: {loss_val/len(idx_pairs)}')

def similarity_words(word1,word2):
  v1 = W2[word2idx[word1]]
  v2 = W2[word2idx[word2]]
  
  cos_sim = torch.dot(v1,v2)/(torch.norm(v1)*torch.norm(v2))
  print(f'cosine dist between {word1} and {word2} is {cos_sim}')
  return cos_sim

res=similarity_words(word1='she', word2='king')
res=similarity_words(word1='she', word2='queen')

# def similarity(v,u):
#   cos_sim = torch.dot(v,u)/(torch.norm(v)*torch.norm(u))
#   return cos_sim  

# similarity(W2[word2idx["she"]], W2[word2idx["king"]]) # = 0.5035
# similarity(W2[word2idx["she"]], W2[word2idx["queen"]]) # = 0.1582






#     https://colab.research.google.com/drive/1JrD8-Nt5hkix_t7DmNCj5FglIM_G_BPa
