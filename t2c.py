# Import the relevant modules.
import os
import re
import pandas as pd

# Get the path in which we are activating the .tec to .csv program
base_path = os.getcwd()
os.chdir(base_path)

# Get list of all the files with the .tec filetype.
tec_files_list = []

for i in os.listdir():
    if ".tec" in i:
        tec_files_list.append(i)

# A function for making a dictionary out of values and variable titles.
def dictionary_maker(variables_list,line_values_list):
    line_values_dict = {}
    for variable in variables_list:
        for value in line_values_list:
            line_values_dict[variable] = value
            line_values_list.remove(value)
            break
    return(line_values_dict)

# A function for generating a name from a file
def name_generator(file):
    # Creating a directory for the outputted .csv files to go in
    csv_path = os.getcwd() + "/tec2csv"
    if os.path.exists(csv_path) == True:
        pass
    else:
        os.mkdir(csv_path)
    original_name = file
    stripped_name = os.path.splitext(original_name)[0]
    extension = ".csv"
    new_name = stripped_name + extension
    new_path = csv_path + "/" + new_name
    return(new_name,new_path)

# A function for opening an individual file and reading all its lines of text.
def file_opener(file):
    with open(file) as f:
        lines = f.readlines()
        nr_lines = len(lines)
    return(lines, nr_lines)

# A function for interpreting a specific file and generating a df of all its data.
def file_interpreter(lines,nr_lines):
    # First line = title information.
    title = re.search('\"(.*)\"', lines[0])
    # Second line = variables information.
    variables_list = re.findall('\"(.*?)\"', lines[1])
    nr_variables = len(variables_list)
    # Third line = zones
    zones = lines[2]
    # Creating a dataframe to place data into:
    df = pd.DataFrame(columns=variables_list)
    # Looping through the data after the third line, and placing it into the df.
    start_i = 3
    end_i = nr_lines
    for i in range(start_i, end_i):
        line_values_list = lines[i].split()
        line_values_dict = dictionary_maker(variables_list, line_values_list)
        row_to_add = pd.Series(line_values_dict, name = i)
        df = df.append(row_to_add)
    return(df)

# A function for placing a df into a correct place as a .csv file
def file_maker(df,new_path):
    df.to_csv(new_path, index=False)


print("---------BEGIN_CONVERSION---------")
# Running through all the files and processing them using the above functions.
j = 1
for file in tec_files_list:
    nr_of_files = len(tec_files_list)
    print(f"Converting {file} ............ File {j} of {nr_of_files}")
    lines, nr_lines = file_opener(file)
    new_name,new_path = name_generator(file)
    df = file_interpreter(lines,nr_lines)
    file_maker(df,new_path)
    j += 1
print("---------END_CONVERSION---------")