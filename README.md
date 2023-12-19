# Info

WIP
You can find the live website at [Site](http://hypergraphrepository.di.unisa.it/)

# Add your dataset here
To add your dataset to this repository, you can follow the steps below:
- Fork this repository
- Add a **single** dataset to the repository with the following structure:
```
dataset_name
├── README.md
├── dataset_name.hg
└── categories.info
```
- Open a pull request to this repository
- Actions will run to check the files
- If the files are valid, at least 1 reviewer will be assigned to the pull request
- If the reviewer approves the pull request, the dataset will be merged into the repository


# File formats

The README.md file should contain a description of the dataset and the source of the data in standard markdown format.

The hypergraph file should be in the following format:
```
0,1
2,3
4,5,6
```
Where each line represents a hyperedge and each number represents a node.

The format of the categories.info file should be:
```
category1
category2
category3
```

# Want to be a reviewer?

If you want to be a reviewer, please open an issue in this repository following the template 

# Stats

![Alt](https://repobeats.axiom.co/api/embed/6ab4b67f9c1ef80bc02370d364ef65db4ec40284.svg "Repobeats analytics image")