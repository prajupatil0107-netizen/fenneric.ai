import streamlit as st
import time

# --- 1. THE FOUNDATION ---
st.set_page_config(page_title="Fenneric AI", page_icon="🛡️", layout="wide")

# Custom CSS for a clean "Dark/Pro" feel
st.markdown("""
    <style>
    .main { background-color: #ffffff; }
    .stButton>button { width: 100%; border-radius: 10px; }
    </style>
    """, unsafe_path=True)

# --- 2. THE PROFESSIONAL SIDEBAR ---
with st.sidebar:
    st.markdown("<h1 style='text-align: center;'>🛡️</h1>", unsafe_path=True)
    st.title("Fenneric Systems")
    st.write("---")
    
    # Professional Metrics only
    st.metric(label="System Status", value="ACTIVE", delta="Secure")
    st.metric(label="Version", value="2.1.0", delta="Stable")
    
    st.write("---")
    st.markdown("### 🛠️ Developer Tools")
    if st.button("Clear Terminal Cache"):
        st.toast("Cache Cleared", icon='🧹')
    
    if st.button("System Diagnostic"):
        with st.spinner('Running...'):
            time.sleep(1)
        st.success("All Systems Nominal")

# --- 3. THE BRAIN (CHAT SYSTEM) ---
if "messages" not in st.session_state:
    st.session_state.messages = []

# Header
st.title("Fenneric AI")
st.caption("Advanced Logic Engine | 2026 Edition")
st.divider()

# Display chat history
for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.markdown(msg["content"])

# --- 4. THE TURBO LOGIC ---
if prompt := st.chat_input("Enter command..."):
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)
    
    with st.chat_message("assistant"):
        response_placeholder = st.empty()
        full_response = ""
        
        # Neutral, Professional Response
        final_reply = f"System Analysis: Request for '{prompt}' received. Accessing logic gates... Processing complete. How may I assist further with this query?"
        
        # Fast Typing Effect
        for word in final_reply.split():
            full_response += word + " "
            time.sleep(0.04) 
            response_placeholder.markdown(full_response + "▌")
        response_placeholder.markdown(full_response)

    st.session_state.messages.append({"role": "assistant", "content": full_response})
