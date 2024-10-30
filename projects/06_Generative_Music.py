import streamlit as st

st.header('Generative Music', divider='green')

st.warning("This model is now hosted on [Huggingface](https://huggingface.co/spaces/ccapo/portfolio)")

st.markdown("#### What are Recurrent Neural Networks?")
st.markdown("A recurrent neural network is a class of artificial neural networks that make use of sequential information. They are called recurrent because they perform the same function for every single element of a sequence, with the result being dependent on previous computations. Whereas outputs are independent of previous computations in traditional neural networks.")
st.markdown("In this project we will use a **Long Short-Term Memory** (LSTM) network. They are a type of Recurrent Neural Network that can efficiently learn via gradient descent. Using a gating mechanism, LSTMs are able to recognise and encode long-term patterns. LSTMs are extremely useful to solve problems where the network has to remember information for a long period of time as is the case in music and text generation.")
st.markdown("#### Data")
st.markdown("The data that our model will be trained on will consist of piano MIDI files of Final Fantasy soundtracks, but any set of MIDI files consisting of a single instrument would work.")
st.markdown("The sequence of notes and chords from the MIDI files are broken down into increments of 100, which are used to predict the next note or chord.")
st.markdown("#### Model")
st.markdown("For this project we will use a network consisting of three LSTM layers, three Dropout layers, two Dense layers and one activation layer.")
st.markdown("It may be possible to improve this model by playing around with the the structure of the network, or adding new categories (e.g. varying note duration, rest periods between notes, etc). However, to achieve satisfying results with more classes we would also have to increase the depth of the LSTM network.")
st.markdown("*This is based off the tutorial by Sigurður Skúli [How to Generate Music using a LSTM Neural Network in Keras](https://towardsdatascience.com/how-to-generate-music-using-a-lstm-neural-network-in-keras-68786834d4c5)*")
st.divider()