import os
import streamlit as st
import requests
# Define the base URI of the API
#   - Potential sources are in `.streamlit/secrets.toml` or in the Secrets section
#     on Streamlit Cloud
#   - The source selected is based on the shell variable passend when launching streamlit
#     (shortcuts are included in Makefile). By default it takes the cloud API url
if 'API_URI' in os.environ:
    BASE_URI = st.secrets[os.environ.get('API_URI')]
else:
    BASE_URI = st.secrets['cloud_api_uri']
# Add a '/' at the end if it's not there
BASE_URI = BASE_URI if BASE_URI.endswith('/') else BASE_URI + '/'
# Define the url to be used by requests.get to get a prediction (adapt if needed)
url = BASE_URI + 'predict'
# Just displaying the source for the API. Remove this in your final version.
#st.markdown(f”Working with {url}“)
# TODO: Add some titles, introduction, ...

def main():
    st.markdown('# Predicting Crypto Prices')
    # TODO: Request user input
    options = ['BTC', 'ETH', 'XRP']
    Coin = st.radio('Select a coin', options)
    st.write('The predicted prices are in US dollars (USD)')

    if Coin == 'BTC':
        st.write('We run the model for BTC and give prediction')
    elif Coin == 'ETH':
        st.write('We run the model for ETH and give prediction')
    else:
        st.write('We run the model for XRP and give prediction')
    # TODO: Call the API using the user's input
    #   - url is already defined above
    #   - create a params dict based on the user's input
    #   - finally call your API using the requests package
    # Create a params dict based on the user's input
    params = {
        'selected_option': Coin
    }
    # Function to call the API
    def call_api(url, params):
        response = requests.get(url, params=params)
        return response.json()

    if Coin == 'BTC':
        result = call_api(url, params)
        #st.write(“API Response:“)
        #st.json(result)
        st.write(result['prediction']['2528'])
    # TODO: retrieve the results
    #   - add a little check if you got an ok response (status code 200) or something else
    #   - retrieve the prediction from the JSON
    # TODO: display the prediction in some fancy way to the user
    # TODO: [OPTIONAL] maybe you can add some other pages?
    #   - some statistical data you collected in graphs
    #   - description of your product
    #   - a 'Who are we?'-page


# About page
def about():
    st.title("About")
    st.write("""
    ## Cryptocurrency Price Prediction
    This application uses an LSTM (Long Short-Term Memory) neural network to predict the future prices of a cryptocurrency based on its historical data from BINANCE API.

    ### Steps:
    1. **Data Preprocessing**: Normalize the data to a range of 0 to 1 using Normalization layer.
    2. **Dataset Preparation**: Create input-output pairs using a look-back period.
    3. **Model Building**: Construct an LSTM model using TensorFlow and Keras.
    4. **Training**: Train the model on the training dataset.
    5. **Prediction**: Make predictions on both training and testing datasets.
    6. **Visualization**: Plot the original data along with the predicted values.

    ### Libraries Used:
    - **Numpy**: For numerical computations.
    - **Pandas**: For data manipulation.
    - **Matplotlib**: For plotting the data.
    - **Scikit-learn**: For preprocessing and evaluation.
    - **TensorFlow**: For building and training the LSTM model.

    ### Note:
    This is a simple example and not meant for actual financial trading. The predictions made by this model should not be used for making financial decisions.
    """)

def team():
    st.title("Team Members")
    st.write("""
    ## Meet the Team

    ### Mike Nilges
    **Role**: Data Scientist/Economist
    - I am a Economics student, focussing on quantitative economics and financial markets.
      I am looking forward to working as a quantitative researcher in the future.

    ### Busra Kocer
    **Role**: Data Scientist/Sentimental Analyst
    - I am engineer. I am currently living in Berlin.
      I worked in energy field before. I have coding experience as well. I like traveling and skiing.

    ### Mahsa Sayyary Namin
    **Role**: Data Scientist/ Back End Developer
    - I received my PhD in mathematics in 2020 from Max Planck Institute for Mathematics in the Sciences in Leipzig.
      Then I was a postdoctoral researcher in the mathematics department at Goethe University in Frankfurt .
      Now, I like to start a new career as Data Scientist .


    ### Yiannis Gregoriou
    **Role**: Data Scientist
    - I am a Civil Engineering that worked abroad for the past 10 years. What lead me to learn coding is to start applying
    Data into Construction projects and project control. I have a few ideas that I want to implement within the course.
    """)

# Navigation
st.sidebar.title("Navigation")
page = st.sidebar.selectbox("Go to", ["Main", "About", "Team"])

if page == "Main":
    main()
elif page == "About":
    about()
else:
    team()
