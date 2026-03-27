import streamlit as st
import time

# --- 1. THE FOUNDATION ---
st.set_page_config(page_title="Fenneric AI | Founder", page_icon="🛡️", layout="wide")

# Custom CSS for that "Premium" look
st.markdown("""
    <style>
    .main { background-color: #f0f2f6; }
    .stButton>button { width: 100%; border-radius: 20px; border: 1px solid #4CAF50; }
    </style>
    """, unsafe_path=True)

# --- 2. THE SIDEBAR (YOUR COMMAND CENTER) ---
with st.sidebar:
    # This is your "Cute" Logo Mascot
    st.markdown("<h1 style='text-align: center;'>🤖</h1>", unsafe_path=True)
    st.title("Fenneric HQ")
    st.write("---")
    
    # Stats with Live Feeling
    st.metric(label="Channel Subs", value="167", delta="Road to 200")
    st.metric(label="Empire Status", value="Online", delta="Secured")
    
    st.write("---")
    st.markdown("### 🎯 Next Milestone")
    st.progress(83) # 83% progress to 200 subs
    st.caption("83% to the 200 Subs Special!")
    
    if st.button("✨ Boost Aura"):
        st.balloons()
        st.toast("Aura Level: MAXIMUM", icon='🔥')

# --- 3. THE BRAIN (CHAT SYSTEM) ---
if "messages" not in st.session_state:
    st.session_state.messages = []

# Header
st.title("🛡️ Fenneric AI")
st.markdown("##### *Founder Edition v2.1 | Powered by Turbo Engine*")
st.divider()

# Display chat history
for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.markdown(msg["content"])

# --- 4. THE TURBO LOGIC ---
if prompt := st.chat_input("Command the Empire..."):
    # User Message
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)
    
    # AI Response with Typing Animation
    with st.chat_message("assistant"):
        response_placeholder = st.empty()
        full_response = ""
        
        # Pinpoint Accuracy Response
        final_reply = f"Founder, your request for '{prompt}' has been analyzed. Logic check complete. The Fenneric Empire is currently at 167 subs and climbing. How else can I assist your growth today?"
        
        # Turbo Typing Effect
        for chunk in final_reply.split():
            full_response += chunk + " "
            time.sleep(0.06) # Perfect speed
            response_placeholder.markdown(full_response + "▌")
        response_placeholder.markdown(full_response)

    st.session_state.messages.append({"role": "assistant", "content": full_response})
