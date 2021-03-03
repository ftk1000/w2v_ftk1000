# w2v_ftk1000

[полезная книжка https://colab.research.google.com/github/jakevdp/PythonDataScienceHandbook/blob/master/notebooks/Index.ipynb](https://colab.research.google.com/github/jakevdp/PythonDataScienceHandbook/blob/master/notebooks/Index.ipynb)<br>
[]()<br>

## Chris McCormick's Tutorials 
[2016: word2vec-tutorial-the-skip-gram-model (Part-1)](http://mccormickml.com/2016/04/19/word2vec-tutorial-the-skip-gram-model/)<br>
[2016: word2vec-tutorial-Negative Sampling (Part-2)](http://mccormickml.com/2017/01/11/word2vec-tutorial-part-2-negative-sampling/)<br>[]()<br>
[]()<br>
[]()<br>

[]()<br>

## Chris Olah's Tutorials 
[Deep Learning, NLP, and Representations](http://colah.github.io/posts/2014-07-NLP-RNNs-Representations/)<br>
[]()<br>
[]()<br>

## TF on embedding
[This document details feature columns. Think of feature columns as the intermediaries between raw data and Estimators.](https://github.com/tensorflow/docs/blob/master/site/en/r1/guide/feature_columns.md)<br>
[весьма удачная иллюстрация векторного вложения слов и выделения компонент разными методами http://projector.tensorflow.org/](http://projector.tensorflow.org/)<br>


# w2v
* [2013: Distributed Representations of Words and Phrases and their Compositionality, by Tomas Mikolov, Ilya Sutskever, Kai Chen, Greg Corrado, Jeffrey Dean](https://arxiv.org/abs/1310.4546)<br>
* [31+ implementations of word2vec in Py et al](https://paperswithcode.com/paper/distributed-representations-of-words-and-1#code)<br>
* [VERY NICE: 2017: Lilian Weng: learning-word-embedding by Lil Log](https://lilianweng.github.io/lil-log/2017/10/15/learning-word-embedding.html#loss-functions)<br>
* [wevi: word embedding visual inspector](https://ronxin.github.io/wevi/)<br>

## W2V and Matrix Factorization
* [2014: Neural Word Embedding as Implicit Matrix Factorization. Omer Levy and Yoav Goldberg](https://wordrepr.danieldk.eu/levy-2014.pdf)<br>
* [2016: skipgram-isnt-matrix-factorisation](http://building-babylon.net/2016/05/12/skipgram-isnt-matrix-factorisation/)<br>
* [REDDIT: word2vec_is_actually_just_matrix_factorization](https://www.reddit.com/r/MachineLearning/comments/2m34kp/word2vec_is_actually_just_matrix_factorization/)<br>
### Unifying Word Embeddings and Matrix Factorization by Kian Kenyon-Dean
* [2019: Part 1: The problems of viewing Word2vec as a neural network, and reviewing Levy & Goldberg’s attempted solution.](https://medium.com/radix-ai-blog/unifying-word-embeddings-and-matrix-factorization-part-1-cb3984e95141)<br>
* [2019: Part 2: Finding the true explicit matrix factorization formulation of Word2vec](https://medium.com/radix-ai-blog/unifying-word-embeddings-and-matrix-factorization-part-2-a0174ace78b8)<br>
* [2019: Part 3: Implementing Word2vec as matrix factorization… in TensorFlow 2.0!](https://medium.com/radix-ai-blog/unifying-word-embeddings-and-matrix-factorization-part-3-4269d9a07470)<br>
* []()<br>
* []()<br>
* []()<br>


[reddit: word2vec is actually just matrix factorization](https://www.reddit.com/r/MachineLearning/comments/2m34kp/word2vec_is_actually_just_matrix_factorization/)<br>
[2016:  BENJAMIN: Skipgram isn't Matrix Factorisation](http://building-babylon.net/2016/05/12/skipgram-isnt-matrix-factorisation/)<br>
[]()<br>


## essential files for building word2vec models using C code 
[Run C code from py on COLAB: Lecture-6A-Fortran-and-C](https://colab.research.google.com/github/jrjohansson/scientific-python-lectures/blob/master/Lecture-6A-Fortran-and-C.ipynb)<br>
## py wrapper to play with the model


[w2v demo](https://github.com/Suji04/NormalizedNerd/blob/master/Introduction%20to%20NLP/Word2Vec.ipynb)<br>
[w2v demo on colab Malstm_quoraquestionpair.ipynb](https://colab.research.google.com/drive/1CXdKsk9mvHiuFMRowELp0NDP5__bsuVy#scrollTo=tfWFxxNGXqDr)<br>
  - downloads data from Kaggle compeition (Quota questions) and w2v embedding from s3.amazon (see below)
  - !wget -P /root/input/ -c "https://s3.amazonaws.com/dl4j-distribution/GoogleNews-vectors-negative300.bin.gz"
  - model malstm saved as model.h5<br>
<br>

[Word2Vec: Obtain word embeddings](https://chainer-colab-notebook.readthedocs.io/en/latest/notebook/official_example/word2vec.html)<br>
  - has some code + key ideas of the algos<br>
[MY COLAB: Copy of Malstm_quoraquestionpair.ipynb](https://colab.research.google.com/drive/1deTNTvPlzO0oRLCuyf377AviWXiS7xRm)<br>
[]()<br>
[]()<br>
[]()<br>
[как скачать данные из кагла в колаб](https://www.kaggle.com/c/made-thousand-facial-landmarks/discussion/143089)<br>

# w2v in py
[2018: implement-your-own-word2vecskip-gram-model-in-python](https://www.geeksforgeeks.org/implement-your-own-word2vecskip-gram-model-in-python/?ref=rp)<br>
[2018: python-word-embedding-using-word2vec](https://www.geeksforgeeks.org/python-word-embedding-using-word2vec/)<br>
[Kaggle: gensim-word2vec-tutorial](https://www.kaggle.com/pierremegret/gensim-word2vec-tutorial)<br>

[Chainer: Word2Vec: Obtain word embeddings](https://chainer-colab-notebook.readthedocs.io/en/latest/notebook/official_example/word2vec.html)<br>
[]()<br>
[]()<br>

# w2v in C
[google's code](https://code.google.com/archive/p/word2vec/)<br>
[]()<br>

