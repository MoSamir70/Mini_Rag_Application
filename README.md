# Mini-rag
This is a minimal implementation of the RAG model for question answering


# Requirements
Python 3.8 or later

# Install git thenck form CMD
```bash
git --version
```

## Create Folder then Craete A Repo and clone it inside this Folder


# Install Python using MiniConda Using Ubuntu
#### Video 3 Steps

```text
1- While installing Do not forget to add path checkbox 
2- Conda --version
```

```text
1- wsl --install
2- wsl --set-default-version 2
3- wsl --install Ubuntu    --> U Capital
4- open Ubuntu form start Menu
5- Sudo apt Update + Ur Passward --> hidden
6- cd /mnt/parition/complete path  --> partition letter Must be Small
7- cd ~  then wget https://repo.anaconda.com/miniconda/Miniconda3-latest-Linux-x86_64.sh
8- chmode +x Miniconda3-latest-Linux-x86_64.sh  
9-  ./Miniconda3-latest-Linux-x86_64.sh --> Q + yes + yes 
10- Close and open Ubuntu terminal Again 
11- conda create -n mini-rag python=3.8
12- export PS1="\[\033[01;32m\]\u@\h:\w\n\[\033[00m\]\$ "
13- conda activate mini-rag
```


# Create a new environment using the following command:

```bash
conda create -n mini-rag python=3.8
```
# Activate the environment:

```bash
conda activate mini-rag
```

# Vid4 : Create a new branch tut-001 & SetUp Files

```text
.gitignore
Readme
License
Requirments.txt
Assests Folder + .gitkeep
.env --> Configurations = Upper Letters
.env.examples
Push all on github
```

```text
Requirments Hints:

1- Keep curser in last line
2- Mention Package == Version
```

# Install the required packages

```bash
pip install -r requirements.txt
```
r -> install all packages in ones


# Setup the environment variables

```bash
cp .env.example .env
```
Set your environment variables in the .env file. Like OPENAI_API_KEY value.