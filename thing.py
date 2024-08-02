from openpyxl import load_workbook
from langchain.document_loaders import PyPDFLoader
from langchain.llms import OpenAI
from langchain.chains.question_answering import load_qa_chain
import xlrd
import csv
import pandas as pd
import re
import json
json_regex = r'\{.*?\}'


def convertToTemplate():
    # read an excel file and convert
    # into a dataframe object
    workbook = load_workbook(filename="template.xlsx")
    sheet = workbook.active
    print(sheet.cell(row=8, column=2).value)
    replaceCoords = []
    for y in range(sheet.max_row):
        for x in range(sheet.max_column):
            if sheet.cell(row=y + 1, column=x + 1).value == "REPLACE":
                replaceCoords.append((y + 1, x + 1))
    print(replaceCoords)
    templateDictionary = {
        "date": (8, 5),
        "bill to": (10, 5),
        "ship to": (14, 5),
    }

    # Locate your PDF here.

    pdf = "./thing.pdf"
    # Load the PDF
    loader = PyPDFLoader(pdf)
    documents = loader.load()

    # api_key = "sk-?????"
    llm = OpenAI(model_name="gpt-4o")
    chain = load_qa_chain(llm, verbose=True)
    question = """With this pdf, find the date, billing address, and shipping address. Output your answer only in the following JSON format: 
    templateDictionary = {
        "date": string,
        "bill to": string (with line breaks),
        "ship to":string (with line breaks),
    }"""

    response = str(chain.run(input_documents=documents, question=question))
    json_match = re.search(json_regex, response, re.DOTALL)
    responseJson = json.loads(json_match.group(0))
    print(responseJson)
    sheet.cell(row=8, column=5).value = responseJson["date"]
    # split addresses
    addresses = responseJson["bill to"].split("\n")
    for i in range(len(addresses)):
        sheet.cell(row=10 + i, column=5).value = addresses[i]

    addresses = responseJson["ship to"].split("\n")
    for i in range(len(addresses)):
        sheet.cell(row=14 + i, column=5).value = addresses[i]

    workbook.save("test.xlsx")


convertToTemplate()
