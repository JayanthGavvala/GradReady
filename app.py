import streamlit as st

st.set_page_config(page_title="AI Interview Prep Agent", page_icon="🤖")

st.title("🤖 AI Technical Interview Coach")
st.write("Welcome, Jayanth! Let's get you ready for 2nd-year internship applications.")

# Sidebar for configuration
st.sidebar.header("Interview Settings")
role = st.sidebar.selectbox(
    "Target Role",
    ["Machine Learning Engineer", "Data Scientist", "Software Engineer (AI/AI Dev)"]
)
difficulty = st.sidebar.select_slider("Difficulty", options=["Junior", "Mid-Level", "FAANG-level"])

# Main interface
st.subheader(f"Current Simulation: {role} ({difficulty})")

# Simulate a question generation
if st.button("Generate Next Interview Question"):
    if role == "Machine Learning Engineer":
        st.info("**Question:** Explain the difference between L1 and L2 regularization, and how they affect model weights.")
    elif role == "Data Scientist":
        st.info("**Question:** How would you handle a severe class imbalance dataset when training a fraud detection model?")
    else:
        st.info("**Question:** Walk me through the time complexity of searching a binary search tree in the worst case.")

# User response box and there
user_answer = st.text_area("Your Response:", placeholder="Type your answer here...")

if st.button("Submit Answer for Evaluation"):
    if user_answer:
        st.success("Answer received! (Next step: Connect an LLM API key to get real-time feedback on your code).")
    else:
        st.warning("Please type an answer before submitting.")