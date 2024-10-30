import streamlit as st

st.header('Fine Tuned LLM', divider='green')

st.warning("This model is now hosted on [Huggingface](https://huggingface.co/spaces/ccapo/portfolio)")

st.markdown("#### What is a LLM?")
st.markdown("LLM stands for Large Language Model, which are mathematical models trained to predict the next set of words based on the prompt provided to it.")
st.markdown("In this case we are using [Meta's LLama 3.1 (8B) Instruct](https://huggingface.co/meta-llama/Llama-3.1-8B-Instruct) as our base model.")
st.markdown("#### What is a fine tuning?")
st.markdown("Fine tuning is the processes of tweaking the response of the LLM to particular subset of prompts. Most LLMs are trained on a large corpus of generic data, fine tuning just guides the LLM to a specific use case.")
st.markdown("In this case I have fine tuned the base model on [Microsoft's Orca Math Word Problems](https://huggingface.co/datasets/microsoft/orca-math-word-problems-200k), so the chatbot below is more of math assistant. Though it occasionally gets the wrong answer, it is willing to try again. I only fine tuned on 1000 math word problems, but I could try to train on the entire dataset in the future.")
st.markdown("#### What is quantization?")
st.markdown("Most LLM are quite large, often too large to fit into a computer's memory. So ML developers employ Graphic Processing Units (GPUs) with large amounts of memory to train or make use of such LLMs.")
st.markdown("However not everyone has access to such resources, so quantization is the process of decreasing the size of a model so that it can fit into memory (GPU or CPU). The process of quantization decreases the precision used to store the models parameters, at the cost of the model's accuracy.")
st.markdown("In this case after I fine tuned the LLama 3.1 (8B) base model, it was quantized to 4 bits which offers reasonable model accuracy at 25% the base model size.")
st.markdown("*This is based off the tutorial by Abid Ali Awan [Fine-Tuning Llama 3 and Using It Locally: A Step-by-Step Guide](https://www.datacamp.com/tutorial/llama3-fine-tuning-locally)*")
st.divider()