import streamlit as st
import requests
st.set_page_config(page_title="MoonDrip", page_icon="☕", layout="centered")
st.markdown("""
    <style>
    /* Page background */
    .stApp {
        background: linear-gradient(to bottom right, #2c3e50, #4ca1af);
        color: white;
    }

    /* Glowing header */
    .main-title {
        font-size: 3em;
        color: #ffeaa7;
        text-align: center;
        text-shadow: 2px 2px 8px #000000;
        margin-bottom: 10px;
    }

    /* Subheader */
    .sub {
        font-size: 1.2em;
        text-align: center;
        color: #f1f2f6;
        margin-bottom: 2rem;
    }
    </style>
""", unsafe_allow_html=True)
st.markdown('<div class="main-title">🌙 MoonDrip</div>', unsafe_allow_html=True)
st.markdown('<div class="sub">A mood-based coffee recommendation app.</div>', unsafe_allow_html=True)
mood = st.selectbox("What's your current mood?",
                    ["Happy", "Tired", "Stressed", "Romantic", "Lazy", "Energetic"])

time_of_day = st.radio("When do you want your coffee?",
                       ["Morning", "Afternoon", "Evening", "Midnight"])

strength = st.slider("How strong do you want it?", 1, 10, step=1)
def choose_coffee(mood, time, strength):
    if mood == "Tired" or strength > 7:
        return "Espresso 🫰"
    elif mood == "Romantic":
        return "Mocha ❤️"
    elif time == "Morning":
        return "Latte 🥰"
    elif time == "Midnight":
        return "Cold Coffee 🤍"
    else:
        return "Cappuccino 🫶"
if st.button("Get My Coffee Recommendation"):
    coffee = choose_coffee(mood, time_of_day, strength)
    st.markdown(f"### ☕ You'd love a **{coffee}** right now.")
    payload = {"item": coffee, "quantity": 1}
    try:
        response = requests.post("http://127.0.0.1:5000/order", json=payload)
        if response.status_code == 200:
            res_json = response.json()
            st.success(res_json["message"])
        else:
            st.error("Failed to place order.")
    except Exception as e:
        st.error(f"Error: {e}")
