import streamlit as st
import time
from PIL import Image
import pandas as pd
import plotly.graph_objects as go

# 1. Page Configuration & Professional Cyber Theme
st.set_page_config(page_title="HaitiAidShield Protocol | Cyber Command", layout="wide", page_icon="🛡️")

st.markdown("""
    <style>
    .stApp { background-color: #0d1117; color: #e6edf3; }
    section[data-testid="stSidebar"] { background-color: #161b22 !important; border-right: 1px solid #30363d; }
    div[data-testid="stMetric"] {
        background-color: #161b22 !important;
        border: 1px solid #30363d !important;
        border-radius: 12px;
        padding: 15px;
    }
    h1, h2, h3, h4, h5 { color: #58a6ff !important; }
    .stButton>button {
        background-color: #238636 !important;
        color: white !important;
        border-radius: 8px !important;
        width: 100%;
        font-weight: bold;
    }
    a { color: #58a6ff !important; text-decoration: none; }
    </style>
    """, unsafe_allow_html=True)

# 2. Sidebar: Protocol Verification (Section 4.1 Alignment)
with st.sidebar:
    st.image("https://img.icons8.com/fluency/96/shield.png", width=70)
    st.title("HaitiAidShield Protocol")
    st.caption("v1.0.2 - Production MVP")
    st.success("AI Sentry Node: ONLINE")
    st.info("Network: Polygon Amoy PoS")
    
    contract_address = "0x8Ede7cAe36Be72F038Dea11F96D25826e8bFe410"
    polygonscan_url = f"https://amoy.polygonscan.com/address/{contract_address}"
    st.markdown(f"**Immutable Smart Contract:**")
    st.markdown(f"[{contract_address}]({polygonscan_url})")
    
    st.divider()
    demo_mode = st.radio("Active Forensic Scenario:", ["Fraudulent (Ghost Project)", "Legitimate (Verified)"])
    
    st.divider()
    st.write("**Security Frameworks (NIST/Security+):**")
    st.write("✅ Frequency Domain Analysis")
    st.write("✅ Temporal Graph Audit")
    st.write("✅ Asynchronous State-Sync")

# 3. Main Dashboard Header
st.title("🛡️ Institutional Accountability Dashboard")
st.markdown("##### *A Decentralized AI-Augmented Anti-Corruption Hub for Humanitarian Resilience*")

# 4. Top Row: Key Metrics (Section 4.3 Alignment)
m1, m2, m3, m4 = st.columns(4)
m1.metric("Aid Volume Protected", "$1.24M", "+14%")
m2.metric("Verification Latency", "3.8s", "Real-time")
m3.metric("Validator Nodes", "12 Active", "Syncing")
m4.metric("Consensus Board", "3-of-5", "Multi-Sig Active")

st.write("---")

col1, col2, col3 = st.columns([1, 1, 1.2])

# --- COLUMN 1: EVIDENCE SUBMISSION (Section 6.3 Alignment) ---
with col1:
    st.header("📁 Evidence Ingestion")
    uploaded_file = st.file_uploader("Upload 'Proof of Work' Project Photo", type=['jpg', 'jpeg', 'png'])
    
    if uploaded_file:
        st.image(Image.open(uploaded_file), use_container_width=True)
        st.subheader("📍 Geospatial Oracle View")
        st.map(pd.DataFrame({'lat': [18.5333], 'lon': [-72.3333]}), zoom=12)
    else:
        st.info("Awaiting metadata-rich evidence for forensic processing.")

# --- COLUMN 2: AI RISK GAUGE & TRUST TRIANGLE (Section 4.2 Alignment) ---
with col2:
    st.header("📊 Forensic Risk Analysis")
    
    if uploaded_file:
        score = 99 if demo_mode == "Fraudulent (Ghost Project)" else 4
        fig = go.Figure(go.Indicator(
            mode = "gauge+number",
            value = score,
            domain = {'x': [0, 1], 'y': [0, 1]},
            title = {'text': "Sentry Risk Score (%)", 'font': {'color': "white"}},
            gauge = {
                'axis': {'range': [None, 100], 'tickcolor': "white"},
                'bar': {'color': "#f85149" if score > 50 else "#238636"},
                'bgcolor': "#161b22",
                'steps': [
                    {'range': [0, 50], 'color': "#30363d"},
                    {'range': [50, 80], 'color': "#d29922"},
                    {'range': [80, 100], 'color': "#f85149"}],
            }
        ))
        fig.update_layout(paper_bgcolor='rgba(0,0,0,0)', plot_bgcolor='rgba(0,0,0,0)', 
                          height=280, margin=dict(l=20, r=20, t=50, b=20), font={'color': "white"})
        st.plotly_chart(fig, use_container_width=True)
    
    st.write("---")
    st.subheader("👥 Trust Triangle (3-of-5 Multi-Sig)")
    st.write("Governance Threshold: **60% Quorum Required**")
    
    # Updated labels to match Paper Section 4.2
    t1, t2, t3 = st.columns(3)
    t4, t5 = st.columns(2)
    participants = [("🌍 Donor (ID)", t1), ("🏥 NGO (LIP)", t2), ("🛡️ Auditor (TA)", t3), ("🤝 Local (CL)", t4), ("🤖 Sentry (AS)", t5)]
    
    for label, col in participants:
        status = "🟥" if (uploaded_file and demo_mode == "Fraudulent (Ghost Project)") else "⬜"
        col.markdown(f"{status} {label}")

# --- COLUMN 3: HUMAN-IN-THE-LOOP ACTION CENTER (Section 5.3 Alignment) ---
with col3:
    st.header("⛓️ Action Center")
    
    # STEP 1: FORENSIC SCAN
    if st.button('🚀 Execute Forensic Analysis'):
        if not uploaded_file:
            st.warning("Action Required: Upload ingestion file.")
        else:
            with st.status("Analyzing Cryptographic Markers...", expanded=False):
                time.sleep(1); st.write("Scanning Frequency Domain for GAN Artifacts...")
                time.sleep(1); st.write("Cross-referencing Satellite Oracle Data...")
            
            if demo_mode == "Fraudulent (Ghost Project)":
                st.error("### 🚨 PROTOCOL VETO: FRAUD DETECTED")
                st.write("**AI Verdict:** Temporal Graph Analysis suggests Sybil behavior. GAN-noise detected in high-frequency pixel spectrum.")
                st.session_state['vetted'] = False
            else:
                st.success("### ✅ AUTHENTICITY CONFIRMED")
                st.write("**AI Verdict:** EXIF Integrity verified. Metadata and lighting vectors consistent with current atmospheric conditions.")
                st.session_state['vetted'] = True

    st.write("")
    
    # STEP 2: LEDGER COMMIT
    if st.button('⛓️ Commit Forensic Receipt to Ledger'):
        if 'vetted' not in st.session_state:
            st.warning("Step Required: Complete Sentry Analysis first.")
        else:
            with st.status("Broadcasting to Polygon Amoy...", expanded=False):
                time.sleep(1); st.write("Generating SHA-256 Audit Hash...")
            
            tx_hash = "0x7721b82fb8282e88a3b538392910"
            tx_url = f"https://amoy.polygonscan.com/tx/{tx_hash}"
            
            if st.session_state['vetted']:
                st.success("#### 🔓 DISBURSEMENT AUTHORIZED")
                st.markdown(f"🔗 **[View Forensic Receipt on Polygonscan]({tx_url})**")
            else:
                st.error("#### 🔒 DISBURSEMENT VETOED")
                st.markdown(f"🔗 **[View Veto Proof on Polygonscan]({tx_url})**")
            
            with st.expander("Technical Technical Audit Trail"):
                decision_state = st.session_state['vetted']
                st.code(f"""
[HASH] {tx_hash}
[AUTH] Multi-Sig Status: {'OPEN' if decision_state else 'BLOCKED'}
[AI] Decision: {'PASS' if decision_state else 'VETO'}
[META] Forensic Proof: {'VERIFIED' if decision_state else 'MALICIOUS_GAN'}
                """, language="bash")

                
                