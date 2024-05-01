import replicate
import streamlit as st

import os
# REPLICATE_API_TOKEN = getpass()
REPLICATE_API_TOKEN = st.secrets['RAT']

os.environ['REPLICATE_API_TOKEN'] = REPLICATE_API_TOKEN

prompt = st.text_input("Enter input: ")
input = {
    "top_p": 1,
    "prompt": prompt,
    "temperature": 0.75,
    "system_prompt": "You are a helpful, respectful and honest assistant. Always answer as helpfully as possible, while being safe. Your answers should not include any harmful, unethical, racist, sexist, toxic, dangerous, or illegal content. Please ensure that your responses are socially unbiased and positive in nature.\n\nIf a question does not make any sense, or is not factually coherent, explain why instead of answering something not correct. If you don't know the answer to a question, please don't share false information.",
    "max_new_tokens": 800,
    "repetition_penalty": 1
}
#=> " Of course, I'd be happy to help! Tailoring a men's suit...

for event in replicate.stream(
    "meta/llama-2-7b-chat",
    input=input):
  st.write(event, end="")
