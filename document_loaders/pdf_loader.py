from langchain_community.document_loaders import PyPDFLoader

loader = PyPDFLoader('dl-curriculum.pdf')

docs = loader.load()

print(len(docs))

print(f"page content: {docs[1].page_content}")
print(f"metadata:{docs[1].metadata}")