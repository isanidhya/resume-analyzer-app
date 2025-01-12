class AnalysisController:
    def __init__(self, api_key):
        self.api_key = api_key
        genai.configure(api_key=self.api_key)
        self.model = genai.GenerativeModel('gemini-pro')

    def analyze_resume(self, resume_text):
        response = self.model.generate(resume_text)
        return response

    def get_feedback(self, analysis_result):
        feedback = analysis_result.get('feedback', '')
        score = analysis_result.get('score', 0)
        return feedback, score