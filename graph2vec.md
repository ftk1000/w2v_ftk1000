# Knowledge Graphs

[Knowledge Graph Embeddings on COLAB](https://colab.research.google.com/github/HybridNLP2018/tutorial/blob/master/02_knowledge_graph_embeddings.ipynb)<br>
[git hub: Holographic Embeddings of Knowledge Graphs](https://github.com/mnick/holographic-embeddings)<br>
[2015: Holographic Embeddings of Knowledge Graphs, Maximilian Nickel1, Lorenzo Rosasco and Tomaso Poggio](https://arxiv.org/pdf/1510.04935.pdf)<br>
  - In this work we are concerned with learning from knowledge graphs (KGs), i.e., knowledge bases which model facts as instances
of binary relations (e.g., bornIn(BarackObama, Hawaii)). This form of knowledge representation can be interpreted as a multigraph, where entities correspond to nodes, facts
correspond to typed edges, and the type of an edge indicates the kind of the relation.
  - Recently, vector space embeddings of knowledge graphs have received considerable attention, as they can be used to create statistical models
of entire KGs, i.e., to predict the probability of any possible relation instance (edge) in the graph. Such models can be used to derive new knowledge from known facts (link
prediction), to disambiguate entities (entity resolution), to extract taxonomies, and for probabilistic question answering (see e.g., (Nickel, Tresp, and Kriegel, 2011; Bordes et al., 2013; Krompaß, Nickel, and Tresp, 2014)).
  - We introduce holographic embeddings (HOLE) which use the circular correlation of entity embeddings (vector representations) to create compositional representations of binary relational data. By using correlation as the compositional operator HOLE can capture rich interactions but simultaneously remains efficient to compute, easy to train, and scalable to very large datasets.
  -  Compositional vector space models have also been considered in cognitive science and natural language processing, e.g., to model symbolic structures, to represent the semantic meaning of phrases, and as models for associative memory (see e.g., Smolensky (1990); Plate (1995); Mitchell and Lapata (2008); Socher et al. (2012)). In this work, we do not only draw inspiration from these models, but we will also highlight the connections of HOLE to holographic models of associative memory.
  - Compositional vector space models provide an elegant way to learn the characteristic functions of the relations in a knowledge graph, as they allow to cast the learning task as a problem of supervised representation learning. Here, we discuss models of the form  Pr(φ_p(s, o) = 1|Θ) = σ(η_spo) = σ(r^T_p(e_s ◦ e_o))
  - ◦ : R^{d_e} × R^{d_e} → R^{d_p} denotes the compositional operator which creates a composite vector representation for the pair (s, o) from the embeddings e_s, e_o. We will discuss possible compositional operators below. Existing models for knowledge graphs are based on the following compositional operators:
    - **Tensor Product:** Compositional models using the tensor product such as RESCAL (Nickel, Tresp, and Kriegel, 2011) and the Neural Tensor Network (Socher et al.,
2013). have shown state-of-the-art performance for learning from KGs. While the tensor product allows to capture rich interactions, its main problem as a compositional operator lies in the fact that it requires a large number of parameters
    - **Concatenation, Projection, and Non-Linearity:** Another way to compute composite representations is via concatenation, projection and subsequent application of a non-linear function. Socher et al. (2013) noted, the non-linearity ψ provides only weak interactions while leading to a harder optimization problem.
    - **Non-compositional Methods:** Another class of models does not (explicitly) form compositional representations, but predicts the existence of triples from the similarity of the vector space embeddings. A major appeal of TRANSE is that it requires very few parameters and moreover is easy to train. However, this simplicity
comes also at the cost of modeling power. Wang et al. (2014) and Lin et al. (2015) proposed TRANSH and TRANSR respectively, to improve the performance of TRANSE on 1-to-N,
N-to-1, and N-to-N relations. Unfortunately, these models lose the simplicity and efficiency of TRANSE.
  - **Holographic Embeddings:** In this section, we propose a novel compositional model for KGs and relational data. To combine the expressive power of the tensor product with the efficiency and simplicity of TRANSE, we use the circular correlation of vectors to represent pairs of entities, i.e., we use the compositional operator:  a ◦ b = a ? b,  where ?: R^d × R^d → R^d denotes circular correlation: [a ? b]k = \SUM_{i=0}^d a_i b_{(k+i) mod d}. 

[]()<br>

[Unsupervised graph classification/representation learning via distances on COLAB](https://colab.research.google.com/github/stellargraph/stellargraph/blob/v1.1.0/demos/embeddings/gcn-unsupervised-graph-embeddings.ipynb)<br>
[2019: Unsupervised Inductive Graph-Level Representation Learning via Graph-Graph Proximity  , Yunsheng Bai,et al](https://arxiv.org/pdf/1904.01098.pdf)<br>

[]()<br>
[2018: A Comprehensive Survey of Graph Embedding: Problems, Techniques and Applications, 
Hongyun Cai, Vincent W. Zheng, and Kevin Chen-Chuan Chang](https://arxiv.org/pdf/1709.07604.pdf)<br>
[Hebbian Graph Embeddings, Shalin Shah, Venkataramana Kini, AI Sciences, Target Corporation](https://arxiv.org/pdf/1908.08037.pdf)<br>
[]()<br>
[]()<br>
[]()<br>
[]()<br>
