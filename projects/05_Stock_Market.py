import streamlit as st
import pickle
import plotly.graph_objects as go
from PIL import Image

@st.cache_resource
def load_model():
    model_file = open('./models/stock_market_model.pkl', 'rb')
    amazon_predictions = pickle.load(model_file)
    amazon_scores = pickle.load(model_file)
    google_predictions = pickle.load(model_file)
    google_scores = pickle.load(model_file)
    ibm_predictions = pickle.load(model_file)
    ibm_scores = pickle.load(model_file)
    microsoft_predictions = pickle.load(model_file)
    microsoft_scores = pickle.load(model_file)
    model_file.close()
    return amazon_predictions, amazon_scores, google_predictions, google_scores, ibm_predictions, ibm_scores, microsoft_predictions, microsoft_scores

# Load Image
gru = Image.open("assets/gru.png")
nn = Image.open("assets/nn.png")

# Load the Model
amazon_predictions, amazon_scores, google_predictions, google_scores, ibm_predictions, ibm_scores, microsoft_predictions, microsoft_scores = load_model()

st.header('Stock Market Forecast', divider='green')

st.markdown("#### Time Series Forecasting")
st.markdown("Time series forecasting uses information regarding historical values and associated patterns to predict future activity. Most often, this relates to trend analysis, cyclical fluctuation analysis, and issues of seasonality. As with all forecasting methods, success is not guaranteed.")

st.markdown("#### GRU Model")
st.markdown("Gated recurrent unit is essentially a simplified LSTM. It has the exact same role in the network. The main difference is in the number of gates and weights — GRU is somewhat simpler. It has 2 gates. Since it does not have an output gate, there is no control over the memory content. The update gate controls the information flow from the previous activation, and the addition of new information as well, while the reset gate is inserted into the candidate activation.")

st.image(gru, caption = "Gated Recurrent Unit (GRU)")

st.markdown("Below are the analyses of four stocks using a GRU-based model: *Amazon*, *Google*, *IBM* and *Microsoft*")
st.markdown("The model consists of the following: A single input and output dimension (i.e. Closing Price) and two hidden layers, with 32 GRU nodes per layer. These models were trained for 105 epochs each.")
st.image(nn, caption = "GRU-based Model")
st.markdown("Below each graph is the mean square error (MSE) for the train and test sets, where the test set consists of the last 20 days.")

fig1 = go.Figure()
fig1.add_trace(go.Scatter(go.Scatter(x=amazon_predictions['Date'], y=amazon_predictions['Train Prediction'],
                    mode='lines',
                    name='Train Prediction')))
fig1.add_trace(go.Scatter(x=amazon_predictions['Date'], y=amazon_predictions['Test Prediction'],
                    mode='lines',
                    name='Test Prediction'))
fig1.add_trace(go.Scatter(go.Scatter(x=amazon_predictions['Date'], y=amazon_predictions['Actual Value'],
                    mode='lines',
                    name='Actual Value')))
fig1.update_layout(
    title="Amazon Stock Prediction",
    xaxis_title="Date",
    yaxis_title="Close (USD)",
    showlegend=True,
    template = 'plotly_dark'
)

annotations = []
annotations.append(dict(xref='paper', yref='paper', x=0.0, y=1.05,
                              xanchor='left', yanchor='bottom',
                              text='',
                              showarrow=False))
fig1.update_layout(annotations=annotations)
st.plotly_chart(fig1, use_container_width=True)

# MSE on train and test sets
st.markdown(f"Train MSE: {amazon_scores[0]}, Test MSE: {amazon_scores[1]}")

fig2 = go.Figure()
fig2.add_trace(go.Scatter(go.Scatter(x=google_predictions['Date'], y=google_predictions['Train Prediction'],
                    mode='lines',
                    name='Train Prediction')))
fig2.add_trace(go.Scatter(x=google_predictions['Date'], y=google_predictions['Test Prediction'],
                    mode='lines',
                    name='Test Prediction'))
fig2.add_trace(go.Scatter(go.Scatter(x=google_predictions['Date'], y=google_predictions['Actual Value'],
                    mode='lines',
                    name='Actual Value')))
fig2.update_layout(
    title="Google Stock Prediction",
    xaxis_title="Date",
    yaxis_title="Close (USD)",
    showlegend=True,
    template = 'plotly_dark'
)

annotations = []
annotations.append(dict(xref='paper', yref='paper', x=0.0, y=1.05,
                              xanchor='left', yanchor='bottom',
                              text='',
                              showarrow=False))
fig2.update_layout(annotations=annotations)
st.plotly_chart(fig2, use_container_width=True)

# MSE on train and test sets
st.markdown(f"Train MSE: {google_scores[0]}, Test MSE: {google_scores[1]}")

fig3 = go.Figure()
fig3.add_trace(go.Scatter(go.Scatter(x=ibm_predictions['Date'], y=ibm_predictions['Train Prediction'],
                    mode='lines',
                    name='Train Prediction')))
fig3.add_trace(go.Scatter(x=ibm_predictions['Date'], y=ibm_predictions['Test Prediction'],
                    mode='lines',
                    name='Test Prediction'))
fig3.add_trace(go.Scatter(go.Scatter(x=ibm_predictions['Date'], y=ibm_predictions['Actual Value'],
                    mode='lines',
                    name='Actual Value')))
fig3.update_layout(
    title="IBM Stock Prediction",
    xaxis_title="Date",
    yaxis_title="Close (USD)",
    showlegend=True,
    template = 'plotly_dark'
)

annotations = []
annotations.append(dict(xref='paper', yref='paper', x=0.0, y=1.05,
                              xanchor='left', yanchor='bottom',
                              text='',
                              showarrow=False))
fig3.update_layout(annotations=annotations)
st.plotly_chart(fig3, use_container_width=True)

# MSE on train and test sets
st.markdown(f"Train MSE: {ibm_scores[0]}, Test MSE: {ibm_scores[1]}")

fig4 = go.Figure()
fig4.add_trace(go.Scatter(go.Scatter(x=microsoft_predictions['Date'], y=microsoft_predictions['Train Prediction'],
                    mode='lines',
                    name='Train Prediction')))
fig4.add_trace(go.Scatter(x=microsoft_predictions['Date'], y=microsoft_predictions['Test Prediction'],
                    mode='lines',
                    name='Test Prediction'))
fig4.add_trace(go.Scatter(go.Scatter(x=microsoft_predictions['Date'], y=microsoft_predictions['Actual Value'],
                    mode='lines',
                    name='Actual Value')))
fig4.update_layout(
    title="Microsoft Stock Prediction",
    xaxis_title="Date",
    yaxis_title="Close (USD)",
    showlegend=True,
    template = 'plotly_dark'
)

annotations = []
annotations.append(dict(xref='paper', yref='paper', x=0.0, y=1.05,
                              xanchor='left', yanchor='bottom',
                              text='',
                              showarrow=False))
fig4.update_layout(annotations=annotations)
st.plotly_chart(fig4, use_container_width=True)

# MSE on train and test sets
st.markdown(f"Train MSE: {microsoft_scores[0]}, Test MSE: {microsoft_scores[1]}")