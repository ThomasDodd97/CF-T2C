# CF-T2C
This is the README for the CF-T2C i.e. the CrunchFlow .Tec to .Csv python script.

Currently, this short script, when executed in the directory where outputted .tec files are, can generate a sub-directory containing the equivalent .csv files.

## Features

* Conversion of all the .tec files in a specific directory into .csv files.

## Requirements

This script requires the following python modules to be run successfully:
* os
* re
* pandas

This script can be cloned to anywhere on the PC and is run by creating an alias pointed at it within the .bashrc or .zshrc files:

alias t2c="conda activate conda_env; python /Users/.../CF-T2C/t2c.py;conda deactivate"

This alias can then be deployed from the terminal by navigating to a directory where crunchtope has successfully been run and then typing the aliased t2c command:

cd /Users/.../crunchy_folder/

t2c

## Known Issues

* No metadata on zones saved, you have to reference back to the original .tec files for this...

## Release Notes

### 1.0.0

Pilot release, this provides the base functionality of simple conversion.
* Added conversion of .tec to .csv