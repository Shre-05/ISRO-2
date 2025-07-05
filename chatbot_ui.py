import streamlit as st

st.set_page_config(page_title="🛰️ ISRO Help Bot", layout="centered")
st.title("🛰️ ISRO Help Bot")
st.markdown("Ask me anything about MOSDAC from the questions below 👇")

query = st.text_input("🔍 Your Question:")

if query:
    q = query.lower().strip()

    if "purpose of mosdac" in q or "main purpose of mosdac" in q or "what is mosdac" in q:
        st.success("MOSDAC provides satellite data products for ocean, land, and atmosphere.")

    elif "how to access mosdac" in q or "download data" in q or "how can i get data" in q:
        st.success("To access MOSDAC data, users must register and log in to download available products.")

    elif "is mosdac data free" in q or "free to use" in q or "mosdac data cost" in q:
        st.success("Yes, MOSDAC data is free for academic and research purposes after registration.")

    elif "which satellites are used by mosdac" in q or "supported satellites" in q or "satellites used by mosdac" in q:
        st.success("MOSDAC hosts data from Indian satellites like INSAT-3D, INSAT-3DR, Megha-Tropiques, SCATSAT-1, and others.")

    elif "what data is available" in q or "information on mosdac" in q or "what products mosdac provides" in q:
        st.success("MOSDAC provides data related to rainfall, cloud motion vectors, ocean winds, temperature, humidity, and more.")

    else:
        st.error("❌ Sorry, I can only answer a few demo questions about MOSDAC. Try asking: 'What is the main purpose of MOSDAC?'")

