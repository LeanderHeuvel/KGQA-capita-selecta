from datasets import load_dataset
import argparse


folder_path = "data/wikidata-simplequestions-master/"
parser = argparse.ArgumentParser(description='Process some env variables')
parser.add_argument('--path', type = str,
                    help='add folder path', default = folder_path)

args = parser.parse_args()
folder_path = args.path
dataset = load_dataset("text", data_files={"train": folder_path+"annotated_wd_data_train_answerable.txt", "test": folder_path+"annotated_wd_data_test_answerable.txt"}, sample_by="paragraph")
print(dataset[0])