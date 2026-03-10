
import streamlit as st
import pandas as pd
import plotly.graph_objects as go
import plotly.express as px
from plotly.subplots import make_subplots
import numpy as np
from datetime import datetime
import base64
from io import BytesIO

# Page configuration
st.set_page_config(
    page_title="⛽ CRUDE OIL CHAOS | Ultimate Edition",
    page_icon="🛢️",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Try to import optional components
try:
    from streamlit_timeline import st_timeline
    TIMELINE_AVAILABLE = True
except ImportError:
    TIMELINE_AVAILABLE = False
    st.sidebar.warning("📦 Install streamlit-timeline for enhanced timeline: pip install streamlit-vis-timeline")

# Ultimate CSS with 3D effects and advanced animations
st.markdown("""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Orbitron:wght@400;700;900&family=Rajdhani:wght@300;500;700&family=Cinzel:wght@400;700&family=Syncopate:wght@400;700&display=swap');

    /* 3D Perspective container */
    .perspective-container {
        perspective: 1000px;
    }

    /* Floating 3D cards */
    .card-3d {
        transform-style: preserve-3d;
        transition: transform 0.6s cubic-bezier(0.23, 1, 0.32, 1);
    }

    .card-3d:hover {
        transform: rotateY(10deg) rotateX(5deg) translateZ(20px);
    }

    /* Animated mesh gradient background */
    @keyframes meshGradient {
        0% { background-position: 0% 0%; }
        50% { background-position: 100% 100%; }
        100% { background-position: 0% 0%; }
    }

    .mesh-bg {
        background: 
            radial-gradient(at 40% 20%, hsla(28,100%,74%,1) 0px, transparent 50%),
            radial-gradient(at 80% 0%, hsla(189,100%,56%,1) 0px, transparent 50%),
            radial-gradient(at 0% 50%, hsla(340,100%,76%,1) 0px, transparent 50%),
            radial-gradient(at 80% 50%, hsla(355,100%,93%,1) 0px, transparent 50%),
            radial-gradient(at 0% 100%, hsla(22,100%,77%,1) 0px, transparent 50%),
            radial-gradient(at 80% 100%, hsla(242,100%,70%,1) 0px, transparent 50%),
            radial-gradient(at 0% 0%, hsla(343,100%,76%,1) 0px, transparent 50%);
        background-size: 200% 200%;
        animation: meshGradient 20s ease infinite;
    }

    /* Holographic effect */
    .holographic {
        background: linear-gradient(
            135deg,
            rgba(255,255,255,0.1) 0%,
            rgba(255,255,255,0.05) 50%,
            rgba(255,255,255,0.1) 100%
        );
        backdrop-filter: blur(20px);
        border: 1px solid rgba(255,255,255,0.2);
        box-shadow: 
            0 8px 32px rgba(0,0,0,0.3),
            inset 0 0 20px rgba(255,255,255,0.1);
    }

    /* Neon flicker animation */
    @keyframes flicker {
        0%, 100% { opacity: 1; text-shadow: 0 0 10px #ffd700, 0 0 20px #ffd700; }
        50% { opacity: 0.8; text-shadow: 0 0 5px #ffd700, 0 0 10px #ffd700; }
    }

    .neon-flicker {
        animation: flicker 3s infinite;
    }

    /* Typewriter effect */
    @keyframes typing {
        from { width: 0; }
        to { width: 100%; }
    }

    .typewriter {
        overflow: hidden;
        white-space: nowrap;
        animation: typing 3s steps(40, end);
    }

    /* Glowing border animation */
    @keyframes borderGlow {
        0%, 100% { border-color: rgba(255,215,0,0.3); box-shadow: 0 0 5px rgba(255,215,0,0.3); }
        50% { border-color: rgba(255,215,0,0.8); box-shadow: 0 0 20px rgba(255,215,0,0.6); }
    }

    .glow-border {
        animation: borderGlow 2s infinite;
    }

    /* Parallax layers */
    .parallax-layer {
        transform: translateZ(0);
        will-change: transform;
    }

    /* Liquid button effect */
    .liquid-btn {
        position: relative;
        overflow: hidden;
        z-index: 1;
    }

    .liquid-btn::before {
        content: '';
        position: absolute;
        top: 0;
        left: -100%;
        width: 100%;
        height: 100%;
        background: linear-gradient(90deg, transparent, rgba(255,255,255,0.4), transparent);
        transition: 0.5s;
        z-index: -1;
    }

    .liquid-btn:hover::before {
        left: 100%;
    }

    /* Data stream effect */
    @keyframes dataStream {
        0% { transform: translateY(-100%); opacity: 0; }
        50% { opacity: 1; }
        100% { transform: translateY(100%); opacity: 0; }
    }

    .data-particle {
        position: absolute;
        width: 2px;
        height: 10px;
        background: #ffd700;
        animation: dataStream 2s infinite;
    }
</style>
""", unsafe_allow_html=True)

# Data loading with enhanced metadata
@st.cache_data(ttl=3600)
def load_ultimate_data():
    """Ultimate oil price dataset with rich metadata"""
    data = [
        # EARLY OIL ERA (1861-1945)
        {"year": 1861, "price": 0.49, "adj": 12.65, "event": "First commercial oil well drilled in Pennsylvania", "category": "Early Oil Era", "type": "tech", "impact": 0, "severity": 1, "icon": "⛏️", "description": "Colonel Edwin Drake strikes oil at 69 feet, launching the modern petroleum industry"},
        {"year": 1864, "price": 8.06, "adj": 119.56, "event": "Civil War PEAK - 19th century all-time high", "category": "Early Oil Era", "type": "war", "impact": 1, "severity": 5, "icon": "🔥", "description": "Union blockade and war demand cause prices to spike 1544% from 1861 levels"},
        {"year": 1892, "price": 0.56, "adj": 14.46, "event": "Century LOW - Standard Oil monopoly overproduction", "category": "Early Oil Era", "type": "economic", "impact": -1, "severity": 4, "icon": "❄️", "description": "Rockefeller's monopoly drives prices to lowest point of the century through vertical integration"},
        {"year": 1901, "price": 0.96, "adj": 26.77, "event": "Spindletop discovery - Texas oil boom begins", "category": "Early Oil Era", "type": "tech", "impact": 0, "severity": 3, "icon": "🌵", "description": "Lucas Gusher at Spindletop produces 100,000 barrels/day, creating the modern oil industry"},
        {"year": 1911, "price": 0.61, "adj": 15.19, "event": "Standard Oil broken up - Seven Sisters created", "category": "Early Oil Era", "type": "economic", "impact": -1, "severity": 3, "icon": "🔨", "description": "Supreme Court antitrust ruling creates Exxon, Mobil, Chevron, and other major oil companies"},
        {"year": 1918, "price": 1.98, "adj": 30.60, "event": "WWI peak demand - Industrial warfare", "category": "Early Oil Era", "type": "war", "impact": 1, "severity": 4, "icon": "⚔️", "description": "Tanks, trucks, and naval warfare create unprecedented demand for petroleum"},
        {"year": 1920, "price": 3.07, "adj": 35.68, "event": "Automobile boom - West Coast gas famine", "category": "Early Oil Era", "type": "economic", "impact": 1, "severity": 3, "icon": "🏎️", "description": "Rising car ownership creates first major gasoline shortage on US West Coast"},
        {"year": 1926, "price": 1.88, "adj": 24.73, "event": "Venezuela discovery - Global supply surge", "category": "Early Oil Era", "type": "tech", "impact": -1, "severity": 2, "icon": "🌎", "description": "Lake Maracaibo discoveries make Venezuela second-largest oil producer"},
        {"year": 1931, "price": 0.65, "adj": 9.94, "event": "Great Depression LOW - East Texas glut", "category": "Early Oil Era", "type": "economic", "impact": -1, "severity": 5, "icon": "📉", "description": "Economic collapse reduces demand while East Texas oil flood creates massive oversupply"},
        {"year": 1938, "price": 1.13, "adj": 18.67, "event": "Kuwait & Saudi Arabia discoveries", "category": "Early Oil Era", "type": "tech", "impact": 0, "severity": 3, "icon": "🕌", "description": "Dammam Well No. 7 in Saudi Arabia and Burgan field in Kuwait discovered, changing global oil geography"},
        {"year": 1944, "price": 1.21, "adj": 18.00, "event": "WWII peak - Aviation fuel demand", "category": "Early Oil Era", "type": "war", "impact": 1, "severity": 4, "icon": "🛩️", "description": "Allied war effort consumes 7 billion barrels; synthetic fuel production in Germany peaks"},

        # POST-WAR ERA (1946-1972)
        {"year": 1947, "price": 1.90, "adj": 19.80, "event": "Post-war industrial boom begins", "category": "Post-War Era", "type": "economic", "impact": 1, "severity": 2, "icon": "🏗️", "description": "Marshall Plan reconstruction drives European oil demand up 50% in two years"},
        {"year": 1956, "price": 2.80, "adj": 32.00, "event": "Suez Crisis - Canal nationalized", "category": "Post-War Era", "type": "geopolitical", "impact": 1, "severity": 4, "icon": "⚓", "description": "Nasser nationalizes Suez Canal; 5% of world oil trade disrupted for months"},
        {"year": 1960, "price": 1.90, "adj": 14.93, "event": "OPEC formed in Baghdad - Cartel begins", "category": "Post-War Era", "type": "geopolitical", "impact": 0, "severity": 3, "icon": "📜", "description": "Five founding members (Iran, Iraq, Kuwait, Saudi Arabia, Venezuela) create oil cartel"},
        {"year": 1970, "price": 1.80, "adj": 10.79, "event": "US production peaks - Texas quotas END", "category": "Post-War Era", "type": "economic", "impact": 0, "severity": 4, "icon": "🏔️", "description": "Hubbert's Peak realized; US oil production maxes at 10.04 million barrels/day, never to return"},
        {"year": 1971, "price": 2.24, "adj": 12.87, "event": "Nixon ends Bretton Woods - Dollar devalues", "category": "Post-War Era", "type": "economic", "impact": 1, "severity": 3, "icon": "💸", "description": "Gold standard abandonment leads to dollar devaluation and commodity price inflation"},

        # OIL CRISIS ERA (1973-1986)
        {"year": 1973, "price": 4.00, "adj": 28.00, "event": "Yom Kippur War - OAPEC EMBARGO begins", "category": "Oil Crisis Era", "type": "war", "impact": 1, "severity": 5, "icon": "⛽", "description": "Arabs cut oil exports 5 million barrels/day; prices quadruple; gas lines form across America"},
        {"year": 1974, "price": 11.58, "adj": 54.74, "event": "FIRST OIL SHOCK - Prices QUADRUPLE", "category": "Oil Crisis Era", "type": "war", "impact": 1, "severity": 5, "icon": "🚀", "description": "Oil prices rise from $3 to $12; global recession follows; inflation hits double digits"},
        {"year": 1979, "price": 31.61, "adj": 101.43, "event": "Iranian Revolution - Production HALVED", "category": "Oil Crisis Era", "type": "war", "impact": 1, "severity": 5, "icon": "🔥", "description": "Shah overthrown; Iranian output drops from 6M to 1.5M bpd; second oil shock begins"},
        {"year": 1980, "price": 36.83, "adj": 104.12, "event": "Iran-Iraq War - ALL-TIME NOMINAL HIGH", "category": "Oil Crisis Era", "type": "war", "impact": 1, "severity": 5, "icon": "💣", "description": "War destroys production in both countries; oil hits $36.83, record until 2008"},
        {"year": 1981, "price": 35.93, "adj": 92.08, "event": "Reagan ends controls - Volcker 20% rates", "category": "Oil Crisis Era", "type": "economic", "impact": -1, "severity": 4, "icon": "🏦", "description": "Reagan deregulates oil; Fed raises rates to 20%; oil demand destruction begins"},
        {"year": 1986, "price": 14.43, "adj": 30.67, "event": "OIL GLUT CRASH - Saudi market share war", "category": "Oil Crisis Era", "type": "economic", "impact": -1, "severity": 5, "icon": "🔻", "description": "Saudi Arabia floods market; prices collapse 46% in one year; oil patch recession"},

        # POST-COLD WAR (1989-2002)
        {"year": 1990, "price": 23.73, "adj": 55.00, "event": "Gulf War - Iraq invades Kuwait", "category": "Post-Cold War", "type": "war", "impact": 1, "severity": 5, "icon": "🎖️", "description": "Saddam Hussein captures Kuwait; 4.3M bpd removed; prices spike to $41"},
        {"year": 1991, "price": 20.00, "adj": 34.21, "event": "Desert Storm - Prices crash 33% in ONE DAY", "category": "Post-Cold War", "type": "war", "impact": -1, "severity": 4, "icon": "📉", "description": "Operation Desert Storm success; largest single-day price drop in history"},
        {"year": 1998, "price": 12.72, "adj": 18.17, "event": "20-YEAR LOW - Asian Financial Crisis", "category": "Post-Cold War", "type": "economic", "impact": -1, "severity": 4, "icon": "❄️", "description": "Asian economies collapse; Russian default; oil demand plummets; prices hit $10.82 intraday"},
        {"year": 2000, "price": 28.50, "adj": 38.55, "event": "Dot-com boom - Strong US demand", "category": "Post-Cold War", "type": "economic", "impact": 1, "severity": 2, "icon": "🌐", "description": "Economic expansion drives demand; OPEC maintains discipline; prices recover"},
        {"year": 2001, "price": 24.44, "adj": 32.15, "event": "9/11 attacks - Recession fears", "category": "Post-Cold War", "type": "war", "impact": -1, "severity": 3, "icon": "🗽", "description": "Terrorist attacks create demand uncertainty; aviation industry devastated"},

        # SUPERCYCLE ERA (2003-2014)
        {"year": 2003, "price": 28.00, "adj": 45.00, "event": "Iraq War - China demand SURGES", "category": "Supercycle Era", "type": "war", "impact": 1, "severity": 3, "icon": "🏭", "description": "US invasion of Iraq coincides with China's entry into WTO; demand explodes"},
        {"year": 2004, "price": 38.27, "adj": 47.19, "event": "China SUPERCYCLE begins", "category": "Supercycle Era", "type": "economic", "impact": 1, "severity": 4, "icon": "🐉", "description": "Chinese oil demand grows 15% annually; becomes world's second-largest consumer"},
        {"year": 2005, "price": 54.52, "adj": 65.03, "event": "Hurricane Katrina - Gulf destroyed", "category": "Supercycle Era", "type": "geopolitical", "impact": 1, "severity": 4, "icon": "🌪️", "description": "Category 5 hurricane destroys 113 oil platforms; 25% of US production offline"},
        {"year": 2008, "price": 147.27, "adj": 210.00, "event": "ALL-TIME HIGH - Speculation PEAK", "category": "Supercycle Era", "type": "economic", "impact": 1, "severity": 5, "icon": "💰", "description": "Financial speculation drives oil to $147.27; commodity index funds peak at $260B"},
        {"year": 2008.5, "price": 32.00, "adj": 45.00, "event": "Financial CRASH - -78% in 5 months", "category": "Supercycle Era", "type": "economic", "impact": -1, "severity": 5, "icon": "🏦", "description": "Lehman Brothers collapse; global recession; oil crashes from $147 to $32"},
        {"year": 2011, "price": 111.26, "adj": 115.22, "event": "Arab Spring - Libya offline", "category": "Supercycle Era", "type": "war", "impact": 1, "severity": 4, "icon": "🔥", "description": "Tunisia, Egypt, Libya uprisings; 1.6M Libyan barrels removed; fear premium returns"},
        {"year": 2014, "price": 114.84, "adj": 150.00, "event": "ISIS advances - Last peak before crash", "category": "Supercycle Era", "type": "war", "impact": 1, "severity": 3, "icon": "⚠️", "description": "Islamic State captures Iraqi oil fields; last major peak before shale revolution"},

        # SHALE ERA (2014-2026)
        {"year": 2014.8, "price": 80.00, "adj": 105.00, "event": "OPEC declares WAR on US shale", "category": "Shale Era", "type": "economic", "impact": -1, "severity": 4, "icon": "🛢️", "description": "Saudi Arabia refuses to cut production; aims to bankrupt US shale producers"},
        {"year": 2016, "price": 26.21, "adj": 34.00, "event": "Shale GLUT LOW - OPEC+ formed", "category": "Shale Era", "type": "economic", "impact": -1, "severity": 5, "icon": "🔻", "description": "OPEC+ alliance formed with Russia; prices bottom at $26; 100 shale bankruptcies"},
        {"year": 2018, "price": 76.00, "adj": 90.00, "event": "Iran sanctions - Venezuela COLLAPSE", "category": "Shale Era", "type": "geopolitical", "impact": 1, "severity": 4, "icon": "🚫", "description": "Trump exits Iran deal; Venezuela production collapses to 1M bpd; prices rise"},
        {"year": 2020, "price": -37.63, "adj": -46.00, "event": "BELOW ZERO - COVID-19 storage FULL", "category": "Shale Era", "type": "pandemic", "impact": -1, "severity": 5, "icon": "💀", "description": "COVID destroys demand; Cushing storage full; WTI goes NEGATIVE for first time in history"},
        {"year": 2021, "price": 70.00, "adj": 75.00, "event": "Post-COVID recovery - Supply shortages", "category": "Shale Era", "type": "pandemic", "impact": 1, "severity": 3, "icon": "💉", "description": "Vaccine rollout; demand rebounds faster than supply; OPEC+ gradual increases"},
        {"year": 2022, "price": 130.50, "adj": 148.00, "event": "Russia-Ukraine WAR - Sanctions", "category": "Shale Era", "type": "war", "impact": 1, "severity": 5, "icon": "⚡", "description": "Russia invades Ukraine; Western sanctions; Brent hits $139; energy crisis begins"},
        {"year": 2022.5, "price": 107.12, "adj": 116.61, "event": "SPR releases - China lockdowns", "category": "Shale Era", "type": "economic", "impact": -1, "severity": 2, "icon": "📦", "description": "US releases 180M barrels from SPR; China COVID lockdowns reduce demand"},
        {"year": 2024, "price": 80.00, "adj": 85.00, "event": "Red Sea attacks - Gaza conflict", "category": "Shale Era", "type": "war", "impact": 1, "severity": 3, "icon": "🎯", "description": "Houthis attack shipping; Gaza war creates Middle East tension; Houthi missile strikes"},
        {"year": 2025, "price": 70.00, "adj": 70.00, "event": "Trump tariffs - Oversupply concerns", "category": "Shale Era", "type": "economic", "impact": -1, "severity": 2, "icon": "🏛️", "description": "Trade war fears; OPEC+ maintains cuts; non-OPEC supply growth concerns"},
        {"year": 2026, "price": 71.13, "adj": 71.13, "event": "CURRENT - OPEC+ cuts uncertainty", "category": "Shale Era", "type": "geopolitical", "impact": 0, "severity": 1, "icon": "🎯", "description": "OPEC+ considers unwinding cuts; demand growth uncertainty; geopolitical tensions persist"}
    ]
    return pd.DataFrame(data)

df = load_ultimate_data()

# Sidebar with futuristic controls
st.sidebar.markdown("""
<div style='text-align:center; padding:20px 0;'>
    <h2 style='color:#ffd700; font-family:Orbitron; margin:0;'>🎛️</h2>
    <h3 style='color:#fff; font-family:Syncopate; margin:5px 0; font-size:0.9em;'>CONTROL CENTER</h3>
</div>
""", unsafe_allow_html=True)

st.sidebar.markdown("---")

# Era selection with visual icons
era_config = {
    "Early Oil Era": {"icon": "⛏️", "color": "#8B4513", "desc": "1861-1945"},
    "Post-War Era": {"icon": "🏭", "color": "#4682B4", "desc": "1946-1972"},
    "Oil Crisis Era": {"icon": "⛽", "color": "#FF4500", "desc": "1973-1986"},
    "Post-Cold War": {"icon": "🌍", "color": "#9370DB", "desc": "1989-2002"},
    "Supercycle Era": {"icon": "🚀", "color": "#FFD700", "desc": "2003-2014"},
    "Shale Era": {"icon": "🛢️", "color": "#32CD32", "desc": "2014-2026"}
}

selected_eras = st.sidebar.multiselect(
    "🎯 SELECT ERAS",
    options=list(era_config.keys()),
    default=list(era_config.keys()),
    format_func=lambda x: f"{era_config[x]['icon']} {x} ({era_config[x]['desc']})"
)

# Advanced controls
st.sidebar.markdown("### ⚙️ ADVANCED SETTINGS")

price_mode = st.sidebar.radio(
    "💰 PRICE MODE",
    ["Nominal ($)", "Inflation-Adjusted 2025 ($)"],
    index=1
)

viz_mode = st.sidebar.selectbox(
    "🔮 VISUALIZATION MODE",
    ["Chaos Timeline", "3D Price Mountain", "Crisis Intensity Map", "Era Battle Arena", "Volatility Storm"]
)

# Effects toggles
st.sidebar.markdown("### ✨ EFFECTS")
col1, col2 = st.sidebar.columns(2)
with col1:
    show_3d = st.toggle("3D Mode", value=True)
with col2:
    show_anim = st.toggle("Animations", value=True)

st.sidebar.markdown("---")

# Info box
st.sidebar.info("📊 **Dataset:** 51 major oil price events from 1861-2026")

# Main header with holographic effect
st.markdown("""
<div class='perspective-container'>
    <h1 class='neon-flicker' style='text-align:center; font-family:Syncopate; font-size:3em; margin-bottom:10px; text-transform:uppercase;'>
        ⛽ CRUDE OIL CHAOS
    </h1>
    <p class='typewriter' style='text-align:center; color:#4ecdc4; font-family:Rajdhani; font-size:1.4em; letter-spacing:3px; margin-top:0;'>
        165 YEARS OF PRICE WARS, CRISES & GEOPOLITICAL MAYHEM
    </p>
</div>
""", unsafe_allow_html=True)

# Filter data
filtered_df = df[df['category'].isin(selected_eras)].copy()
price_col = 'adj' if price_mode == "Inflation-Adjusted 2025 ($)" else 'price'

# Key metrics with 3D cards
st.markdown("---")
metric_cols = st.columns(5)
metrics_data = [
    ("📈 PEAK", "$147.27", "July 2008", "#ffd700", "All-time high"),
    ("📉 ABYSS", "-$37.63", "April 2020", "#ff6b6b", "Negative prices"),
    ("💰 NOW", "$71.13", "March 2026", "#4ecdc4", "Current"),
    ("📊 SWING", "±492%", "Max Range", "#a29bfe", "Volatility"),
    ("🌍 EVENTS", str(len(filtered_df)), "Recorded", "#fd79a8", "Total")
]

for i, (label, value, sub, color, desc) in enumerate(metrics_data):
    with metric_cols[i]:
        st.markdown(f"""
        <div class='card-3d holographic glow-border' style='padding:20px; text-align:center; border-radius:15px;'>
            <h4 style='margin:0; color:{color}; font-family:Orbitron; font-size:0.9em;'>{label}</h4>
            <h2 style='margin:10px 0; color:#fff; font-family:Orbitron; font-size:2em; text-shadow:0 0 10px {color};'>{value}</h2>
            <small style='color:#888;'>{sub}</small>
            <div style='margin-top:10px; padding:5px; background:rgba(255,255,255,0.1); border-radius:5px;'>
                <small style='color:{color};'>{desc}</small>
            </div>
        </div>
        """, unsafe_allow_html=True)

st.markdown("---")

# Main visualization based on mode
if viz_mode == "Chaos Timeline":
    st.markdown("<h2 style='text-align:center; font-family:Orbitron; color:#ffd700;'>🕰️ THE CHAOS TIMELINE</h2>", unsafe_allow_html=True)

    # Create enhanced timeline with streamlit-timeline if available
    if TIMELINE_AVAILABLE and show_3d:
        # Prepare timeline items
        timeline_items = []
        for _, row in filtered_df.iterrows():
            year_int = int(row['year'])
            content = f"{row['icon']} {row['event'][:30]}..."
            timeline_items.append({
                "id": str(row['year']),
                "content": content,
                "start": f"{year_int}-01-01",
                "type": "point",
                "className": f"era-{row['category'].replace(' ', '-').lower()}"
            })

        timeline = st_timeline(timeline_items, groups=[], options={"height": "400px"}, height="400px")
        if timeline:
            st.write(f"Selected: {timeline}")

    # Create main scatter plot
    fig = go.Figure()

    # Color mapping
    type_colors = {'war': '#ff6b6b', 'economic': '#4ecdc4', 'geopolitical': '#ffd700', 'tech': '#a29bfe', 'pandemic': '#fd79a8'}

    # Add traces by type
    for etype in type_colors.keys():
        mask = filtered_df['type'] == etype
        if mask.any():
            subset = filtered_df[mask]
            fig.add_trace(go.Scatter(
                x=subset['year'],
                y=subset[price_col],
                mode='markers+text',
                name=f"{etype.upper()} ({len(subset)} events)",
                marker=dict(
                    size=subset['severity'] * 6,
                    color=type_colors[etype],
                    line=dict(color='white', width=2),
                    symbol='diamond',
                    opacity=0.9
                ),
                text=subset['icon'],
                textposition="middle center",
                textfont=dict(size=14),
                hovertemplate='<b>%{x}</b><br>Price: $%{y:.2f}<br>%{customdata[0]}<extra></extra>',
                customdata=subset[['event']].values
            ))

    # Add connecting spline
    sorted_df = filtered_df.sort_values('year')
    fig.add_trace(go.Scatter(
        x=sorted_df['year'],
        y=sorted_df[price_col],
        mode='lines',
        line=dict(color='rgba(255,215,0,0.4)', width=3, shape='spline'),
        hoverinfo='skip',
        showlegend=False
    ))

    fig.update_layout(
        template='plotly_dark',
        paper_bgcolor='rgba(0,0,0,0)',
        plot_bgcolor='rgba(0,0,0,0.3)',
        height=600,
        showlegend=True,
        legend=dict(orientation="h", yanchor="bottom", y=1.02, xanchor="right", x=1),
        xaxis=dict(title="Year", gridcolor='rgba(255,255,255,0.1)', rangeslider=dict(visible=True)),
        yaxis=dict(title="Price (USD)", gridcolor='rgba(255,255,255,0.1)', zerolinecolor='#ff6b6b')
    )

    st.plotly_chart(fig, use_container_width=True)

elif viz_mode == "3D Price Mountain":
    st.markdown("<h2 style='text-align:center; font-family:Orbitron; color:#ffd700;'>🏔️ 3D PRICE MOUNTAIN</h2>", unsafe_allow_html=True)

    # Create 3D surface visualization
    sorted_df = filtered_df.sort_values('year')

    # Create mesh grid for 3D effect
    years = sorted_df['year'].values
    prices = sorted_df[price_col].values

    # Create 3D scatter with size based on severity
    fig = go.Figure(data=[go.Scatter3d(
        x=years,
        y=[0] * len(years),
        z=prices,
        mode='markers+lines',
        marker=dict(
            size=sorted_df['severity'] * 3,
            color=prices,
            colorscale='Viridis',
            opacity=0.8,
            line=dict(color='white', width=2)
        ),
        line=dict(color='rgba(255,215,0,0.5)', width=4),
        hovertemplate='Year: %{x}<br>Price: $%{z:.2f}<extra></extra>'
    )])

    fig.update_layout(
        template='plotly_dark',
        paper_bgcolor='rgba(0,0,0,0)',
        scene=dict(
            xaxis=dict(title='Year', gridcolor='rgba(255,255,255,0.1)'),
            yaxis=dict(title='', showticklabels=False, showgrid=False),
            zaxis=dict(title='Price ($)', gridcolor='rgba(255,255,255,0.1)'),
            bgcolor='rgba(0,0,0,0.3)'
        ),
        height=700,
        margin=dict(l=0, r=0, b=0, t=30)
    )

    st.plotly_chart(fig, use_container_width=True)

elif viz_mode == "Crisis Intensity Map":
    st.markdown("<h2 style='text-align:center; font-family:Orbitron; color:#ffd700;'>🔥 CRISIS INTENSITY HEATMAP</h2>", unsafe_allow_html=True)

    # Calculate volatility
    sorted_df = filtered_df.sort_values('year')
    sorted_df['change'] = sorted_df[price_col].pct_change() * 100
    sorted_df['abs_change'] = abs(sorted_df['change'])

    # Create animated heatmap
    fig = go.Figure()

    # Add heatmap
    fig.add_trace(go.Heatmap(
        z=[sorted_df['abs_change'].fillna(0).values],
        x=sorted_df['year'].values,
        y=['Volatility'],
        colorscale=[
            [0, 'rgba(78,205,196,0.2)'],
            [0.3, 'rgba(255,215,0,0.5)'],
            [0.7, 'rgba(255,107,107,0.8)'],
            [1, 'rgba(255,0,0,1)']
        ],
        showscale=True,
        hovertemplate='Year: %{x}<br>Change: %{z:.1f}%<extra></extra>'
    ))

    fig.update_layout(
        template='plotly_dark',
        paper_bgcolor='rgba(0,0,0,0)',
        height=400,
        xaxis=dict(title="Year"),
        yaxis=dict(showticklabels=False)
    )

    st.plotly_chart(fig, use_container_width=True)

    # Show top volatile events
    st.markdown("<h3 style='color:#ffd700; font-family:Orbitron;'>⚡ EXTREME VOLATILITY EVENTS</h3>", unsafe_allow_html=True)
    top_volatile = sorted_df.nlargest(5, 'abs_change')[['year', 'change', 'event', 'icon']]

    vol_cols = st.columns(5)
    for i, (_, row) in enumerate(top_volatile.iterrows()):
        with vol_cols[i]:
            color = '#ff6b6b' if row['change'] > 0 else '#4ecdc4'
            st.markdown(f"""
            <div class='holographic' style='padding:15px; border-radius:10px; text-align:center; border-left:5px solid {color};'>
                <h2 style='margin:0; color:{color}; font-size:2em;'>{row['icon']}</h2>
                <h4 style='margin:5px 0; color:#fff;'>{int(row['year'])}</h4>
                <h3 style='margin:5px 0; color:{color};'>{row['change']:+.1f}%</h3>
                <small style='color:#888; font-size:0.7em;'>{row['event'][:25]}...</small>
            </div>
            """, unsafe_allow_html=True)

elif viz_mode == "Era Battle Arena":
    st.markdown("<h2 style='text-align:center; font-family:Orbitron; color:#ffd700;'>⚔️ ERA BATTLE ARENA</h2>", unsafe_allow_html=True)

    # Calculate era statistics
    era_stats = filtered_df.groupby('category').agg({
        'price': ['min', 'max', 'mean', 'std'],
        'severity': 'mean',
        'year': ['min', 'max', 'count']
    }).round(2)

    era_stats.columns = ['Min', 'Max', 'Avg', 'Volatility', 'Avg Severity', 'Start', 'End', 'Events']
    era_stats['Duration'] = era_stats['End'] - era_stats['Start']
    era_stats['Power Score'] = (era_stats['Avg Severity'] * era_stats['Volatility'] / 10).round(1)

    # Create radar chart
    categories = ['Avg Price', 'Max Price', 'Volatility', 'Duration', 'Events', 'Severity']

    fig = go.Figure()
    colors = ['#ff6b6b', '#4ecdc4', '#ffd700', '#a29bfe', '#fd79a8', '#55efc4']

    for i, era in enumerate(era_stats.index):
        values = [
            era_stats.loc[era, 'Avg'] / 50,
            era_stats.loc[era, 'Max'] / 100,
            era_stats.loc[era, 'Volatility'] / 20,
            era_stats.loc[era, 'Duration'] / 50,
            era_stats.loc[era, 'Events'] / 10,
            era_stats.loc[era, 'Avg Severity']
        ]
        values += values[:1]

        fig.add_trace(go.Scatterpolar(
            r=values,
            theta=categories + [categories[0]],
            fill='toself',
            name=f"{era} (Power: {era_stats.loc[era, 'Power Score']})",
            line_color=colors[i % len(colors)],
            fillcolor=f'rgba{tuple(list(int(colors[i % len(colors)].lstrip("#")[j:j+2], 16) for j in (0, 2, 4)) + [0.2])}'
        ))

    fig.update_layout(
        polar=dict(radialaxis=dict(visible=True, range=[0, 5], gridcolor='rgba(255,255,255,0.2)'), bgcolor='rgba(0,0,0,0.3)'),
        template='plotly_dark',
        paper_bgcolor='rgba(0,0,0,0)',
        showlegend=True,
        height=600,
        legend=dict(orientation="h", yanchor="bottom", y=-0.2)
    )

    st.plotly_chart(fig, use_container_width=True)

    # Era ranking table
    st.markdown("<h3 style='color:#ffd700;'>🏆 ERA POWER RANKINGS</h3>", unsafe_allow_html=True)
    ranking_df = era_stats[['Power Score', 'Avg Severity', 'Volatility', 'Events']].sort_values('Power Score', ascending=False)
    st.dataframe(ranking_df.style.highlight_max(color='#ffd700', axis=0).highlight_min(color='#ff6b6b', axis=0))

elif viz_mode == "Volatility Storm":
    st.markdown("<h2 style='text-align:center; font-family:Orbitron; color:#ffd700;'>🌪️ VOLATILITY STORM</h2>", unsafe_allow_html=True)

    # Create violin plot of price distributions by era
    fig = go.Figure()

    for era in filtered_df['category'].unique():
        era_data = filtered_df[filtered_df['category'] == era][price_col]
        fig.add_trace(go.Violin(
            x=[era] * len(era_data),
            y=era_data,
            name=era,
            box_visible=True,
            line_color=era_config.get(era, {}).get('color', '#fff'),
            fillcolor=f'rgba{tuple(list(int(era_config.get(era, {}).get("color", "#fff").lstrip("#")[j:j+2], 16) for j in (0, 2, 4)) + [0.3])}',
            meanline_visible=True
        ))

    fig.update_layout(
        template='plotly_dark',
        paper_bgcolor='rgba(0,0,0,0)',
        plot_bgcolor='rgba(0,0,0,0.3)',
        height=500,
        xaxis=dict(title="Era"),
        yaxis=dict(title="Price Distribution ($)", zerolinecolor='#ff6b6b'),
        violinmode='group'
    )

    st.plotly_chart(fig, use_container_width=True)

# Legendary Crisis Cards Section
st.markdown("---")
st.markdown("<h2 style='text-align:center; font-family:Orbitron; color:#ffd700;'>🎴 LEGENDARY CRISIS CARDS</h2>", unsafe_allow_html=True)

# Define the 6 legendary crises
legendary_crises = [
    {"year": 1864, "title": "⚔️ CIVIL WAR PEAK", "price": "$8.06", "adj": "$119.56", "change": "+1544%", 
     "desc": "The American Civil War created unprecedented demand for lamp oil. Prices hit the highest point of the entire 19th century.",
     "fact": "First oil war in history", "color": "#ff6b6b", "severity": 5},
    {"year": 1973, "title": "🌍 THE FIRST SHOCK", "price": "$11.58", "adj": "$54.74", "change": "+289%",
     "desc": "Yom Kippur War triggers OAPEC embargo. Gas lines form across America. The era of cheap oil ends forever.",
     "fact": "Birth of OPEC power", "color": "#ff6b6b", "severity": 5},
    {"year": 1979, "title": "☪️ IRANIAN REVOLUTION", "price": "$31.61", "adj": "$101.43", "change": "+173%",
     "desc": "The Shah falls. Iranian production halts. Second oil crisis begins. Inflation-adjusted price exceeds $100.",
     "fact": "Islamic Revolution impact", "color": "#ff6b6b", "severity": 5},
    {"year": 1990, "title": "🇮🇶 GULF WAR", "price": "$41.00", "adj": "$95.00", "change": "+141%",
     "desc": "Iraq invades Kuwait. 4.3M barrels/day removed. Largest single-day price jump in history at the time.",
     "fact": "Desert Storm prelude", "color": "#ff6b6b", "severity": 4},
    {"year": 2008, "title": "📈 THE SUPERCYCLE", "price": "$147.27", "adj": "$210.00", "change": "All-time high",
     "desc": "China's insatiable demand + financial speculation drives oil to its highest price ever. Then crashes to $32.",
     "fact": "Commodity supercycle peak", "color": "#ffd700", "severity": 5},
    {"year": 2020, "title": "🦠 THE IMPOSSIBLE", "price": "-$37.63", "adj": "-$46.00", "change": "-128%",
     "desc": "COVID-19 destroys demand. Storage fills completely. Traders PAY to get rid of oil. First negative price in history.",
     "fact": "Negative oil prices!", "color": "#fd79a8", "severity": 5}
]

# Display cards in 3 columns
card_cols = st.columns(3)
for i, crisis in enumerate(legendary_crises):
    with card_cols[i % 3]:
        st.markdown(f"""
        <div class='card-3d holographic' style='padding:20px; border-radius:20px; margin:10px 0; border:2px solid {crisis['color']};'>
            <div style='display:flex; justify-content:space-between; align-items:center;'>
                <span style='background:{crisis['color']}; color:white; padding:5px 15px; border-radius:20px; font-size:0.8em; font-weight:bold;'>{crisis['year']}</span>
                <span style='color:{crisis['color']}; font-size:1.5em;'>{'★' * crisis['severity']}</span>
            </div>
            <h3 style='color:{crisis['color']}; margin:15px 0; font-family:Orbitron; font-size:1.1em;'>{crisis['title']}</h3>
            <div style='display:flex; justify-content:space-between; align-items:center; margin:15px 0; padding:10px; background:rgba(0,0,0,0.3); border-radius:10px;'>
                <div>
                    <h2 style='color:#fff; margin:0; font-size:1.8em;'>{crisis['price']}</h2>
                    <small style='color:#888;'>({crisis['adj']} adj)</small>
                </div>
                <div style='text-align:right;'>
                    <span style='color:{crisis['color']}; font-weight:bold; font-size:1.3em;'>{crisis['change']}</span>
                </div>
            </div>
            <p style='color:#ccc; font-size:0.9em; line-height:1.5;'>{crisis['desc']}</p>
            <div style='margin-top:15px; padding:10px; background:linear-gradient(90deg, {crisis['color']}20, transparent); border-left:3px solid {crisis['color']}; border-radius:0 5px 5px 0;'>
                <small style='color:{crisis['color']};'>💡 {crisis['fact']}</small>
            </div>
        </div>
        """, unsafe_allow_html=True)

# Data Explorer Section
st.markdown("---")
st.markdown("<h2 style='text-align:center; font-family:Orbitron; color:#ffd700;'>🔍 DATA EXPLORER</h2>", unsafe_allow_html=True)

with st.expander("📊 View Complete Dataset"):
    # Search functionality
    search_term = st.text_input("🔎 Search events", "")

    if search_term:
        search_results = filtered_df[filtered_df['event'].str.contains(search_term, case=False, na=False)]
        st.write(f"Found {len(search_results)} matching events:")
        display_df = search_results[['year', 'price', 'adj', 'event', 'category', 'type', 'description']]
    else:
        display_df = filtered_df[['year', 'price', 'adj', 'event', 'category', 'type', 'description']]

    display_df.columns = ['Year', 'Nominal', 'Inflation Adj.', 'Event', 'Era', 'Type', 'Details']

    # Styled dataframe
    st.dataframe(
        display_df.style.apply(lambda x: ['background: rgba(255,215,0,0.2)' if x['Nominal'] == filtered_df['price'].max() 
                                        else 'background: rgba(255,107,107,0.2)' if x['Nominal'] == filtered_df['price'].min() 
                                        else '' for _ in x], axis=1),
        use_container_width=True,
        height=400
    )

# Export Section
st.markdown("---")
st.markdown("<h2 style='text-align:center; font-family:Orbitron; color:#ffd700;'>💾 EXPORT THE CHAOS</h2>", unsafe_allow_html=True)

export_cols = st.columns(4)

with export_cols[0]:
    csv = filtered_df.to_csv(index=False)
    st.download_button("📄 CSV", csv, "oil_chaos_ultimate.csv", "text/csv")

with export_cols[1]:
    json_str = filtered_df.to_json(orient='records', indent=2)
    st.download_button("📋 JSON", json_str, "oil_chaos_ultimate.json", "application/json")

with export_cols[2]:
    buffer = BytesIO()
    with pd.ExcelWriter(buffer, engine='openpyxl') as writer:
        filtered_df.to_excel(writer, sheet_name='Oil Chaos', index=False)
    st.download_button("📊 EXCEL", buffer.getvalue(), "oil_chaos_ultimate.xlsx", 
                       "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet")

with export_cols[3]:
    if st.button("🔄 REFRESH DATA"):
        st.cache_data.clear()
        st.rerun()

# Ultimate Easter Egg
st.markdown("---")
col1, col2, col3 = st.columns([1, 2, 1])
with col2:
    if st.checkbox("🎮 ACTIVATE CHAOS PROTOCOL", key="ultimate"):
        st.balloons()
        st.snow()
        st.markdown("""
        <div style='background:linear-gradient(45deg, #ff6b6b, #4ecdc4, #ffd700, #a29bfe); padding:40px; border-radius:30px; text-align:center; animation:pulse 1s infinite;'>
            <h1 style='color:white; font-family:Syncopate; margin:0; font-size:2.5em; text-shadow:0 0 20px rgba(0,0,0,0.5);'>🎉 CHAOS PROTOCOL ACTIVATED 🎉</h1>
            <p style='color:white; font-size:1.3em; font-family:Rajdhani; margin:20px 0;'>
                <b>THE TRUTH REVEALED:</b><br>
                Oil is not just a commodity.<br>
                It is the lifeblood of civilization.<br>
                Its price is the heartbeat of human conflict.<br>
                Every spike is a war.<br>
                Every crash is a recession.<br>
                Every bubble is human greed.<br>
                <b>Welcome to the Chaos.</b>
            </p>
            <div style='font-size:3em; margin-top:20px;'>⛽🔥💀🚀💰⚔️🌍🦠</div>
        </div>
        """, unsafe_allow_html=True)
        st.audio("https://www.soundjay.com/misc/sounds/bell-ringing-05.wav", format="audio/wav")

# Footer
st.markdown("---")
st.markdown("""
<div style='text-align:center; padding:20px;'>
    <p style='color:#666; font-family:Rajdhani; font-size:0.9em;'>
        <b>DATA SOURCES:</b> BP Statistical Review • EIA • World Bank • OPEC • FRED • IEA | 
        <b>FRAMEWORK:</b> Streamlit + Plotly | 
        <b>DESIGN:</b> Chaos Theory Applied
    </p>
    <p style='color:#444; font-size:0.8em; font-style:italic;'>
        "In the midst of chaos, there is also opportunity" - Sun Tzu 🎋
    </p>
</div>
""", unsafe_allow_html=True)