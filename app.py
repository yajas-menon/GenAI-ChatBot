from llama_index import SimpleDirectoryReader, LLMPredictor, PromptHelper, ServiceContext, GPTVectorStoreIndex, load_index_from_storage
from langchain.llms import OpenAI
import gradio as gr
# import openai
# import sys
import os
import pandas as pd
import shutil
import time
os.environ["OPENAI_API_KEY"] = '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'
#http://127.0.0.1:7860
def construct_index(directory_path):
    max_input_size = 4096
    num_outputs = 512
    max_chunk_overlap = 0.1
    chunk_size_limit = 600
    llm_predictor = LLMPredictor(llm=OpenAI(temperature=0/7, model_name="gpt-3.5-turbo-instruct"))
    prompt_helper = PromptHelper(max_input_size, num_outputs, max_chunk_overlap, chunk_size_limit=chunk_size_limit)    
    service_context = ServiceContext.from_defaults(llm_predictor=llm_predictor, prompt_helper=prompt_helper)

    # llm_predictor = LLMPredictor(llm=OpenAI(temperature=0.7, model_name="text-davinci-003", max_tokens=num_outputs))
    documents = SimpleDirectoryReader(directory_path).load_data()    
    index = GPTVectorStoreIndex.from_documents(documents, service_context=service_context)
    # index.load_index_from_storage('./content/contract/index.json')
    index.storage_context.persist(persist_dir="index.json")
    return index
index = construct_index('./content/docs')

def add_row_to_dataframe(df, string):
    # Split the string into key-value pairs
    pairs = string.split('\n')
    data = {}
    for pair in pairs:
        if ":" in pair:
            key, value = pair.split(':')
            data[key] = [value]
        
    # Create a DataFrame from the dictionary
    new_row = pd.DataFrame.from_dict(data)
    
    # Append the new row to the original DataFrame
    df = df.append(new_row, ignore_index=True)    
       
    return df

def chatbot(input_text,file):    
    query_engine = index.as_query_engine()
    response = query_engine.query(input_text)   
    # response = index.query(input_text, response_mode="compact")
    df=pd.read_excel("knowledge_repo.xlsx")    
    Bidf=pd.read_csv(r"C:\Users\menon.i.yajas\Documents\proj_ChatGPT\PowerBI-dash.csv")
    df=pd.concat([df,pd.DataFrame([{"File_name":"null","question":input_text,"answer":response.response}])],ignore_index=True)  

    FileName = os.path.basename(file.name)

    Response_String = response.response 
    print(Response_String)
    Bidf = add_row_to_dataframe(Bidf, str(Response_String))
    Bidf.to_csv(r"C:\Users\menon.i.yajas\Documents\proj_ChatGPT\PowerBI-dash.csv",index=False)
    df.to_excel("knowledge_repo.xlsx",index=False)
    return response.response

def upload_file(file):
    time.sleep(5)
    print("here")
    folder = "./content/docs/"
    for filename in os.listdir(folder):
        file_path = os.path.join(folder, filename)
        try:
            if os.path.isfile(file_path) or os.path.islink(file_path):
                os.unlink(file_path)
            elif os.path.isdir(file_path):
                shutil.rmtree(file_path)
        except Exception as e:
            print('Failed to delete %s. Reason: %s' % (file_path, e))
    file_paths = [file.name]
    print(file_paths)
    copy_status=shutil.copyfile(file.name, "./content/docs/"+os.path.basename(file.name).split('/')[-1])
    print(copy_status)
    return file_paths

with gr.Blocks() as chat:
    gr.Markdown("Custom trained AI Chatbot")
    file_output = gr.File()
    upload_button = gr.UploadButton("Click to Upload a File", file_types=["pdf"])
    upload_button.upload(upload_file, upload_button, file_output)


    with gr.Row():
        inp = gr.Textbox("Enter your text?")
        out = gr.Textbox("text")
    btn = gr.Button("Submit")
    

    btn.click(fn=chatbot, inputs=[inp,file_output], outputs=out)

chat.launch(share=True)