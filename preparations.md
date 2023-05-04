# Preparations before running BABS

## Prepare conda env `showcase`

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
