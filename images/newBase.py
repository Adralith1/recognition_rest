import zipfile
import os


def extract(option,file_path):
    if option=="delete":
        i=0
        folder = 'bow_retrieval/dataset-retr/train'
        for the_file in os.listdir(folder):
            file_path_del = os.path.join(folder, the_file)
            i=i+1
            print("deleting file : " + str(i))
            try:
                if os.path.isfile(file_path_del):
                    os.unlink(file_path_del)
            except Exception as e:
                print(e)

        if 'zip' in file_path :
            with zipfile.ZipFile(file_path,"r") as zip_ref:
                print("Extracting files...")
                zip_ref.extractall("bow_retrieval/dataset-retr/train")
            os.remove(file_path)
            return "Files extracted and saved"
