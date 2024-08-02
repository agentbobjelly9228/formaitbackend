from langchain.document_loaders import PyPDFLoader
from langchain.llms import OpenAI
from langchain.chains.question_answering import load_qa_chain

# Locate your PDF here.
pdf = "./thing.pdf"
# Load the PDF
loader = PyPDFLoader(pdf)
documents = loader.load()

# api_key = "sk-?????"
llm = OpenAI(model_name="gpt-4o")
chain = load_qa_chain(llm, verbose=True)
question = "Make a csv file with data from this pdf"
response = chain.run(input_documents=documents, question=question)

print(response)
