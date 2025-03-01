import streamlit as st
import requests

st.title("Customer Segmentation using K-Means")
st.write("Enter Customer Details to Predict the Cluster")

annual_income = st.number_input("Annual Income", min_value=0, step=1)
spending_score = st.number_input("Spending Score", min_value=0, max_value=100, step=1)


CLUSTER_DETAILS = {
    1: "**Cluster 1:** Customers with **moderate annual income** and **moderate spending scores**. They form the **middle segment** of customers.",
    2: "**Cluster 2:** Customers with **high annual income** and **high spending scores**. These are **potential premium customers**.",
    3: "**Cluster 3:** Customers with **high annual income** but **low spending scores**. They may be **financially conservative or dissatisfied**.",
    4: "**Cluster 4:** Customers with **low annual income** and **low spending scores**. Likely to be **price-sensitive customers**.",
    5: "**Cluster 5:** Customers with **low annual income** but **high spending scores**. They could be **impulse buyers or brand-loyal customers**."
}

if st.button("Predict Cluster"):
    api_url = "http://127.0.0.1:5000/predict"
    data = {"features": [annual_income, spending_score]}
    
    try:
        response = requests.post(api_url, json=data)
        result = response.json()

        if "cluster" in result:
            cluster_number = result["cluster"]
            st.success(f"The customer belongs to **Cluster {cluster_number}**")
            st.info(CLUSTER_DETAILS.get(cluster_number, "Unknown Cluster"))
        else:
            st.error("❌ Error: Unable to predict cluster.")

    except Exception as e:
        st.error(f"Error connecting to API: {e}")