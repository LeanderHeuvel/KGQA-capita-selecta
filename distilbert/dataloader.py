from datasets import load_dataset
folder_path = "datasets/wikidata-simplequestions-master/"
dataset = load_dataset("text", data_files={"train": folder_path+"annotated_wd_data_train_answerable.txt", "test": folder_path+"annotated_wd_data_test_answerable.txt"}, sample_by="paragraph")
print(dataset[0])