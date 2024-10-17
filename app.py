import requests
import streamlit as st

# ExchangeRate-API URL with the provided API key
api_url = "https://v6.exchangerate-api.com/v6/d10cdf4e0852ad5e6a789660/latest/USD"

# Function to get exchange rates
def get_exchange_rates(api_url):
    response = requests.get(api_url)
    data = response.json()
    if response.status_code == 200:
        return data['conversion_rates']
    else:
        st.error("Error fetching data from the API. Please check the API key or URL.")
        return None

# Fetch exchange rates
rates = get_exchange_rates(api_url)

# Create currency converter app
if rates:
    st.title("Currency Converter")

    # Create dropdowns for currency selection and input for amount
    currencies = list(rates.keys())
    from_currency = st.selectbox("From Currency:", currencies)
    to_currency = st.selectbox("To Currency:", currencies)
    amount = st.number_input("Amount:", min_value=0.0, value=1.0, step=0.01)

    # Perform conversion when button is clicked
    if st.button("Convert"):
        if from_currency and to_currency:
            # Calculate the conversion rate
            conversion_rate = rates[to_currency] / rates[from_currency]
            converted_amount = amount * conversion_rate
            # Display the converted amount
            st.success(f"{amount:.2f} {from_currency} is equal to {converted_amount:.2f} {to_currency}")
        else:
            st.error("Please select both currencies for conversion.")
else:
    st.error("Could not fetch exchange rates. Please try again later.")
