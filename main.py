from fastapi import FastAPI, File, UploadFile, Form
from mailersend import emails
import os
import base64
import tempfile
from dotenv import load_dotenv
import pypdf
import anthropic
import io

load_dotenv()

app = FastAPI()
anthropic_api_key = os.getenv('ANTHROPIC_API_KEY')
mailersend_name ="AiResume" # write the name that will be sent via the mailersend
mailersend_email= "" #domain email id registered with the mailersend
admin_name="John Doe" #write the name of the admin, who will receive the email confirmation
admin_email="akhilesh@rediffmail.com" #write the email id of the admin, who will receive the email confirmation


# Sending email function via Mailersend
def send_email(file_path: str, uploader_name: str, uploader_email: str):
    # Initialize MailerSend
    mailer = emails.NewEmail(os.getenv('MAILERSEND_API_KEY'))
    # Read the uploaded file and encode it in base64
    with open(file_path, 'rb') as attachment:
        att_read = attachment.read()
        att_base64 = base64.b64encode(att_read)

    mail_list = [
        {   
            "from": {
                "name": mailersend_name,
                "email": mailersend_email,
            },
            "to": [
                {
                    "name": uploader_name,
                    "email": uploader_email,
                }
            ],
            "subject": f"Received your resume",
            "text": f" Dear {uploader_name},\n, We have reciever your resume. Now you can generate custmoized cover letters. \n Thank you\n AiResume.",
            # Define the attachment
            "attachments": [
                {
                    "id": "my-attached-file",
                    "filename": os.path.basename(file_path),
                    "content": f"{att_base64.decode('ascii')}",
                    "disposition": "attachment"
                }
            ]
        },
        {
            "from": {
                "name": mailersend_name,
                "email": mailersend_email,
            },
            "to": [
                {
                    "name": admin_name,
                    "email": admin_email,
                }
            ],
            "subject": f"New Entry : Resume submitted by {uploader_name}",
            "text": f"{uploader_name} has submitted a new resume. Please check the attachment.",
            # Define the attachment
            "attachments" : [
                {
                    "id": "my-attached-file",
                    "filename": os.path.basename(file_path),
                    "content": f"{att_base64.decode('ascii')}",
                    "disposition": "attachment"
                }
            ]
        }
    ]
    
    # Send the email
    try:
        status = mailer.send_bulk(mail_list)
        print(status)
        return "Email sent successfully!"
        
    except Exception as e:
        return f"Error sending email: {str(e)}"

@app.post("/send_email")
async def send_email_endpoint(uploader_name: str = Form(...), uploader_email: str = Form(...), file: UploadFile = File(...)):
    file_name=file.filename
    with tempfile.NamedTemporaryFile(prefix=f"{os.path.splitext(file_name)[0]}_",suffix=os.path.splitext(file_name)[1], delete=False) as tmp_file:
        tmp_file.write(await file.read())
        tmp_file_path = tmp_file.name
    result = send_email(tmp_file_path, uploader_name, uploader_email)
    os.unlink(tmp_file_path)
    return {"message": result}

# Generate Cover Letter API endpoint
@app.post("/generate_cover_letter")
async def generate_cover_letter_endpoint(question: str = Form(...), file: UploadFile = File(...)):
    print(file)
    #Read the content of the uploaded file
    file_content = await file.read()
    file_like_object = io.BytesIO(file_content)
    pdf_file = pypdf.PdfReader(file_like_object)
    resume=""
    for page in pdf_file.pages:
        #resume += pdf_file.getPage(page).extract_text()
        resume += page.extract_text()
    #resume=uploaded_file.read().decode()
    prompt = f"""{anthropic.HUMAN_PROMPT} Here's the resume:\n\n<article>
    {resume}\n\n</article>\n\n{question}{anthropic.AI_PROMPT}"""

    client = anthropic.Client(api_key=anthropic_api_key)
    response = client.completions.create(
        prompt=prompt,
        stop_sequences=[anthropic.HUMAN_PROMPT],
        model="claude-v1",  # "claude-2" for Claude 2 model
        max_tokens_to_sample=100,
    )
    # Return the generated cover letter
    print (response)
    return {"cover_letter": response.completion}
