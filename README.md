# aiResume Coverletter Generator

This project provides a web-based application for generating custom cover letters based on uploaded resumes. It combines FastAPI for the backend API endpoints and Streamlit for the frontend UI. The application utilizes the [Anthropic](https://www.anthropic.com/) API for natural language processing to generate personalized cover letters.

## Overview

The application consists of two main components:

1. **Streamlit UI for Resume Upload**: Users can upload their resumes (in PDF or DOCX format) along with their name and email address. Upon upload, an email confirmation is sent, and users can proceed to generate custom cover letters.

2. **FastAPI Backend for Cover Letter Generation**: The backend server handles the generation of cover letters based on user input questions and the content of the uploaded resume. It interacts with the Anthropi API to generate natural-sounding cover letters.

## Setup and Installation

To run the application locally, follow these steps:

1. Clone this repository to your local machine.

2. Install the required Python packages by running:
`pip install -r requirements.txt`

3. Set up environment variables by creating a `.env` file in the root directory and adding the following variables:
MAILERSEND_API_KEY=your_mailersend_api_key ;
ANTHROPIC_API_KEY=your_anthropic_api_key

5. Run the FastAPI server by executing the following command:
uvicorn main:app --reload

6. Run the Streamlit application by executing the following command in a separate terminal:
 streamlit run app.py


7. Access the application in your web browser at `http://localhost:8501`.

![Screenshot 2024-04-22 at 3 42 56 PM](https://github.com/akhil20187/aiResume/assets/19240034/d42fd34e-95aa-410f-8e32-ff87494b8c23)

## Usage

1. **Upload Resume**: In the Streamlit UI, upload your resume file (PDF or DOCX format) and provide your name and email address. Click the "Upload" button to confirm.
   Once you upload user will receive an email with a confirmation of receipt. You can also define another email i.e admin to receive the email. The content of the same can be update in the fastapi file - main.py .

3. **Generate Cover Letters**: After uploading your resume, you can input questions or prompts for generating custom cover letters. Click the "Generate" button to receive your personalized cover letter. Ensure that you have configured the API keys

4. **Receive Email Confirmation**: Upon successful upload of your resume, you will receive an email confirmation. You can proceed to generate cover letters after receiving the confirmation.

## Contributors

- Akhilesh ([https://github.com/akhil20187])

## License

This project is licensed under the [MIT License](LICENSE).




