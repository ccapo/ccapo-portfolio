import streamlit as st
# from llama_cpp import Llama
import re

st.header('Fine Tuned LLM', divider='green')

st.markdown("#### What is a LLM?")
st.markdown("LLM stands for Large Language Model, which are mathematical models trained to predict the next set of words based on the prompt provided to it.")
st.markdown("In this case we are using [Meta's LLama 3.1 (8B) Instruct](meta-llama/Llama-3.1-8B-Instruct) as our base model.")
st.markdown("#### What is a fine tuning?")
st.markdown("Fine tuning is the processes of tweaking the response of the LLM to particular subset of prompts. Most LLMs are trained on a large corpus of generic data, fine tuning just guides the LLM to a specific use case.")
st.markdown("In this case I have fine tuned the base model on [Microsoft's Orca Math Word Problems](https://huggingface.co/datasets/microsoft/orca-math-word-problems-200k), so the chatbot below is more of math assistant. Though it occasionally gets the wrong answer, it is willing to try again. I only fine tuned on 1000 math word problems, but I could try to train on the entire dataset in the future.")
st.markdown("#### What is quantization?")
st.markdown("Most LLM are quite large, often too large to fit into a computer's memory. So ML developers employ Graphic Processing Units (GPUs) with large amounts of memory to train or make use of such LLMs.")
st.markdown("However not everyone has access to such resources, so quantization is the process of decreasing the size of a model so that it can fit into memory (GPU or CPU). The process of quantization decreases the precision used to store the models parameters, at the cost of the model's accuracy.")
st.markdown("In this case after I fine tuned the LLama 3.1 (8B) base model, it was quantized to 4 bits which offers reasonable model accuracy at 25% the base model size.")

st.warning("**Work In Progress**")

if "messages" not in st.session_state:
    st.session_state["messages"] = [{"role": "system", "content": "You are a helpful math assistant."}, {"role": "assistant", "content": "What math problem can I help you with today?"}]

def chat_action(prompt):
    if len(st.session_state.messages) > 6:
        st.session_state.messages.pop(2)
        st.session_state.messages.pop(2)
    st.session_state["messages"].append({"role": "user", "content": prompt})
    st.chat_message("user").write(prompt)

    # with st.spinner(f"Generating response"):
    #     response = llm.create_chat_completion(
    #         messages=st.session_state.messages,
    #         temperature = 0.7,
    #         repeat_penalty = 1.1,
    #         stop = "[/INST]"
    #     )
    #     msg = response['choices'][0]['message']['content']
    #     msg = re.sub(r'(<<|\[)*(INST|SYS)(>>|\])*', '', msg)
    #     st.session_state["messages"].append({"role": "assistant", "content": msg})
    #     st.chat_message("assistant").write(msg)

# @st.cache_resource
# def load_llm():
#     #### Import Model from Huggingface
#     llm = Llama.from_pretrained(
#         repo_id="ccapo/llama-3.1-8b-chat-math-teacher-GGUF",
#         filename="*Q4_K_M.gguf",
#         verbose=False,
#         n_ctx=2048
#     )
#     return llm

for msg in st.session_state.messages:
    if msg["role"] != "system":
        with st.chat_message(name=msg["role"]):
            st.write(msg["content"])

# with st.spinner(f"Loading LLM"):
#     llm = load_llm()

if prompt := st.chat_input():
    chat_action(prompt)