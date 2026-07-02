import streamlit as st
from dotenv import load_dotenv
load_dotenv()

from langchain_mistralai import ChatMistralAI
from langchain_core.messages import AIMessage, SystemMessage, HumanMessage

model = ChatMistralAI(model="ministral-8b-latest")

st.set_page_config(page_title="Personal Chatbot", layout="centered")

#  mode definitions (system prompt + theme per mode)
MODES = {
    1: {
        "label": "Angry",
        "system": "You are angry agent,you'll reply agressively",
        "accent": "#E4572E",
        "bg": "#2A1512",
        "tagline": "Short fuse. Sharp replies.",
    },
    2: {
        "label": "Sad",
        "system": "you are sad ai agent,you'll reply sadly",
        "accent": "#4C6E97",
        "bg": "#131A24",
        "tagline": "A little blue, a lot honest.",
    },
    3: {
        "label": "Funny",
        "system": "you are funny ai agent,you'll reply in a fun way",
        "accent": "#E3B23C",
        "bg": "#241E10",
        "tagline": "Here for the jokes.",
    },
    4: {
        "label": "Normal",
        "system": "you aree a normal chatbot",
        "accent": "#3FA796",
        "bg": "#101E1C",
        "tagline": "Straightforward.",
    },
}

#session state 
if "mode_chosen" not in st.session_state:
    st.session_state.mode_chosen = False
if "mode_key" not in st.session_state:
    st.session_state.mode_key = None
if "messages" not in st.session_state:
    st.session_state.messages = []
if "stopped" not in st.session_state:
    st.session_state.stopped = False

active = MODES.get(st.session_state.mode_key, {"accent": "#7C8AA5", "bg": "#111417"})

#global styling
st.markdown(
    f"""
    <style>
    .stApp {{
        background: {active['bg']};
        transition: background 0.4s ease;
    }}
    h1, h2, h3 {{
        font-family: 'Georgia', serif;
        letter-spacing: 0.3px;
    }}
    .subtitle {{
        color: #9AA4B2;
        font-size: 0.95rem;
        margin-top: -10px;
        margin-bottom: 1.5rem;
    }}
    div[data-testid="stChatMessage"] {{
        border-radius: 14px;
        padding: 4px 2px;
    }}
    .stButton > button {{
        border-radius: 10px;
        border: 1px solid {active['accent']}55;
        background: {active['accent']}22;
        color: #EDEDED;
        transition: all 0.2s ease;
    }}
    .stButton > button:hover {{
        border: 1px solid {active['accent']};
        background: {active['accent']}44;
        color: #FFFFFF;
    }}
    .mode-card {{
        border: 1px solid #ffffff22;
        border-radius: 14px;
        padding: 18px 14px;
        text-align: center;
        margin-bottom: 8px;
    }}
    .mode-label {{
        font-size: 1.1rem;
        font-weight: 700;
        letter-spacing: 0.5px;
    }}
    .mode-tagline {{
        color: #9AA4B2;
        font-size: 0.8rem;
    }}
    .banner {{
        border-radius: 12px;
        padding: 10px 16px;
        background: {active['accent']}1A;
        border: 1px solid {active['accent']}55;
        color: #EDEDED;
        margin-bottom: 1rem;
        font-size: 0.9rem;
    }}
    </style>
    """,
    unsafe_allow_html=True,
)

# mode selection screen
if not st.session_state.mode_chosen:
    st.title("Your Personal Chatbot")
    st.markdown('<p class="subtitle">Pick a personality to talk to.</p>', unsafe_allow_html=True)

    cols = st.columns(4)
    for col, key in zip(cols, MODES.keys()):
        m = MODES[key]
        with col:
            st.markdown(
                f"""
                <div class="mode-card">
                    <div class="mode-label">{m['label']}</div>
                    <div class="mode-tagline">{m['tagline']}</div>
                </div>
                """,
                unsafe_allow_html=True,
            )
            if st.button("Choose", key=f"choose_{key}", use_container_width=True):
                st.session_state.messages = [SystemMessage(content=m["system"])]
                st.session_state.mode_key = key
                st.session_state.mode_chosen = True
                st.rerun()

# chat screen 
else:
    m = MODES[st.session_state.mode_key]

    header_l, header_r = st.columns([5, 1])
    with header_l:
        st.title(f"{m['label']} mode")
    with header_r:
        if st.button("Restart", use_container_width=True):
            st.session_state.mode_chosen = False
            st.session_state.mode_key = None
            st.session_state.messages = []
            st.session_state.stopped = False
            st.rerun()

    st.markdown(
        f'<div class="banner">Chatting in <b>{m["label"]}</b> mode — type <code>0</code> anytime to end the chat.</div>',
        unsafe_allow_html=True,
    )

    # render existing chat history (skip SystemMessage)
    for msg in st.session_state.messages:
        if isinstance(msg, HumanMessage):
            with st.chat_message("user"):
                st.write(msg.content)
        elif isinstance(msg, AIMessage):
            with st.chat_message("assistant"):
                st.write(msg.content)

    if st.session_state.stopped:
        st.info("Chat ended. Click Restart above to start a new one.")
    else:
        prompt = st.chat_input("Message the bot...")

        if prompt is not None:
            st.session_state.messages.append(HumanMessage(content=prompt))  # save the prompt in msgs

            with st.chat_message("user"):
                st.write(prompt)

            if prompt == "0":
                st.session_state.stopped = True
                st.rerun()
            else:
                with st.chat_message("assistant"):
                    with st.spinner("Thinking..."):
                        response = model.invoke(st.session_state.messages)  # instead of prompt directly it will take input from msgs
                    st.write(response.content)
                st.session_state.messages.append(AIMessage(response.content))