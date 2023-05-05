# This is to generate `babs-init` command
# Used by BABS show case

import os.path as op

flag_where = "local"    # "cubic" or "local"

type_session = "single-ses"
bidsapp = "fmriprep"
config_yaml_filename = "showcase_config_fmriprep_anatonly.yaml"
container_name = "fmriprep-20-2-3"

if flag_where == "cubic":
    where_project = "/cbica/projects/BABS/babs_showcase"
    input_ds = "?????"   # path to the input dataset
    container_ds = op.join(where_project, bidsapp + "-container")
    container_config_yaml_file = "????"   # path to yaml file
elif flag_where == "local":
    where_root = "/Users/chenyzh/Desktop/Research/Satterthwaite_Lab/datalad_wrapper"
    where_project = op.join(where_root, "data")
    # use toy data and toy container for testing only:
    input_ds = op.join(where_project, "w2nu3")
    container_ds = op.join(where_project, "toybidsapp-container-docker")
    container_config_yaml_file = op.join(where_root, "babs_paper", config_yaml_filename)

project_name = "showcase_HBN_fmriprep_anatonly"
list_sub_file = None   # no pre-defined subject list file

cmd = "babs-init \\\n"
cmd += "\t" + "--where_project " + where_project + " \\\n"
cmd += "\t" + "--project_name " + project_name + " \\\n"
cmd += "\t" + "--input " + "BIDS" + " " + input_ds + " \\\n"
if list_sub_file is not None:
    cmd += "\t" + "--list_sub_file " + list_sub_file + " \\\n"
cmd += "\t" + "--container_ds " + container_ds + " \\\n"
cmd += "\t" + "--container_name " + container_name + " \\\n"
cmd += "\t" + "--container_config_yaml_file " + container_config_yaml_file + " \\\n"
cmd += "\t" + "--type_session " + type_session + " \\\n"
cmd += "\t" + "--type_system " + "sge"

print(cmd)
