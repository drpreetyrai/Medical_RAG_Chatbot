from langchain.document_loaders import PyPDFLoader, DirectoryLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.embeddings import HuggingFaceEmbeddings
from langchain.text_splitter import CharacterTextSplitter

#Extract data from the PDF
def load_pdf(data):
    loader = DirectoryLoader(data,
                    glob="*.pdf",
                    loader_cls=PyPDFLoader)
    
    documents = loader.load()

    return documents



#Create text chunks
def text_split(extracted_data):
    # Splitting the data into chunk
   text_splitter = CharacterTextSplitter(chunk_size=2000, chunk_overlap=30, separator="\n")
   text_chunks = text_splitter.split_documents(documents=extracted_data)   
   return text_chunks 



#download embedding model
def download_hugging_face_embeddings():
    #loading the embedding model from huggingface
    embedding_model_name = "sentence-transformers/all-mpnet-base-v2"
    # model_kwargs = {"device": "cuda"}
    model_kwargs = {"device": "cpu"}
    embeddings = HuggingFaceEmbeddings(
       model_name=embedding_model_name,
       model_kwargs=model_kwargs
    )
    return embeddings

