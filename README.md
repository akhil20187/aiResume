# aiResume
The application can generate tailor made cover letter based on the resume uploaded and submitted.

# AI Resume Coverletter Generator

This project provides a web-based application for generating custom cover letters based on uploaded resumes. It combines FastAPI for the backend API endpoints and Streamlit for the frontend UI. The application utilizes the [Anthropic](https://www.anthropic.com/) API for natural language processing to generate personalized cover letters.

## Overview

The application consists of two main components:

1. **Streamlit UI for Resume Upload**: Users can upload their resumes (in PDF or DOCX format) along with their name and email address. Upon upload, an email confirmation is sent, and users can proceed to generate custom cover letters.

2. **FastAPI Backend for Cover Letter Generation**: The backend server handles the generation of cover letters based on user input questions and the content of the uploaded resume. It interacts with the Anthropi API to generate natural-sounding cover letters.

## Setup and Installation

To run the application locally, follow these steps:

1. Clone this repository to your local machine.

2. Install the required Python packages by running:

