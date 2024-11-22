## Introduction

Simple summary of general DVC commands

### Setting a remote location

You have to create the remote location for your data.
DVC allows local and remote locations (like S3)

```
dvc remote add -d myremote /path/to/data
```

### Pushing data

```
dvc push [Optional --remote to select the remote you want]
```

### Pulling data

```
dvc pull [Optional --remote to select the remote you want]
```

### Adding data to dvc

To add data, just type the command
```
dvc add mydata
```

DVC will then update the .gitignore file so the data are not saved in github

To follow up, you have to do the command:
```
git add .gitignore mydata.csv.dvc
```

### Listing the data from a repository

With DVC you can list the data from a github repo even if the data are stored somewhere else.

```
dvc list https://github.com/myrepo myfolder
```

You will have a list of the data files and the dvc files.

### Getting the data from a repo

```
dvc get https://github.com/myrepo myfolder
```
The downside of dvc get is you lose track of the origin of the file.
To keep track about the source of the data, you can use import instead

```
dvc import https://github.com/myrepo myfolder/myfile.csv -o myfile.csv
```

Once you have loaded the data, you can check if there is an update

```
dvc update myfile.csv.dvc
```
