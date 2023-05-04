# This is to generate `babs-init` command
# Used by BABS show case

import os
import os.path as op

where_project = "/cbica/projects/BABS/babs_showcase"
project_name = "showcase_HBN_fmriprep_anatonly"
input_ds = "?????"   # path to the input dataset
list_sub_file = None   # no pre-defined subject list file
container_ds = "????"   # path to the container datalad dataset
container_config_yaml_file = "????"   # path to yaml file
container_name = "fmriprep-?-?-?"
type_session = "single-ses"


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
