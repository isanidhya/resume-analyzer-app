# Resume Analyzer App

## Overview
The Resume Analyzer App is a web application that allows users to upload their resumes for analysis. Utilizing the Gemini API, the app provides feedback and a percentage score based on the content of the resume. The front-end is developed using Flet, ensuring a smooth user experience.

## Features
- Upload resumes in various formats.
- Analyze resumes using the Gemini API.
- Receive feedback and a percentage score for improvement.

## Project Structure
```
resume-analyzer-app
├── src
│   ├── app.py                  # Entry point of the application
│   ├── controllers
│   │   └── analysis_controller.py # Handles resume analysis logic
│   ├── routes
│   │   └── upload_route.py      # Manages file upload routes
│   └── types
│       └── index.py             # Defines data types and interfaces
├── requirements.txt             # Lists project dependencies
└── README.md                    # Documentation for the project
```

## Setup Instructions
1. Clone the repository:
   ```
   git clone <repository-url>
   cd resume-analyzer-app
   ```

2. Install the required dependencies:
   ```
   pip install -r requirements.txt
   ```

3. Run the application:
   ```
   python src/app.py
   ```

## Usage Guidelines
- Navigate to the application in your web browser.
- Use the upload feature to submit your resume.
- Review the feedback and percentage score provided after analysis.

## Contributing
Contributions are welcome! Please submit a pull request or open an issue for any enhancements or bug fixes.