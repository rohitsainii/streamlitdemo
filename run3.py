import streamlit as st
import requests
import random
import time
import re
import pyautogui
import fitz #pip install PyMuPDF
import filetype
import json
import streamlit as st
 
 
# Custom CSS to align header
docusense_page_html = """
<style>
        .header-container {
            display: flex;
            justify-content: center;
            align-item:center;
            text-align:center;
           
            conic-gradient(#553c9a 30%, #ee4b2b 40%, #ee4b2b 70%, #00c2cb 80%, #553c9a);
           
        }
</style>
<div class="header-container">
<b>
<h4>Document Sense <sub>v 0.0.1</sub></h4>
<h6>Cloud Based Generative AI Solution</h6>
</b>
</div>
"""
 
 
 
login_page_html = """
<style>
        .header-container {
            display: flex;
            justify-content: center;
        }
</style>
<div class="header-container">
<h4>Sign in</h4>
</div>
"""
 
 
usecase_page_html = """
<style>
        .header-container {
            display: flex;
            justify-content: center;
        }
</style>
<div class="header-container">
<h4>New Usecase</h4>
</div>
"""
 
 
sign_up_page_html = """
<style>
        .header-container {
            display: flex;
            justify-content: center;
        }
</style>
<div class="header-container">
<h4>Sign up</h4>
</div>
"""
 
 
 
# Render the header using st.markdown with unsafe_allow_html=True
 
 
# Your Streamlit app content goes here
class Document:
    def __init__(self, page_content, page, source):
        self.page_content = page_content
        self.page = page
        self.source = source
 
def extract_documents(json_content):
    documents = []
 
    for item in json_content["context"]:
        # if item.get('type') == 'Document':
            page_content = item['page_content']
            page = item['metadata']['page']
            source = item['metadata']['source']
            document = Document(page_content, page, source)
            documents.append(document)
    return documents
 




def is_pdf(file_path):
    file_info = filetype.guess(file_path)
    return file_info is not None and file_info.mime == 'application/pdf'

def is_scanned_pdf(pdf_path):
    doc = fitz.open(pdf_path)
    total_pages = doc.page_count
    scanned_pages = 0
    
    for page_num in range(total_pages):
        page = doc.load_page(page_num)
        text = page.get_text()
        
        if not text.strip():
            scanned_pages += 1
    
    scanned_percentage = (scanned_pages / total_pages) * 100
    doc.close()
    
    return scanned_percentage > 80


 
 
def check(email):
    regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,7}\b'
 
    if(re.fullmatch(regex, email)):
        return True
 
    else:
        return False
 
def login():
    # st.markdown(docusense_page_html, unsafe_allow_html=True)
    # st.markdown("<h3 style='text-align: center;'>DocuSense</h3>", unsafe_allow_html=True)
    # st.divider()
    # st.header("   ",divider="rainbow")
    # st.header("   ")
   
 
    # st.subheader("Sign in")
    st.markdown(login_page_html, unsafe_allow_html=True)
    
 
    # Form fields
    form = st.form("Login", clear_on_submit = False)
    with form:
        username = st.text_input("Email", max_chars=100)
        password = st.text_input("Password", type="password",max_chars=20)
        col1, col2, col3,col4, col5, col6,col7 = st.columns(7)
        submit = col7.form_submit_button("Submit")
    #     submit2 = col7.form_submit_button("Reset")
    # if submit2:
    #     refresh()
 
    if submit:
        # Prepare form-urlencoded data
       
        if not username and not password:
            alert28=st.error("Email is required!")
            alert29=st.error("Password is required!")
 
            time.sleep(2)
            alert28.empty()
            alert29.empty()
        elif not username:
            alert30=st.error("Email is Required!")
            time.sleep(2)
            alert30.empty()
        elif check(username) == False and username:
            alert31=st.error("Invalid Email!")
            time.sleep(2)
            alert31.empty()
        elif not password:
            alert32=st.error("Password is Required!")
            time.sleep(2)
            alert32.empty()
 
        else:
   
            data = {
                "grant_type": "",
                "username": username,
                "password": password,
                "scope": "",
                "client_id": "",
                "client_secret": ""
            }
 
   # Send POST request to FastAPI backend
            response = requests.post(
                "https://docu-sense.jollybush-4dc76daa.eastus.azurecontainerapps.io/users/token",
                data=data,
                headers={"Content-Type": "application/x-www-form-urlencoded"}
            )
   
            if response.status_code == 200:
                st.success("Login successful!")
                st.session_state.logged_in = True
                if 'email' not in st.session_state:
                    st.session_state.email = username
                st.experimental_rerun()
            else:
                st.error("Login failed. Please check your credentials.")
 
 
def register():
    # st.subheader("Sign Up")
    # st.markdown(docusense_page_html, unsafe_allow_html=True)
    # st.header("   ",divider="rainbow")
    # st.header("   ")
 
    st.markdown(sign_up_page_html, unsafe_allow_html=True)
    # st.header("   ",divider="rainbow")
    # st.divider()
 
 
    form = st.form("Register", clear_on_submit = False)
    with form:
        email = st.text_input("Email",max_chars=100)
        password = st.text_input("Password", type="password",max_chars=20)
        confirm_password = st.text_input("Confirm Password", type="password", max_chars=20)
        col1, col2, col3,col4, col5, col6,col7 = st.columns(7)
        submit = col7.form_submit_button("Sign up")
        #submit2 = col7.form_submit_button("Reset")
 
    if submit:
        if check(email) == False and email:
                alert14=st.error("Invalid Email!")
                time.sleep(2)
                alert14.empty()
        else:
            if not email and not password and not confirm_password:
                # alert=st.error("Email, Password and Confirm Password are required!")
                alert15=st.error("Email is required!")
                alert16=st.error("Password is required!")
                alert17=st.error("Confirm Password is required!")
 
                time.sleep(2)
                alert15.empty()
                alert16.empty()
                alert17.empty()
            elif not email and not confirm_password:
                # alert=st.error("Email and Confirm Password are required!")
                alert18=st.error("Email is required!")
                alert19=st.error("Confirm Password is required!")
                time.sleep(2)
                alert18.empty()
                alert19.empty()
            elif not email and not password:
                # alert=st.error("Email and password are required!")
                alert20=st.error("Email is required!")
                alert21=st.error("Password is required!")
                time.sleep(2)
                alert20.empty()
                alert21.empty()
            elif not password and not confirm_password:
                # alert=st.error("Password and Confirm Password are required!")
                alert22=st.error("Password is required!")
                alert23=st.error("Confirm Password is required!")
                time.sleep(2)
                alert22.empty()
                alert23.empty()
            elif not email:
                alert24=st.error("Email is required!")
                time.sleep(2)
                alert24.empty()
            elif not password:
                alert25=st.error("Password is required!")
                time.sleep(2)
                alert25.empty()
            elif not confirm_password:
                alert26=st.error("Confirm Password is required!")
                time.sleep(2)
                alert26.empty()
 
            elif password != confirm_password:
                alert27=st.error("Passwords do not match!")
                time.sleep(2)
                alert27.empty()
            else:
                # Prepare data as JSON
                data = {
                    "email": email,
                    "password": password
                }
 
            # Send POST request to FastAPI backend
                response = requests.post("https://docu-sense.jollybush-4dc76daa.eastus.azurecontainerapps.io/users/register", json=data)
                # submited=st.form_submit_button("Sign up")
                if response.status_code == 201 and submit== True :
                    # form.Register
 
                    st.success("Registration successful!")
                    time.sleep(3)
                    pyautogui.hotkey("ctrl", "F5")
 
                    #st.json(response.json())  # Display response from backend
                elif response.status_code == 400:
                    st.error("A user with the same email already exists!")              
                else:
                    st.error(f"Registration failed with status code: {response.status_code}")
 
 
 # Function to fetch project names from FastAPI backend
def fetch_project_names(email):
    url = f"https://docu-sense.jollybush-4dc76daa.eastus.azurecontainerapps.io/projects/user/{email}"
    params = {"skip": 0, "limit": 100}
    response = requests.get(url, params=params)
    if response.status_code == 200:
        if response.json():
            projects = response.json()
            return [project["name"] for project in projects]
        else:
            return []
    else:
        st.error("Failed to fetch project names!")
 
# Streamlit app
def project_list(usecase_name):
    #logout()
    email = st.session_state.email
    print("usecace name: ", usecase_name)
    # Fetch project names
    project_names = fetch_project_names(email)
 
    if project_names:
        #selected_project = st.sidebar.radio("",["Select usecase"] + project_names)
        #st.write(f"Selected Project: {selected_project}")
        chat_part(usecase_name)
       
 
def creat_new_usecase():
    #st.markdown(docusense_page_html, unsafe_allow_html=True)
    #st.image("logo.png",width=250)
    #st.header("   ",divider="rainbow")
    # st.header("   ")
    # st.markdown(usecase_page_html, unsafe_allow_html=True)
    #logout()
    st.subheader("New Usecase")
    if "messages" not in st.session_state:
        pass
    else:
        del st.session_state.messages
 
    API_URL = "https://docu-sense.jollybush-4dc76daa.eastus.azurecontainerapps.io/projects/"
 
 
    # Form inputs
    form = st.form("Submit", clear_on_submit = False)
    with form:
        name = st.text_input("Name", max_chars=100)
        description = st.text_area("Description", max_chars=250)
        createdby = st.session_state.email
        files = st.file_uploader("Upload Upto 2 Files",help="Supports only searchable pdf", accept_multiple_files=True)
 
        col1, col2, col3,col4, col5, col6,col7 = st.columns(7)
        submit = col7.form_submit_button("Submit")
        #submit2 = col7.form_submit_button("Reset")
 
 
    # File uploader
    # Button to send data
    is_uploaded = False
    files_to_upload = []
    scan_cout =0
    if submit:
        if not name and not description and not files:
            # alert=st.error("Name, Description and PDF file are Required!")
            alert1=st.error("Name is Required!")
            alert2=st.error("Description is Required!")
            alert3=st.error("PDF file is Required!")
            time.sleep(2)
            alert1.empty()
            alert2.empty()
            alert3.empty()
        elif not name and not description:
            # alert=st.error("Name and Description are Required!")
            alert4=st.error("Name is Required!")
            alert5=st.error("Description is Required!")
            time.sleep(2)
            alert4.empty()
            alert5.empty()
        elif not description and not files:
            # alert=st.error("Description and PDF file are Required!")
            alert6=st.error("Description is Required!")
            alert7=st.error("PDF file is Required!")
            time.sleep(2)
            alert6.empty()
            alert7.empty()
        elif not name and not files:
            # alert=st.error("Name and PDF file are Required!")
            alert8=st.error("Name is Required!")
            alert9=st.error("PDF file is Required!")
            time.sleep(2)
            alert8.empty()
            alert9.empty()
        elif not name:
            alert10=st.error("Name is Required!")
            time.sleep(2)
            alert10.empty()
        elif not description:
            alert11=st.error("Description is Required!")
            time.sleep(2)
            alert11.empty()
        elif not files:
            alert12=st.error("PDF file is Required!")
            time.sleep(2)
            alert12.empty()
        elif len(files) >2:
            alert13=st.error("Upload only upto 2 files!")
            time.sleep(2)
            alert13.empty()
        else:
        # Prepare files for upload

        
            
            if files:
                cout =0
                
                for file in files:
                    if is_pdf(file):
                        cout +=1
                        files_to_upload.append(("files", file))
                        # if not is_scanned_pdf(file):
                        #     scan_cout+=1

                        
                    else:
                        is_uploaded = False
                        alert13=st.error("Upload PDF file only!")
                        time.sleep(2)
                        alert13.empty()
                if cout == len(files):
                    is_uploaded = True
                else:
                    is_uploaded= False
        
                        

        # if (not scan_cout == len(files) )and is_uploaded:
        #     alert13=st.error("Upload Scan PDF file only!")
        #     time.sleep(2)
        #     alert13.empty()

        if is_uploaded:
            # Prepare data for the request
            data = {
                "name": name,
                "description": description,
                "createdby": createdby,
            }
 
            try:
                # Send multipart request to FastAPI server
                response = requests.post(API_URL, data=data, files=files_to_upload)
               
                if response.status_code == 201:
                    
                    st.success("Usecase created successfully!".format(response.status_code))
                    refresh()
                   
                elif response.status_code == 500:
                    #st.error("Failed to create project. Status code: {}".format(response.status_code))
                    st.error("Name already Exist!")
                else:
                    st.error("Failed to create project. Status code: {}".format(response.status_code))
            except Exception as e:
                st.error("An error occurred: {}".format(e))
 
def refresh():
    st.experimental_rerun()
 
def logout():
 
# Add the button with the 'top-right' class
    button_clicked = st.sidebar.button("Logout")
    # Clear session state or perform any other logout actions
    if button_clicked:
        for key in st.session_state.keys():
            del st.session_state[key]
            pyautogui.hotkey("ctrl", "F5")
    #st.experimental_rerun()
 
def chat_part(username):
    # st.markdown(docusense_page_html, unsafe_allow_html=True)
    # st.header("   ",divider="rainbow")
    # st.header("   ")
 
 
    # st.subheader(username)  
    if st.session_state.usecase !=username:
        del st.session_state.messages
 
    st.session_state.usecase = username
 
    if "usecase" not in st.session_state:
        st.session_state.usecase =[]
    if "messages" not in st.session_state:
        st.session_state.messages = []
    if not st.session_state.messages:
        name_of_user = st.session_state.email
        name = name_of_user.split('@')
        st.session_state.messages.append({"role":"🤖" , "content": f"Hello **{name[0]}**, What do you want to know about **{username}**"})
    for message in st.session_state.messages:
        with st.chat_message(message["role"]):
            st.markdown(message["content"])
   
    if prompt := st.chat_input("Write your query here!", max_chars=250):
        st.session_state.messages.append({"role": "🙋‍♂️", "content": prompt})
        with st.chat_message("🙋‍♂️"):
            st.markdown(prompt)
   
        # Connect to the URL and get the response
        base_url = "https://docu-sense.jollybush-4dc76daa.eastus.azurecontainerapps.io/projects/qdrant/"
        query = prompt
        url = base_url +username.replace(" ","%20")+"/query/" +query.replace(" ", "%20")
        print("url : ", url)
        response = requests.get(url, params={"username": username, "query": query}).json()
        print("json: ", response)
   
        # Display assistant response in chat message container
   
        
        documents = extract_documents(response)
        document_texts = [f"Page No : {doc.page +1 }\n\nPage Content : {doc.page_content}  \n\n Source : {doc.source}" for doc in documents]
        help_content = '\n\n---\n\n'.join(document_texts)
        with st.chat_message("🤖"):
            st.markdown(response["answer"],help=help_content)
       
        # Add assistant response to chat history
        st.session_state.messages.append({"role": "🤖", "content": response["answer"]})
        #del st.session_state.messages
   
 

 
def main():
    st.image("logo3.png",width=250)
    #st.header("   ",divider="rainbow")
    st.sidebar.markdown(docusense_page_html, unsafe_allow_html=True)
    st.sidebar.header("   ",divider="rainbow")
 
    if "messages" not in st.session_state:
        st.session_state.messages = []
    if "usecase" not in st.session_state:
        st.session_state.usecase =[]
    if st.session_state.get("logged_in"):
        logout()
 
        if fetch_project_names(st.session_state.email) == []:
           
            creat_new_usecase()
        else:
            page2 = st.sidebar.radio("", ["New Usecase"] +fetch_project_names(st.session_state.email))
           
            if  page2 == "New Usecase":
                creat_new_usecase()
            else:
                project_list(page2)
 
    else:
        page = st.sidebar.radio("", ["Sign in", "Sign up"])
 
        if page == "Sign in":
            login()
                     
        elif page == "Sign up":
            register()
 
if __name__ == "__main__":
    main()