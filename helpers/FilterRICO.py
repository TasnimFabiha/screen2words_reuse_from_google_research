import csv
import os
import shutil
# directory where JSON files are stored
json_dir = './combined/'
# directory to copy the JSON files to
copy_dir = './result/'
# path to the CSV file relative to the current directory
csv_path = './screen2words/screen_summaries.csv'
# get the absolute path to the CSV file
csv_abs_path = os.path.abspath(csv_path)
id_dict = {}
# open the CSV file in read mode
with open(csv_abs_path, 'r') as file:
    # create a CSV reader object
    reader = csv.reader(file)
    # iterate over each row in the CSV file
    for row in reader:
        # extract the id and name from the row
        id = row[0]
        name = row[1]
        
        if id in id_dict:
            print(f'{id} is already present')
            continue
            
        # construct the filename for the JSON file
        filename = str(id) + '.json'
        # check if the file exists in the directory
        if os.path.exists(json_dir + filename):
                
            # if the file exists, copy it to the copy directory
            jpgFilename = str(id) + '.jpg'
            shutil.copy(json_dir + filename, copy_dir)
            shutil.copy(json_dir + jpgFilename, copy_dir)
            
            id_dict[id] = 1
            # print a message to confirm the file was copied
            print(f'{filename} and {jpgFilename} copied to {copy_dir}')
        else:
            # if the file doesn't exist, print an error message
            print(f'Error: JSON file {filename} not found')







