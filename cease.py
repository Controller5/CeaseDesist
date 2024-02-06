import streamlit as st
from streamlit import session_state as ss
import pyperclip


if "letter" not in st.session_state:
    st.session_state.letter = ""
if 'platform_tos' not in st.session_state:
    st.session_state.platform_tos = ""
if 'platform' not in st.session_state:
    st.session_state.platform = ""
if 'st.session_state.platform_tos_args' not in st.session_state:
    st.session_state.platform_tos_args = ""
if 'reporting_text' not in st.session_state:
    st.session_state.reporting_text = ""
if 'platform_nn' not in st.session_state:
    st.session_state.platform_nn = ""
if 'email' not in ss:
    ss.email = ""



st.title("Cease & Desist Letter")

def sidew(n):
    st.sidebar.title(n)


st.sidebar.title("Guide to finding the right place to send your letter.")
sidew("Instagram")
sidew("X/Twitter")
sidew("Meta/Facebook")

with st.sidebar.container():
    st.sidebar.write("""_Email:_
                \nlegal@facebook.com 
                \n _Send a paper version to:_
                \n Facebook 
                \n Attn: Legal Department 
                \n 156 University Ave 
                \n Palo Alto, CA \n 94301 """)

sidew("Google")
sidew("Youtube")
sidew("Reddit")


name = st.text_input("Your name", key="name")
ss.email = st.text_input("Your email. We recommend using a unique email address for this purpose, to maintain your privacy. ")
service1 = st.selectbox("Platform/Publisher", ['Other', 'Instagram', 'X/Twitter'])
service2 = st.text_input("Other publisher of doxing materials ",
                         placeholder="Optional, use only if you marked Other above",
                         key="service")

if service1 == "Other":
    st.session_state.platform = service2
if service1 == 'Instagram':
    st.session_state.platform = 'instagram'
if service1 == 'X/Twitter':
    st.session_state.platform = "twitter"
    st.session_state.platform_nn = "X/Twitter"


if st.session_state.platform == 'instagram':
    st.session_state.platform_tos = "https://www.facebook.com/help/instagram/477434105621119"
    st.session_state.platform_tos_args = " Instagram's \"Community Guidelines\" in particular the section entitled, \"Follow the law\" and the section entitled, \"Respect other members of the Instagram community,\" states with clarity that Instagram will \"remove content that contains credible threats or hate speech, content that targets private individuals to degrade or shame them, personal information meant to blackmail or harass someone...\""
    if st.session_state.reported is True:
        st.session_state.reporting_text = "I have already reported the material in question via the protocols established in Instagram's Reporting Portal found at: https://help.instagram.com/contact/383679321740945."
if st.session_state.platform == 'twitter':
    st.session_state.platform_tos = "https://twitter.com/en/tos"


url = st.text_input("URL of harassment material", placeholder="URL where the harassment material can be currently found")
date_discovery = st.date_input("Date of discovery of doxing", key="date", format="MM/DD/YYYY")
st.checkbox("Have you reported it on the platform/site already?", key="reported")
describe = st.text_area("""
Description of the harassment: 
\n \(Copy/Paste so you don't lose data\)""", key="describe", placeholder="Describe the manner and location of the doxing that you experienced. Describe the harms that you suffered as a result of this harassment.")

today_date = st.date_input("Today's date", key="today", label_visibility="visible", format="MM/DD/YYYY")

with st.container():

    if st.button("Generate Letter", key="generate"):
        st.session_state.letter = f"""Dear {st.session_state.platform_nn},
            \nMy name is {name}. On {date_discovery} I discovered that I had been \"doxed,\" a recognized form of online harassment. Please find a summary of the details of the harassment herein:
            \n{describe}
            \nPublication of the doxing materials are to be found at {url} as of {date_discovery}.  {st.session_state.reporting_text}
            \n I respectfully demand that {st.session_state.platform_nn} cease the publication of the aforementioned harassment materials, and desist from future publication. Confirmation of compliance with this demand should be sent to {ss.email} as soon as completed. 
            \n Doxing is an English word, short for Dropping Documents, for harassment through the publishing of PII (Personally Identifiable Information). Because of the interconnected nature of the internet, PII published online spreads quickly around the world and can cause irreparable harm to a doxed individual.
            \n This letter shall serve as notice that absent the swift removal from {st.session_state.platform_nn}'s site of the aforemention doxing material I am prepared to retain an attorney and take steps towards the resolution of this matter. The harassment published on your platform may violate federal law against stalking, and/or state law, including but not limited to, in the states of Arizona, Colorado, Florida, Kentucky, Minnesota, Oklahoma, and Oregon, each of whom have laws explicitly targeting the practice of doxing. 
            \nFurther, I am prepared to retain counsel and seek resolution under the laws of various foreign nations in which this published material is accessible, including but not limited to, France, Germany, the United Kingdom, and Canada. 
            \nThe harassment materials published at {url} fall strictly within the language regarding prohibited postings found at {st.session_state.platform_nn}'s Terms of Service found at {st.session_state.platform_tos} {st.session_state.platform_tos_args}
            \nFinally, I appeal to the humanity within your company to recognize that this harassment has been harmful to me and should end immediately. Thank you for your time in consideration of this letter.
            \nYours sincerely,
            \n/s/ {name}
            \n{today_date}
        """
        st.success("Letter Generated")

    # if st.button("Copy to Clipboard", key="copy"):
    #     pyperclip.copy(st.session_state.letter)
    #     st.success("Copied to Clipboard")

    if st.download_button("Download Letter",
        st.session_state.letter,
        f"ceasedesist_{name}.txt"):
            st.success("Download Initiated")

st.divider()
st.write(st.session_state.letter)