from flask import Flask, render_template, jsonify, request
from src.helper import download_hugging_face_embeddings
from langchain.vectorstores import FAISS 
from langchain.prompts import PromptTemplate
from langchain.chains import RetrievalQA
from langchain_groq import ChatGroq
from dotenv import load_dotenv
from src.prompt import *
import os



app = Flask(__name__)

load_dotenv()

embeddings = download_hugging_face_embeddings()

#load from local storage
persisted_vectorstore = FAISS.load_local("faiss_index_", embeddings, allow_dangerous_deserialization=True)

# creating a retriever on top of database
retriever = persisted_vectorstore.as_retriever()

PROMPT=PromptTemplate(template=prompt_template, input_variables=["context", "question"])
chain_type_kwargs={"prompt": PROMPT} 


groq_api_key=os.environ.get('GROQ_API_KEY')
llm = ChatGroq(groq_api_key=groq_api_key, model_name="llama-3.1-70b-versatile")


qa = RetrievalQA.from_chain_type(
    llm=llm,
    chain_type="stuff", retriever=retriever,
    return_source_documents=True,
    chain_type_kwargs=chain_type_kwargs
    )



@app.route("/")
def index():
    return render_template('chat.html')




@app.route("/get", methods=["GET", "POST"])
def chat():
    msg = request.form["msg"]
    input = msg
    print(input)
    result=qa({"query": input})
    print("Response : ", result["result"])
    return str(result["result"])



if __name__ == '__main__':
    app.run(host="0.0.0.0", port= 8080, debug= True)

