import streamlit as st

# Load Image
gru = Image.open("assets/gru.png")
nn = Image.open("assets/nn.png")

# Load the Model
st.header('Stock Market Forecast', divider='green')

st.warning("This model is now hosted on [Huggingface](https://huggingface.co/spaces/ccapo/portfolio)")

st.markdown("#### Time Series Forecasting")
st.markdown("Time series forecasting uses information regarding historical values and associated patterns to predict future activity. Most often, this relates to trend analysis, cyclical fluctuation analysis, and issues of seasonality. As with all forecasting methods, success is not guaranteed.")

st.markdown("#### GRU Model")
st.markdown("Gated recurrent unit is essentially a simplified LSTM. It has the exact same role in the network. The main difference is in the number of gates and weights — GRU is somewhat simpler. It has 2 gates. Since it does not have an output gate, there is no control over the memory content. The update gate controls the information flow from the previous activation, and the addition of new information as well, while the reset gate is inserted into the candidate activation.")

st.image(gru, caption = "Gated Recurrent Unit (GRU)")

st.markdown("Below are the analyses of four stocks using a GRU-based model: *Amazon*, *Google*, *IBM* and *Microsoft*")
st.markdown("The model consists of the following: A single input and output dimension (i.e. Closing Price) and two hidden layers, with 32 GRU nodes per layer. These models were trained for 105 epochs each.")
st.image(nn, caption = "GRU-based Model")

st.divider()

st.markdown("Below each graph is the mean square error (MSE) for the train and test sets, where the test set consists of the last 20 days.")