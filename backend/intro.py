import pyrebase
from fastapi import FastAPI, File, UploadFile, Request
from pydantic import BaseModel

from backend.googlevision import upload_file_to_gs, async_detect_document

app = FastAPI()

firebaseconfig = {}

firebase = pyrebase.initialize_app(firebaseconfig)
db = firebase.database()


@app.post("/uploadfile/")
def create_upload_item(pdf: UploadFile = File(...)):
    """
    upload file uses spooled file:Spooling is a system function that saves data in a database file for later processing or printing
    """
    # save the file
    input_path = upload_file_to_gs(pdf.file, pdf.filename)
    output_path = 'gs://harshitgoel/output/' + pdf.filename

    text = async_detect_document(input_path, output_path)
    print(text)
    database(text)
    # config to database

    return {'input_path': input_path, 'output_path': output_path, 'text': text}


class issue(BaseModel):
    email: str
    message: str


@app.post("/Customer_issues/")
def get_customer_issue(item: issue):
    print([item.email, item.message])
    return [item.email, item.message]

def database(text):
    data = {"Adhar card detail": text}
    db.child("data").push(data)
