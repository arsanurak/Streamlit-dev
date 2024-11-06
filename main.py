import streamlit as st
import requests

# WordPress API URL
api_url = "http://your-wordpress-site.com/wp-json/custom/v1/api-call"

# Streamlit UI
st.title("WordPress API Call Interface")

# Input fields for API Key and User ID
user_id = st.text_input("User ID")
api_key = st.text_input("API Key", type="password")

if st.button("Use Tool"):
  if not user_id or not api_key:
    st.error("Please enter both User ID and API Key.")
  else:
    # Prepare the API request payload
    payload = {"user_id": user_id, "api_key": api_key}

    # Call the WordPress API
    response = requests.post(api_url, json=payload)

    # Handle the API response
    if response.status_code == 200:
      data = response.json()
      if data.get("status") == "success":
        st.success(
            f"API call successful! New balance: {data.get('new_balance')}")
      else:
        st.error(f"Failed: {data.get('message')}")
    elif response.status_code == 401:
      st.error("Authentication failed: Invalid User ID or API Key.")
    elif response.status_code == 403:
      st.warning("Insufficient points balance.")
    else:
      st.error(f"API call failed with status code: {response.status_code}")
