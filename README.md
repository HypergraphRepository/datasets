# Info

![preview](https://i.ibb.co/qJbtfrS/Screenshot-2024-01-08-alle-11-54-22.png)

You can find the live website at [Site](https://hypergraphrepository.di.unisa.it/)

# Add your dataset here
To add your dataset to this repository, you can follow the steps below:
- Fork this repository
- Add a **single** dataset to the repository with the following structure:
```
dataset_name
├── README.md
├── dataset_name.hgf
├── categories.info
└── otherfiles.any
```
- Open a pull request to this repository
- Actions will run to check the files
- If the files are valid, at least 1 reviewer will be assigned to the pull request
- If the reviewer approves the pull request, the dataset will be merged into the repository

We have 3 mandatory files:
- README.md
- dataset_name.hgf
- categories.info
However, you can add other files if you want, specifying them in the README.md file for what they are used.
For example, you can add a file containing labels for the nodes or hyperedges.

# File formats

The README.md file should contain a description of the dataset and the source of the data in standard markdown format.

The hypergraph file should be in the following format:
```
16 4
1=true 2=true 3=true
4=true 5=true 6=true 7=true 8=true 9=true 10=true 
11=true 12=true 13=true 14=true 15=true 
9=true 10=true 11=true 13=true 16=true
```
The first line contains the number of nodes and the number of hyperedges.
The following lines represent a hyperedge and each number represents a node.

The format of the categories.info file should be:
```
domain
---
category1
category2
category3
```

Do you need an example? Check out this list:
- Categories:
  - Biological Networks
  - Collaboration Networks
  - Citation Networks
  - Dynamic Networks
  - Ecology Networks
  - Economic Networks
  - Email Networks
  - Massive Network Data
  - Miscellaneous Networks
  - Online communities 
  - Online reviews 
  - Power Networks
  - Proximity Networks
  - Recommendation Networks
  - Social Networks
  - Telecom networks 
- Types:
  - Nature of the relation
    - Homogeneous
    - Heterogeneous
    - Weighted
  - Directionality of the relation
    - Directed
    - Undirected 
  - Size of the relation
    - K-uniform
    - Non-uniform
  - Temporal dimension
    - Static
    - Temporal
  - Node/Hyperedge attributes
    - Attributed
    - Signed
  
# Want to be a reviewer?

If you want to be a reviewer, please open an issue in this repository following the template 

# Stats

![Alt](https://repobeats.axiom.co/api/embed/6ab4b67f9c1ef80bc02370d364ef65db4ec40284.svg "Repobeats analytics image")

# Star History

[![Star History Chart](https://api.star-history.com/svg?repos=HypergraphRepository/datasets&type=Date)](https://star-history.com/#HypergraphRepository/datasets&Date)