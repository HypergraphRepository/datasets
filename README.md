![Uptime Robot status](https://img.shields.io/uptimerobot/status/m795798027-01f7c737628356e8136c7bed)

## General Info

![preview](https://i.ibb.co/hCkPWkr/Screenshot-2024-03-01-alle-16-16-46.png)
You can find the live website at [Site](https://hypergraphrepository.di.unisa.it/)

## Cite us

If you use this repository in your research, please cite us as follows:
```
@article{hgRepo,
title = {HypergraphRepository: A Community-driven and Interactive Hypernetwork Data Collection},
authors = {Alessia Antelmi and Daniele De Vinco and Carmine Spagnuolo},
journal = {},
volume = {},
number = {},
pages = {},
year = {2024},
doi = {}
}
```

## Add your dataset here
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
- If the reviewers approve the pull request, the dataset will be merged into the repository

We have 3 mandatory files:
- README.md
- dataset_name.hgf
- categories.info

However, you can add other files if you want, specifying them in the README.md file for what they are used.
For example, you can add a file containing labels for the nodes or hyperedges, see section [Adding metadata](#adding-metadata) for more information.

## What do you need

### Info on the dataset
The README.md file should contain a description of the dataset and the source of the data in standard markdown format.

### Define your HyperNetwork
The hypergraph file should be in the **HGF** format. The HGF format is a simple format to represent hypergraphs. The format is as follows:
The first line contains the number of nodes and the number of hyperedges.
The following lines represent a hyperedge and each number represents a node.

generic format:
```
<# of nodes> <# of edges>
<id1>=<weight1> <id2>=<weight2> ... <id10>=<weight10>
.
.
.
<id1000>=<weight1000> <id1001>=<weight1001> ... <id1234>=<weight1234>
```

example with weights as float numbers:
```
16 4
1=0.5 2=0.5 3=0.5
4=1.0 5=1.0 6=1.0 7=1.0 8=1.0 9=1.0 10=1.0
11=1.0 12=1.0 13=1.0 14=1.0 15=1.0
9=0.8 10=0.8 11=0.8 13=0.8 16=0.8
```

example without weights as boolean:
```
16 4
1=true 2=true 3=true
4=true 5=true 6=true 7=true 8=true 9=true 10=true 
11=true 12=true 13=true 14=true 15=true 
9=true 10=true 11=true 13=true 16=true
```

### Describe your network

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

## Adding metadata

Using 
See [NDC-classes](https://github.com/HypergraphRepository/datasets/tree/main/NDC-classes) as a pratical example.
  
# Want to be a reviewer?

Do you want to be a reviewer for this repository?
If you would like to help us mantain this repository and enhance the quality of the datasets to boost your research
, please open an issue in this repository following the template "Become a reviewer" at the following link: [Issue](https://github.com/HypergraphRepository/datasets/issues/new/choose)

# Stats

![Alt](https://repobeats.axiom.co/api/embed/6ab4b67f9c1ef80bc02370d364ef65db4ec40284.svg "Repobeats analytics image")

# Star History

[![Star History Chart](https://api.star-history.com/svg?repos=HypergraphRepository/datasets&type=Date)](https://star-history.com/#HypergraphRepository/datasets&Date)
