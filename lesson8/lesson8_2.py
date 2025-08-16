## Block 架構

import gradio as gr

def greet(name):
    return name + "，你好！"

with gr.Blocks() as demo:
    name_textbox = gr.Textbox(label="姓名",placeholder="請輸入您的姓名")
    output_textbox = gr.Textbox(label="輸出",placeholder="輸出結果將顯示在這裡")
    greet_button = gr.Button("打聲招呼吧！")
    
    @greet_button.click(
        inputs=[name_textbox],
        outputs=[output_textbox]
    )
    def greet(name):
        return name + "，你好！"

    demo.launch()