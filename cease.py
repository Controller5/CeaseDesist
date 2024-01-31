import streamlit as st

if "letter" not in st.session_state:
    st.session_state.letter = ""

st.title("Cease & Desist Letter")

st.sidebar.header("Guide to finding the right place to send your letter.")
st.sidebar.markdown(""" Guide here:
    \n Instagram
    \n Facebook/Meta
    \n Google
    \n 
    \n X / Twitter
    \n other site: See Host lookup
    \n 
 """)


name = st.text_input("Your name", key="name")
date_discovery = st.date_input("Date of discovery of doxxing", key="date")
describe = st.text_area("""Description of the harrassment and sites on which you were doxxed. 
\n \(Copy/Paste so you don't lose data\)""", key="describe")
service = st.text_input("Publisher of doxxing materials", key="service")
today_date = st.date_input("Today's date", key="today")

if st.button("Generate Letter", key="generate"):
    st.session_state.letter = f"""
        Dear {service}
        \nMy name is {name}. On {date_discovery} I discovered that I had been \"doxxed,\" a recognized form of online harassment. Please find a summary of the details of the harassment herein:
        \n {describe}
        \n Signed, 
        \n /s/ {name} 
        \n {today_date}
    """
    st.download_button("Download Letter as .txt", st.session_state.letter, f"ceasedesist_{name}.txt")
st.divider()
st.markdown(st.session_state.letter)




