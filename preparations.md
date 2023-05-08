# Preparations before running BABS

## Prepare conda env `showcase` for large dataset application
This env was created via cloning `babs_demo` env:
```
conda create --name showcase --clone babs_demo
```
## Create a main folder
```
cd /cbica/projects/BABS
mkdir babs_showcase
cd babs_showcase
conda activate showcase
```

## Clone the input dataset
Clone the input dataset from PMACS to CUBIC:
```
datalad clone ria+ssh://[username]@[pmacs login node path]:/static/LINC_HBN#~BIDS HBN_BIDS
```
Replace `[username]` and `[pmacs login node path]` with the correct one.

Get the data needed first, otherwise my pmacs credentials will be asked during job run:
```
# in a screen session:
datalad get sub-*/ses-*/anat/ -J 2
```
