import streamlit as st
import pandas as pd
import pickle

# =========================
# PAGE CONFIG
# =========================

st.set_page_config(
    page_title='IPL Predictor',
    page_icon='🏏',
    layout='centered'
)

# =========================
# CUSTOM CSS
# =========================

st.markdown("""
<style>

/* Main Container */
.main .block-container {
    max-width: 950px;
    padding-top: 1rem;
    padding-bottom: 1rem;
}

/* Background Image */
.stApp {
    background-image: url("https://images.unsplash.com/photo-1540747913346-19e32dc3e97e");
    background-size: cover;
    background-position: center;
    background-attachment: fixed;
}

/* Dark Overlay */
[data-testid="stAppViewContainer"] {
    background: rgba(0,0,0,0.55);
}

/* Title */
h1 {
    text-align: center;
    color: white;
    font-size: 38px;
    font-weight: bold;
    text-shadow: 2px 2px 8px black;
}

/* Subtitle */
h3 {
    text-align: center;
    color: white;
    text-shadow: 1px 1px 6px black;
}

/* Labels */
label {
    color: white !important;
    font-weight: bold;
    text-shadow: 1px 1px 5px black;
}

/* Selectbox */
.stSelectbox div[data-baseweb="select"] {
    background-color: rgba(255,255,255,0.92);
    border-radius: 12px;
    color: black;
}

/* Dropdown Text */
.stSelectbox * {
    color: black !important;
    font-weight: 500;
}

/* Reduce Dropdown Height */
div[data-baseweb="select"] {
    min-height: 45px !important;
}

/* Button */
.stButton button {
    background: linear-gradient(
        90deg,
        #F97316,
        #EA580C
    );
    color: white;
    border: none;
    border-radius: 12px;
    height: 52px;
    width: 100%;
    font-size: 18px;
    font-weight: bold;
}

/* Button Hover */
.stButton button:hover {
    background: linear-gradient(
        90deg,
        #EA580C,
        #C2410C
    );
}

/* Success Box */
.stSuccess {
    border-radius: 12px;
    font-size: 18px;
}

/* Info Box */
.stInfo {
    border-radius: 12px;
    font-size: 16px;
}

/* Hide Streamlit Header */
header {
    visibility: hidden;
}

</style>
""", unsafe_allow_html=True)

# =========================
# LOAD MODEL
# =========================

model = pickle.load(open('model.pkl', 'rb'))

le_team = pickle.load(open('le_team.pkl', 'rb'))
le_venue = pickle.load(open('le_venue.pkl', 'rb'))
le_decision = pickle.load(open('le_decision.pkl', 'rb'))
le_winner = pickle.load(open('le_winner.pkl', 'rb'))

# =========================
# TEAM LOGOS
# =========================

team_logos = {

    'Chennai Super Kings':
    'https://scores.iplt20.com/ipl/teamlogos/CSK.png',

    'Mumbai Indians':
    'https://scores.iplt20.com/ipl/teamlogos/MI.png',

    'Royal Challengers Bangalore':
    'https://scores.iplt20.com/ipl/teamlogos/RCB.png',

    'Royal Challengers Bengaluru':
    'https://scores.iplt20.com/ipl/teamlogos/RCB.png',

    'Kolkata Knight Riders':
    'https://scores.iplt20.com/ipl/teamlogos/KKR.png',

    'Sunrisers Hyderabad':
    'https://scores.iplt20.com/ipl/teamlogos/SRH.png',

    'Rajasthan Royals':
    'https://scores.iplt20.com/ipl/teamlogos/RR.png',

    'Delhi Capitals':
    'https://scores.iplt20.com/ipl/teamlogos/DC.png',

    'Punjab Kings':
    'https://scores.iplt20.com/ipl/teamlogos/PBKS.png',

    'Lucknow Super Giants':
    'https://scores.iplt20.com/ipl/teamlogos/LSG.png',

    'Gujarat Titans':
    'https://scores.iplt20.com/ipl/teamlogos/GT.png'
}

# =========================
# TITLE
# =========================

st.title("🏏 IPL Match Winner Predictor")

st.markdown("""
<h3>
Predict IPL Match Winners using Machine Learning
</h3>
""", unsafe_allow_html=True)

st.markdown("---")

# =========================
# TEAMS
# =========================

teams = [
    'Chennai Super Kings',
    'Mumbai Indians',
    'Gujarat Titans',
    'Royal Challengers Bengaluru',
    'Kolkata Knight Riders',
    'Sunrisers Hyderabad',
    'Rajasthan Royals',
    'Delhi Capitals',
    'Punjab Kings',
    'Lucknow Super Giants'
]

# =========================
# VENUES
# =========================

venues = [
    'MA Chidambaram Stadium',
    'Wankhede Stadium',
    'M Chinnaswamy Stadium',
    'Eden Gardens',
    'Narendra Modi Stadium',
    'Arun Jaitley Stadium',
    'Sawai Mansingh Stadium',
    'Rajiv Gandhi International Stadium',
    'Punjab Cricket Association Stadium',
    'Bharat Ratna Shri Atal Bihari Vajpayee Ekana Cricket Stadium, Lucknow'
]

# =========================
# TEAM SELECTION
# =========================

col1, col2, col3 = st.columns([2,1,2])

# TEAM 1
with col1:

    team1 = st.selectbox(
        'Select Team 1',
        teams
    )

# CENTER VS
with col2:

    st.markdown("""
    <h1 style='font-size:30px; margin-top:60px;'>
    VS
    </h1>
    """, unsafe_allow_html=True)

# TEAM 2
with col3:

    team2 = st.selectbox(
        'Select Team 2',
        [t for t in teams if t != team1]
    )

# =========================
# TEAM LOGOS
# =========================

logo1, mid, logo2 = st.columns([2,1,2])

with logo1:

    st.markdown(
        f"""
        <div style='text-align:center;'>
            <img src="{team_logos[team1]}" width="110">
        </div>
        """,
        unsafe_allow_html=True
    )

with mid:

    st.markdown("""
    <h1 style='font-size:26px; color:white; margin-top:25px;'>
    VS
    </h1>
    """, unsafe_allow_html=True)

with logo2:

    st.markdown(
        f"""
        <div style='text-align:center;'>
            <img src="{team_logos[team2]}" width="110">
        </div>
        """,
        unsafe_allow_html=True
    )

st.markdown("<br>", unsafe_allow_html=True)

# =========================
# OTHER INPUTS
# =========================

input1, input2, input3 = st.columns(3)

with input1:

    venue = st.selectbox(
        'Select Stadium',
        venues
    )

with input2:

    toss_winner = st.selectbox(
        'Toss Winner',
        [team1, team2]
    )

with input3:

    toss_decision = st.selectbox(
        'Toss Decision',
        ['bat', 'field']
    )

st.markdown("<br>", unsafe_allow_html=True)


# =========================
# PREDICTION
# ====================================

if st.button('🔮 Predict Winner'):

    # Encode Inputs
    t1 = le_team.transform([team1])[0]
    t2 = le_team.transform([team2])[0]
    v = le_venue.transform([venue])[0]
    tw = le_team.transform([toss_winner])[0]
    td = le_decision.transform([toss_decision])[0]

    # Predict probabilities
    proba = model.predict_proba([[t1, t2, v, tw, td]])[0]

    # Get probabilities for selected teams only
    team1_idx = le_winner.transform([team1])[0]
    team2_idx = le_winner.transform([team2])[0]

    team1_prob = proba[team1_idx]
    team2_prob = proba[team2_idx]

    # Choose winner
    if team1_prob > team2_prob:

        winner = team1
        confidence = round(team1_prob * 100, 1)

    else:

        winner = team2
        confidence = round(team2_prob * 100, 1)

    # ====================================
    # RESULT
    # ====================================

    st.success(f'🏆 Predicted Winner: {winner}')

    # Winner logo
    st.image(team_logos[winner], width=220)

    # Confidence
    st.subheader('Prediction Confidence')

    st.progress(float(confidence) / 100)

    st.info(f'Confidence: {confidence}%') 
