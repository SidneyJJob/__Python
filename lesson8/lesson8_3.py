import gradio as gr

with gr.Blocks() as demo:
    gr.Markdown("""
    # 歡迎使用 Gradio
    請輸入您的姓名，並點擊按鈕以獲得問候語。
    """)
    input_textbox = gr.Textbox(label="姓名", placeholder="請輸入您的姓名")
    output_textbox = gr.Textbox(label="問候語", placeholder="輸出結果將顯示在這裡")

    @input_textbox.change(inputs=[input_textbox], outputs=[output_textbox])
    def update_output(text):
        return text

    demo.launch()