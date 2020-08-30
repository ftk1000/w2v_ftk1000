# Mikolov Papers

[2013.06: Linguistic Regularities in Continuous Space Word Representations,
Tomas Mikolov, Wen-tau Yih, Geoffrey Zweig, Microsoft Research, Redmond, WA 98052](https://www.aclweb.org/anthology/N13-1090.pdf)<br>
  - we examine the vector-space word representations
that are implicitly learned by the input-layer
weights. We find that these representations
are surprisingly good at capturing syntactic
and semantic regularities in language, and
that each relationship is characterized by a
relation-specific vector offset
  - For example, the male/female
relationship is automatically learned, and with
the induced vector representations, “King -
Man + Woman” results in a vector very close
to “Queen.”
   - We demonstrate that the word
vectors capture syntactic regularities by means
of syntactic analogy questions (provided with
this paper), and are able to correctly answer
almost 40% of the questions. We demonstrate
that the word vectors capture semantic regularities by using the vector offset method to
answer SemEval-2012 Task 2 questions.
   - In Section 2, we discuss related work; Section
3 describes the recurrent neural network language
model we used to obtain word vectors; Section 4 discusses the test sets; Section 5 describes our proposed
vector offset method; Section 6 summarizes our experiments, and we conclude in Section 7.
   -  **CHALLENGE**: Early neural network language
models for distributed word representations
demonstrated outstanding performance in terms of
word-prediction, but also **the need for more computationally efficient models**. 
    - This has been addressed
by subsequent work using hierarchical prediction
(Morin and Bengio, 2005; Mnih and Hinton, 2009;
Le et al., 2011; Mikolov et al., 2011b; Mikolov et
al., 2011a).
    - This has been addressed
by subsequent work using **hierarchical prediction**
(Morin and Bengio, 2005; Mnih and Hinton, 2009;
Le et al., 2011; Mikolov et al., 2011b; Mikolov et
al., 2011a). 
   - The word representations we study are learned by a
recurrent neural network language model (Mikolov
et al., 2010)

[]()<br>

[]()<br>

[]()<br>

[]()<br>

[]()<br>

[]()<br>

