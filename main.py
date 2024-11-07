import streamlit as st
import requests
import pandas as pd  # Import the pandas library

# WordPress API URL
api_url = "https://wp.dollarsmart.co/wp-json/n8n-api/v1/get-n8n-data"

# Streamlit UI
st.title("WordPress API Call Interface")

# Sidebar for input fields
with st.sidebar:
    user_id = st.text_input("User ID")
    api_key = st.text_input("API Key", type="password")
    st.markdown(
        "Where is API Key: [https://wp.dollarsmart.co/api-key/](https://wp.dollarsmart.co/api-key/)"
    )
    data = st.text_input("Data")

if st.button("Use Tool"):
    if not user_id or not api_key:
        st.error("Please enter both User ID and API Key.")
    else:
        # Prepare the API request payload
        payload = {"user_id": user_id, "api_key": api_key, "data": data}

        # Call the WordPress API
        response = requests.post(api_url, json=payload)

        # Handle the API response
        if response.status_code == 200:
            data = response.json()
            if data.get("status") == "success":
                st.success(
                    f"API call successful! New balance: {data.get('new_balance')}"
                )
                # Show the response data
                st.write(f"**Points Deducted:** {data.get('points_deducted')}")
                st.write(f"**New Balance:** {data.get('new_balance')}")
                # Display the entire JSON response
                st.write(f"**Full Response Data:**")
                st.json(data)

                # Display the n8n_response data in a table
                st.write(f"**n8n Response Data:**")
                n8n_response = data.get('data', {}).get('n8n_response', [])
                if n8n_response:
                    st.table(
                        pd.DataFrame(n8n_response))  # Now pandas is available
                else:
                    st.write("No data in n8n_response.")

            else:
                st.error(f"Failed: {data.get('message')}")
        elif response.status_code == 401:
            st.error("Authentication failed: Invalid User ID or API Key.")
        elif response.status_code == 403:
            st.warning("Insufficient points balance.")
        else:
            st.error(
                f"API call failed with status code: {response.status_code}")
