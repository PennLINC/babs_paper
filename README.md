# babs_paper

This repository includes scripts and other materials for BABS manuscript.

Here,
* `showcase` means the application of BABS to HBN dataset.
## Main folder
* Preparations for the application:
    * [preparations.md](preparations.md):
        * Preparations before running BABS commmands
    * [prep_babs-init_cmd.py](prep_babs-init_cmd.py):
        * Prepare full command of `babs-init`
* YAML file used for showcase:
    * [showcase_config_fmriprep_anatonly.yaml](showcase_config_fmriprep_anatonly.yaml) was directly used in the showcase;
    * [figure_showcase_config_fmriprep_anatonly.yaml](figure_showcase_config_fmriprep_anatonly.yaml):
        * Used for Supplementary Figure 1. 
        * Copied from above [showcase_config_fmriprep_anatonly.yaml](showcase_config_fmriprep_anatonly.yaml), only with some minor comments removed.

## Folder `showcase_messages`
* Printed messages from `babs-status` during showcase:
    * `message_babs-status*.txt`
        * 1st round of submitted jobs finished: [message_babs-status_2023-05-19_11-06.txt](message_babs-status_2023-05-19_11-06.txt)
        * After resubmitting failed jobs + they also finished: [message_babs-status_2023-05-24_10-09.txt](message_babs-status_2023-05-24_10-09.txt)
    * `figure_babs-status_msg.txt`:
        * Used for Figure 4



