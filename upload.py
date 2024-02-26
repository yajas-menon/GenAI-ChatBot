import gradio as gr

def process_file(file):
  # do something with the file and return an output
  return output

iface = gr.Interface(
  fn=process_file,
  inputs=gr.inputs.File(label="Upload a file"),
  outputs="text"
)

with gr.Blocks() as chat:
    gr.Markdown("Custom trained AI Chatbot")
    
    with gr.Row():
        iface
 
chat.launch(share=True)