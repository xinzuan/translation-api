from easynmt import EasyNMT
from glob import glob
import os

examples = glob('./examples/*.txt')
lang = 'en'
nmt_model = EasyNMT("m2m_100_1.2B",device="cpu")

#

def read_file_to_array(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        lines = file.read().splitlines()
    return lines

def save_array_to_file(file_path, text_array):
    try:
        with open(file_path, 'w', encoding='utf-8') as file:
            for line in text_array:
                file.write(line + '\n')
    except IOError as e:
        print(f"An error occurred while writing to the file: {e}")


def main (examples):
    for file in examples:
        lines = read_file_to_array(file)
        fname = os.path.basename(file)[:-4]
        results = nmt_model.translate(lines,target_lang=lang)
        save_array_to_file(f'{fname}_kor_res.txt',results)


main(examples)