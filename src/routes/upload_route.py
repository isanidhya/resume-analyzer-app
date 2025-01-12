def setup_upload_route(page):
    def upload_file(e):
        file = e.control.files[0]
        if file:
            # Save the uploaded file temporarily
            with open("uploaded_resume.pdf", "wb") as f:
                f.write(file.read())
            
            # Analyze the resume using the AnalysisController
            from controllers.analysis_controller import AnalysisController
            controller = AnalysisController()
            score, feedback = controller.analyze_resume("uploaded_resume.pdf")
            
            # Display the results on the page
            page.add(ft.Text(f"Score: {score}%"))
            page.add(ft.Text(f"Feedback: {feedback}"))

    page.add(ft.FilePicker(on_change=upload_file))