import os

class DocumentLoader:

    def load_text_files(self, folder_path):
        documents = []

        for filename in os.listdir(folder_path):
            if filename.endswith(".txt"):
                with open(os.path.join(folder_path, filename), "r", encoding="utf-8") as f:
                    documents.append(f.read())

        return documents