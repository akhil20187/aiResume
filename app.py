import streamlit as st
import requests
import json

# Streamlit UI for resume upload
st.title("aiResume Coverletter Writer")

uploaded_file = st.file_uploader("Upload Resume", type=["pdf", "docx"])
uploader_name = st.text_input("Name")
uploader_email = st.text_input("Email")
print (uploaded_file)

if st.button("Upload"):
    if uploaded_file is not None and uploader_name and uploader_email:
        
        files = {'file': (uploaded_file.name, uploaded_file.getvalue(),uploaded_file.type)}
        data = {'uploader_name': uploader_name, 'uploader_email': uploader_email}
        response = requests.post("http://localhost:8000/send_email", files=files, data=data)
        st.write(response.json()["message"])

# Streamlit UI to Generate Cover Letter
st.header("Write your cover letter")
question = st.text_input("Ask your Question", placeholder="Write me a cover letter for product manager")

if st.button("Generate"):
    if question:
        files = {'file': (uploaded_file.name, uploaded_file.getvalue(),uploaded_file.type)}
        data = {'question': question}
        response = requests.post("http://localhost:8000/generate_cover_letter", files=files,data=data)
        print(response)
        st.write(response.json()["cover_letter"])
