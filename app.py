import streamlit as st
import time

# ------------------ CONFIG ------------------
st.set_page_config(page_title="TenderMind AI", layout="centered")

# ------------------ STYLE ------------------
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
    font-size: 42px;
    font-weight: 800;
    color: #3b0764;
    margin-bottom: 8px;
}

.hero p {
    font-size: 16px;
    color: #555;
}

/* UPLOADER */
div[data-testid="stFileUploader"] {
    background: white;
    padding: 25px;
    border-radius: 15px;
    border: 2px dashed #a855f7;
    width: 90%;
    max-width: 500px;
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
    max-width: 500px;
    margin: 20px auto;
    background: white;
    padding: 20px;
    border-radius: 12px;
    box-shadow: 0px 5px 20px rgba(0,0,0,0.08);
}

/* MOBILE OPTIMIZATION */
@media (max-width: 768px) {

    .hero h1 {
        font-size: 30px;
    }

    .hero p {
        font-size: 14px;
    }

    div[data-testid="stFileUploader"] {
        padding: 15px !important;
        width: 95% !important;
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
uploaded_file = st.file_uploader("Upload your tender document", type=["png", "jpg", "jpeg", "pdf"])

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
st.markdown("---")

col1, col2 = st.columns([2, 1])

with col1:
    st.markdown(
        """
        <div style='font-size:14px;'>
        Contact &nbsp;&nbsp;&nbsp; 
        Careers &nbsp;&nbsp;&nbsp; 
        Privacy Policy &nbsp;&nbsp;&nbsp; 
        Terms and Conditions
        </div>
        """,
        unsafe_allow_html=True
    )

with col2:
    st.markdown(
        """
        <div style='text-align:right; line-height:1.4;'>
            <div style='font-size:18px; font-weight:600;'>TenderMind AI</div>
            <div style='font-size:12px; color:gray;'>© 2026 tendermind</div>
        </div>
        """,
        unsafe_allow_html=True
    )
