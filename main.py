import streamlit as st
from streamlit_chat import message
from bardapi import Bard
import json

with open('credentials.json', 'r') as f:
    file = json.load(f)
    token = file["token"]


# Function to generate the output
def generate_response(prompt):
    bard = Bard(token=token)
    response = bard.get_answer(prompt)['content']
    return response


# Function to receive user queries(input)
def get_text():
    input_text = st.text_input("Hello", "", key='input')
    return input_text


# Title of the streamlit app
st.title('My ChatBOT!')

# to change the background of the chatbot UI page
changes = '''
<style>
[data-testid="stAppViewContainer"]
    {
    background-image:url("https://images.pexels.com/photos/6153354/pexels-photo-6153354.jpeg?auto=compress&cs=tinysrgb&w=1260&h=750&dpr=2");
    background-position: 60% 40%;
    background-repeat: no-repeat;
    background-size: cover;
    }
</style>
'''
st.markdown(changes, unsafe_allow_html=True)

if 'generated' not in st.session_state:
    st.session_state['generated'] = []

if 'past' not in st.session_state:
    st.session_state['past'] = []

# Accepting user input
user_input = get_text()
if user_input:
    print(user_input)
    output = generate_response(user_input)
    print(output)
    st.session_state.past.append(user_input)
    st.session_state.generated.append(output)

if st.session_state['generated']:
    # for loop is to print the chat in reverse order
    for i in range(len(st.session_state['generated']) - 1, -1, -1):
        # below syntax identify as every message as a unique key
        message(st.session_state['generated'][i], key=str(i))
        message(st.session_state['past'][i], key="user_" + str(i), is_user=True)
