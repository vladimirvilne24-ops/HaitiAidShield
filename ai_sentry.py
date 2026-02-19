import time
from web3 import Web3
from PIL import Image

# 1. CONNECTIONS: Linking to the HaitiAidShield Contract
POLYGON_RPC = "https://rpc-amoy.polygon.technology"
w3 = Web3(Web3.HTTPProvider(POLYGON_RPC))
CONTRACT_ADDRESS = "0x8Ede7cAe36Be72F038Dea11F96D25826e8bFe410"

# 2. DASHBOARD LOGIC: Translating Code for Jo-Ann
def display_civic_alert(project_id, risk_score):
    """Generates the 'Parallel Civic Oversight' view for non-technical users."""
    print("\n" + "!"*60)
    print(" " * 12 + "📢 PARALLEL CIVIC OVERSIGHT ALERT 📢")
    print("!"*60)
    print(f" PROJECT:      {project_id}")
    print(f" AI RISK SCORE: {risk_score} / 1.0 (CRITICAL)")
    print(f" VIOLATION:     Fraudulent Documentation (2014 Metadata)")
    print("-" * 60)
    print(" PROTOCOL STATUS: [ LOCKED ] Funds held in Smart Contract.")
    print(" NEXT STEP:       Awaiting Civil Society (CSO) Audit Review.")
    print("!"*60 + "\n")

# 3. FORENSIC LOGIC: The Ghost Project Filter
def audit_construction_metadata(image_path):
    """Handshake AI: EXIF Metadata Integrity Check"""
    print(f"\n[AI FORENSICS] Analyzing Construction Proof: {image_path}")
    try:
        # Simulations of GPS and Timestamp extraction
        print(f"[ANALYSIS] Extracting EXIF Tag 34853 (GPS)...")
        print(f"[ERROR] Metadata Mismatch: Image captured in 2014, not 2026.")
        return 0.98  # High Risk Score
    except Exception:
        return 1.0

# 4. MONITORING LOGIC: Listening to the Blockchain
print("--- HaitiAidShield: Handshake AI Sentry Active ---")
print(f"Monitoring Ledger: {CONTRACT_ADDRESS}")

def run_sentry():
    while True:
        print("\n[SCANNING] Checking Block for AidRequested events...")
        # Simulating detection of a PetroCaribe-style Ghost Project
        project_name = "Hospital Site Alpha"
        risk_score = audit_construction_metadata("hospital_site_alpha.jpg")
        
        if risk_score > 0.80:
            print(f"[CRITICAL] Risk Score: {risk_score}")
            print("[ACTION] GHOST PROJECT DETECTED. Blocking Multi-Sig release.")
            
            # TRIGGER THE DASHBOARD VIEW FOR JO-ANN
            display_civic_alert(project_name, risk_score)
        
        time.sleep(5) # Scans every 5 seconds for a more active demo

if __name__ == "__main__":
    try:
        run_sentry()
    except KeyboardInterrupt:
        print("\n[SYSTEM] Sentry deactivating...")