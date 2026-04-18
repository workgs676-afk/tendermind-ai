import streamlit as st
import time

# ------------------ CONFIG ------------------
st.set_page_config(page_title="TenderMind AI", layout="centered")

# ------------------ GLOBAL STYLE ------------------
st.markdown("""
<style>

/* BACKGROUND */
.stApp {
    background: linear-gradient(135deg, #ffffff 0%, #f5edff 100%);
    font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", sans-serif;
}

/* HERO */
.hero {
    text-align: center;
    margin-top: 40px;
    margin-bottom: 25px;
}

.hero h1 {
    font-size: 44px;
    font-weight: 900;
    color: #3b0764;
    margin-bottom: 10px;
}

.hero p {
    font-size: 16px;
    color: #555;
}

/* FILE UPLOADER */
div[data-testid="stFileUploader"] {
    background: white;
    padding: 25px;
    border-radius: 15px;
    border: 2px dashed #a855f7;
    width: 90%;
    max-width: 520px;
    margin: 20px auto;
    transition: 0.3s;
}

div[data-testid="stFileUploader"]:hover {
    border-color: #7e22ce;
    box-shadow: 0px 10px 25px rgba(168,85,247,0.2);
}

/* RESULT BOX */
.result-box {
    width: 90%;
    max-width: 520px;
    margin: 20px auto;
    background: white;
    padding: 20px;
    border-radius: 12px;
    box-shadow: 0px 5px 20px rgba(0,0,0,0.08);
}

/* FOOTER TEXT */
.footer-title {
    font-size: 22px;
    font-weight: 800;
    color: #3b0764;
    margin-bottom: 8px;
}

.footer-text {
    font-size: 14px;
    color: gray;
}

/* MOBILE */
@media (max-width: 768px) {

    .hero h1 {
        font-size: 30px;
    }

    .hero p {
        font-size: 14px;
    }

    div[data-testid="stFileUploader"] {
        width: 95% !important;
        padding: 18px !important;
    }
}

</style>
""", unsafe_allow_html=True)

# ------------------ HERO ------------------
st.markdown("""
<div class="hero">
    <h1>TenderMind AI</h1>
    <p>Automate tender evaluation in seconds, not weeks</p>
</div>
""", unsafe_allow_html=True)

# ------------------ UPLOAD ------------------
uploaded_file = st.file_uploader(
    "Upload your tender document",
    type=["png", "jpg", "jpeg", "pdf"]
)

# ------------------ FAKE AI ------------------
def fake_ai():
    with st.spinner("Analyzing document..."):
        time.sleep(2)

    return [
        ("Revenue Check", "✅ Pass"),
        ("Safety Certificate", "❌ Fail"),
        ("Experience Requirement", "✅ Pass")
    ]

# ------------------ RESULTS ------------------
if uploaded_file:
    results = fake_ai()

    st.markdown('<div class="result-box">', unsafe_allow_html=True)

    st.subheader("Evaluation Results")

    for r in results:
        st.write(f"**{r[0]}** → {r[1]}")

    st.markdown('</div>', unsafe_allow_html=True)

# ------------------ FOOTER ------------------
# ------------------ FOOTER ------------------
st.markdown("---")

col1, col2 = st.columns([3, 2])

with col1:
    st.markdown("Contact | Careers | Privacy Policy | Terms & Conditions")

with col2:
    st.markdown("### TenderMind AI")
    st.caption("© 2026 TenderMind AI.  All Rights Reserved.")
