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
