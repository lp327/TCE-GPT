import os
os.environ['OPENAI_API_KEY'] = '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'

from gpt_index import SimpleDirectoryReader, GPTVectorStoreIndex, GPTListIndex, GPTSimpleVectorIndex, LLMPredictor, PromptHelper, ServiceContext, Document
from langchain import OpenAI
import openai
from googletrans import Translator
import mysql.connector
import sys

def construct_index(directory_path):
    max_input_size = 4096
    num_outputs = 512
    max_chunk_overlap = 20
    chunk_size_limit = 600
    prompt_helper = PromptHelper(max_input_size, num_outputs, max_chunk_overlap, chunk_size_limit=chunk_size_limit)
    llm_predictor = LLMPredictor(llm=OpenAI(temperature=0.7, model_name="text-davinci-003", max_tokens=num_outputs))
    documents = SimpleDirectoryReader(directory_path).load_data()
    index = GPTSimpleVectorIndex.from_documents(documents)
    index.save_to_disk('index.json')
    return index

def chatbot(input_text):
    print("Input Message: ",input_text)
    translator = Translator()
    lang = translator.detect(input_text).lang
    english_translated_text = translator.translate(input_text, src=lang, dest= 'en')
    input_text = english_translated_text.text
    index = GPTSimpleVectorIndex.load_from_disk('index.json')
    response = index.query(input_text, response_mode="compact")
    english_translated_text = translator.translate(response.response, src='en', dest= lang)
    print("Output Message: ",english_translated_text.text)
    return(english_translated_text.text)

username = "root"
password = "priya2003"
database = "mysql"
table = "README"

index = construct_index('docs')

