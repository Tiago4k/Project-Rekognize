import os
from tqdm import tqdm
from pathlib import Path


def multi_replace(dir):
    '''
    Replaces a "vehicle registration plate" with the filename and
    the word "plate", and replaces all spaces with commas.
    '''
    for root, _, files in os.walk(labels_dir):
        for fname in tqdm(files):
            file_path = os.path.join(root, fname)

            if fname != '.DS_Store':

                f = Path(file_path).stem
                replacement_dict = {
                    'Vehicle registration plate': f + '.jpg,plate',
                    ' ': ','
                }

                # Open the file and replace words in the dic by iterating the through the dictionary
                with open(file_path, "r+") as fin:
                    data = fin.read()
                    for _, key in enumerate(replacement_dict):
                        data = data.replace(key, replacement_dict[key])

                # Write the new replaced data to the file
                with open(file_path, "wt") as fin:
                    fin.write(data)

                # Append an ',S' to the end of each line
                newline = ''
                with open(file_path, 'r') as f:
                    for line in f:
                        newline += line.strip()+",S\n"
                    f.close()

                with open(file_path, 'w') as f:
                    f.write(newline)
                    f.close()

                replace_S(file_path)


def replace_S(file_path):
    '''
    Replaces ',S' with with an int. Int will be the ID of each bounding box in an image
    '''
    f = open(file_path, "r+")
    lines = f.readlines()
    for i, line in enumerate(lines):
        lines[i] = line.replace(',S', ',' + str(i+1))

    f = open(file_path, "w")
    f.writelines(lines)
    f.close()


def combine_txts(dir):
    '''
    Combines all of the .text files into a single file
    '''
    for root, _, files in os.walk(labels_dir):
        for fname in tqdm(files):
            file_path = os.path.join(root, fname)

            if fname != '.DS_Store':
                with open(file_path) as input_f:
                    with open('bboxes.txt', 'at') as output_f:
                        for line in input_f:
                            output_f.write(line)


if __name__ == '__main__':
    labels_dir = os.path.dirname(
        '/Users/tiagoramalho/Project-Rekognize/Dataset/Plate/Label/')

    multi_replace(labels_dir)
    combine_txts(labels_dir)
