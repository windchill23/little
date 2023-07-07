import streamlit as st
import pybase64

st.set_page_config(
    page_title="Classifer",
)

#st.sidebar.success("Contact us")
# Add background image
def get_img_as_base64(file):
    with open(file, "rb") as f:
        data = f.read()
    return pybase64.b64encode(data).decode()
img1 = get_img_as_base64("stormy.png")
img2 = get_img_as_base64("5.png")
img3 = get_img_as_base64("18.png")

page_bg_img = f"""
           <style>
           [data-testid ="stAppViewContainer"] {{
            background-image: url("data:image/png;base64,{img2}");
            background-repeat: no-repeat;
            background-size:cover; 
            background-position: bottom left;
            background-attachment: local;
           }}
           [data-testid = "stHeader"]{{
           background: rgba(0,0,0,0);
           }}
           [data-testid = "stToolbar"]{{
           right: 2rem}}
           [data-testid="stSidebarNav"]{{
           background-image: url("data:image/png;base64,{img3}");
           background-size: 100%; 
           background-repeat: no-repeat;
           background-position: upper left;
           }}
           
           [data-testid ="stSidebar"] {{
            background-image: url("data:image/png;base64,{img1}");
            background-position: center;
            background-size: cover; 
            background-repeat: no-repeat;}}
          </style>
           """
st.markdown(page_bg_img, unsafe_allow_html=True)
hide_streamlit_style = """
            <style>
            footer {visibility: hidden;}
            #MainMenu {visibility: hidden;}
            </style>
            """
st.markdown(hide_streamlit_style, unsafe_allow_html=True)
st.markdown(
        """
        ### Test
        ### Dedicated to creative arts.
       
        <style>
        .stButton > button {
            border-radius: 15%
         }
        </style>
      """
    , unsafe_allow_html=True)      
    """
    , unsafe_allow_html=True)
st.button("Enter")



