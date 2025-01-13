import flet as ft
import google.generativeai as genai
from flet import ElevatedButton, Column, Page

def main(page: Page):
    page.title = "Resume Analyzer"
    page.scroll = "auto"

    def on_file_picked(e):
        if e.files:
            resume_path = e.files[0].path
            feedback, score = analyze_resume(resume_path)
            page.add(ft.Text(f"Feedback: {feedback}"))
            page.add(ft.Text(f"Score: {score}%"))

    file_picker = ft.FilePicker(on_result=on_file_picked)
    page.overlay.append(file_picker)

    def upload_resume(e):
        file_picker.pick_files(allow_multiple=False)

    upload_button = ElevatedButton("Upload Resume", on_click=upload_resume)
    page.add(Column([upload_button]))

def analyze_resume(resume_path):
    genai.configure(api_key="YOUR API KEY")
    model = genai.GenerativeModel('gemini-pro')
    
    with open(resume_path, 'r', encoding='utf-8') as file:
        resume_content = file.read()
    
    response = model.generate(resume_content)
    feedback = response['feedback']
    score = response['score']
    
    return feedback, score

if __name__ == "__main__":
    ft.app(target=main)
