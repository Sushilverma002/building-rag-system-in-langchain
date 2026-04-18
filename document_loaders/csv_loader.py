from langchain_community.document_loaders import CSVLoader

loader = CSVLoader(file_path="Social_Network_Ads.csv", encoding="utf-8")

docs = loader.load()

print(len(docs))
print(docs[2])
print(f"page content:{docs[2].page_content}")
print(f"metadata: {docs[2].metadata}")
