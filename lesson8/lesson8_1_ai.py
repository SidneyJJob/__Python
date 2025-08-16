#建立一個gradio的Blocks的架構
#功能:
#1.輸入姓名，點擊按鈕後，顯示問候語
#2.建立輸出框
#3.建立按鈕

import gradio as gr

def greet(name):
    return name + "，你好！"

with gr.Blocks() as demo:
    name_textbox = gr.Textbox(label="姓名",placeholder="請輸入您的姓名")
    output_textbox = gr.Textbox(label="輸出",placeholder="輸出結果將顯示在這裡")
    greet_button = gr.Button("打聲招呼吧！")
    greet_button.click(fn=greet,
                       inputs=[name_textbox],
                       outputs=[output_textbox])

    demo.launch()