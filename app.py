import streamlit as st

# --- 1. SETUP ---
st.set_page_config(page_title="Fenneric AI", page_icon="🛡️")

# --- 2. SIDEBAR ---
with st.sidebar:
    st.title("🛡️ Fenneric HQ")
    st.write("---")
    st.metric(label="System Status", value="ACTIVE")
    st.metric(label="Version", value="2.5")

# --- 3. MAIN CHAT ---
st.title("🛡️ Fenneric AI")
st.caption("Founder Edition | Secure Interface")

if "messages" not in st.session_state:
    st.session_state.messages = []

# Display history
for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.markdown(msg["content"])

# --- 4. INPUT ---
if prompt := st.chat_input("Enter command..."):
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)
    
    with st.chat_message("assistant"):
        response = f"Fenneric Intelligence: '{prompt}' received. Analysis complete. System is 100% stable."
        st.markdown(response)
    st.session_state.messages.append({"role": "assistant", "content": response})
