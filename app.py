import streamlit as st
import time

# ------------------ CONFIG ------------------
st.set_page_config(page_title="TenderMind AI", layout="wide")

# ------------------ STYLE ------------------
st.markdown("""
<style>

/* BACKGROUND */
.stApp {
    background: linear-gradient(135deg, #ffffff 0%, #f5edff 100%);
    font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", sans-serif;
}

/* HERO SECTION */
.hero {
    text-align: center;
    margin-top: 80px;
    margin-bottom: 50px;
}

.hero h1 {
    font-size: 64px;
    font-weight: 800;
    color: #3b0764;
    margin-bottom: 10px;
}

.hero p {
    font-size: 20px;
    color: #555;
}

/* UPLOAD BOX */
div[data-testid="stFileUploader"] {
    background: white;
    padding: 50px;
    border-radius: 20px;
    border: 2px dashed #a855f7;
    width: 60%;
    margin: 40px auto;
    transition: 0.3s;
}

div[data-testid="stFileUploader"]:hover {
    border-color: #7e22ce;
    box-shadow: 0px 10px 30px rgba(168,85,247,0.2);
}

/* BUTTON (if any appears later) */
.stButton button {
    background: #7e22ce;
    color: white;
    border-radius: 10px;
    padding: 10px 20px;
    border: none;
}

/* RESULT BOX */
.result-box {
    width: 60%;
    margin: auto;
    margin-top: 30px;
    background: white;
    padding: 25px;
    border-radius: 15px;
    box-shadow: 0px 5px 20px rgba(0,0,0,0.08);
}

/* FOOTER */
.footer {
    display: flex;
    justify-content: space-between;
    padding: 40px 80px;
    margin-top: 100px;
    border-top: 1px solid #eee;
    font-size: 14px;
    color: #444;
}

.footer-left span {
    margin-right: 25px;
    cursor: pointer;
    transition: 0.2s;
}

.footer-left span:hover {
    color: #7e22ce;
}

.footer-right strong {
    display: block;
    font-size: 16px;
}

.footer-right small {
    color: #777;
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
uploaded_file = st.file_uploader("", type=["png", "jpg", "jpeg", "pdf"])

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
col1, col2 = st.columns([3, 1])
with col1:
    st.markdown(
        "Contact &nbsp;&nbsp;&nbsp; Careers &nbsp;&nbsp;&nbsp; Privacy Policy &nbsp;&nbsp;&nbsp; Terms and Conditions",
        unsafe_allow_html=True
    )
with col2:
    st.markdown(
        "<p style='font-size:22px; font-weight:600; margin-bottom:0; text-align:right;'>TenderMind AI</p>",
        unsafe_allow_html=True
    )
    st.markdown(
        "<p style='font-size:13px; color:gray; margin-top:28px; text-align:right;'>© 2026 tendermind</p>",
        unsafe_allow_html=True
    )
    