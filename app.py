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
    font-size: 46px;
    font-weight: 900;
    color: #3b0764;
    margin-bottom: 10px;
}

.hero p {
    font-size: 17px;
    color: #555;
}

/* FILE UPLOADER */
div[data-testid="stFileUploader"] {
    background: white;
    padding: 28px;
    border-radius: 16px;
    border: 2px dashed #a855f7;
    width: 90%;
    max-width: 520px;
    margin: 25px auto;
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
    padding: 22px;
    border-radius: 14px;
    box-shadow: 0px 5px 20px rgba(0,0,0,0.08);
}

/* FOOTER */
.footer {
    width: 100%;
    padding: 50px 20px;
    border-top: 1px solid rgba(0,0,0,0.08);
    margin-top: 60px;
}

.footer-container {
    display: flex;
    justify-content: space-between;
    align-items: flex-start;
    max-width: 900px;
    margin: auto;
    flex-wrap: wrap;
    gap: 30px;
}

/* LINKS */
.footer-links {
    font-size: 15px;
    display: flex;
    flex-wrap: wrap;
    gap: 18px;
    color: #444;
}

/* BRAND */
.footer-brand {
    text-align: right;
    min-width: 220px;
}

.footer-brand h2 {
    font-size: 30px;
    font-weight: 900;
    color: #3b0764;
    margin: 0;
}

/* BIG GAP */
.footer-gap {
    height: 12px;
}

.footer-brand p {
    font-size: 14px;
    color: gray;
    margin: 0;
}

/* MOBILE */
@media (max-width: 768px) {

    .hero h1 {
        font-size: 32px;
    }

    .hero p {
        font-size: 14px;
    }

    div[data-testid="stFileUploader"] {
        padding: 18px !important;
        width: 95% !important;
    }

    .footer-container {
        flex-direction: column;
        align-items: center;
        text-align: center;
    }

    .footer-brand {
        text-align: center;
    }

    .footer-links {
        justify-content: center;
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
st.markdown("<br><br><br>", unsafe_allow_html=True)

st.markdown("""
<style>
.footer {
    width: 100%;
    padding: 50px 20px;
    border-top: 1px solid rgba(0,0,0,0.08);
    margin-top: 60px;
}

.footer-container {
    display: flex;
    justify-content: space-between;
    max-width: 900px;
    margin: auto;
    flex-wrap: wrap;
    gap: 30px;
}

.footer-links {
    font-size: 15px;
    display: flex;
    flex-wrap: wrap;
    gap: 18px;
    color: #444;
}

.footer-brand {
    text-align: right;
    min-width: 220px;
}

.footer-brand h2 {
    font-size: 30px;
    font-weight: 900;
    color: #3b0764;
    margin: 0;
}

.footer-gap {
    height: 12px;
}

.footer-brand p {
    font-size: 14px;
    color: gray;
    margin: 0;
}

@media (max-width: 768px) {
    .footer-container {
        flex-direction: column;
        text-align: center;
        align-items: center;
    }

    .footer-brand {
        text-align: center;
    }

    .footer-links {
        justify-content: center;
    }
}
</style>
""", unsafe_allow_html=True)



# ------------------ FOOTER ------------------
st.markdown("---")

col1, col2 = st.columns([3, 2])

with col1:
    st.markdown(
        """
        **Contact** | **Careers** | **Privacy Policy** | **Terms & Conditions**
        """
    )

with col2:
    st.markdown(
        """
        <div style="text-align:right;">
            <div style="font-size:26px; font-weight:800; color:#3b0764;">
                TenderMind AI
            </div>

            <div style="height:10px;"></div>

            <div style="font-size:14px; color:gray;">
                © 2026 TenderMind AI. All rights reserved.
            </div>
        </div>
        """,
        unsafe_allow_html=True
    ) 

    </div>
</div>
""", unsafe_allow_html=True) 
