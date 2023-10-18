
import gradio as gr
from regex import F
from extract_data import extract_pdf_info
from open_ai_call import call_ai
from store_db import save_str_data


def summarize_pdf(pdf_file, custom_prompt=""):
    text_data = extract_pdf_info(pdf_file.name)
    server_prompt = "You are resume expert. Please analyze the following resume\n" + custom_prompt
    summary = call_ai(text_data, server_prompt)
    save_str_data(summary)
    gr.Info("Summary Saved")
    return summary
   
def main():
    input_pdf_path = gr.File(file_count="single", file_types=["pdf"])
    input_custom_prompt = gr.Textbox(label="Enter your custom prompt", value="Generate 5 points with 3 words each")

    output_summary = gr.Textbox(label="Summary")

    app = gr.Interface(
        fn=summarize_pdf,
        inputs=[input_pdf_path,input_custom_prompt],
        outputs=[output_summary],
        title="Resume Summarizer",
        description="Input resume to get its summary.",
    )
    
    app.launch()


if __name__ == "__main__":
    main()
    
