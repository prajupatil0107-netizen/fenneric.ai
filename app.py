import streamlit as st

# --- 1. SYSTEM SETUP ---
if "messages" not in st.session_state:
    st.session_state.messages = []

st.title("🛡️ Fenneric AI")
st.subheader("2026 Founder Edition")

for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.markdown(msg["content"])

if prompt := st.chat_input("Ask Fenneric..."):
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)
    
    reply = "System processing... How else can I help the Empire today?"
    with st.chat_message("assistant"):
        st.markdown(reply)
    st.session_state.messages.append({"role": "assistant", "content": reply})
