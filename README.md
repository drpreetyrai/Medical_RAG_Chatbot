

# End-to-end-Medical-Chatbot-using-Llama 3.1

# How to run?
### STEPS:

Clone the repository

```bash
Project repo: https://github.com/
```

### STEP 01- Create a conda environment after opening the repository

```bash
conda create -n mchatbot python=3.8.19 -y
```

```bash
conda activate mchatbot
```

### STEP 02- install the requirements
```bash
pip install -r requirements.txt
```


### Create a `.env` file in the root directory and add your Pinecone credentials as follows:

```ini
GROQ_API_KEY = "xxxxxxxxxxxxxxxxxxxxxxxxxxxxx"

```


### Download the quantize model from the link provided in model folder & keep the model in the model directory:

```ini
## Use the Llama 3.1 Model:
Using Groq i have used LLama 3.1 model 
llm = ChatGroq(groq_api_key=groq_api_key, model_name="llama-3.1-70b-versatile")


## From the following link to get groq api key:
https://console.groq.com/keys
```



```bash
# Finally run the following command
python app.py
```

Now,
```bash
open up localhost:
```


### Techstack Used:

- Python
- LangChain
- Flask
- Meta Llama3.1
- GROQ 
- FAISS

