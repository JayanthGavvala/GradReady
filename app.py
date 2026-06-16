import streamlit as st
import google.generativeai as genai

# --- Securely configure the AI ---
# Streamlit looks in .streamlit/secrets.toml for this key automatically
genai.configure(api_key=st.secrets["GEMINI_API_KEY"])
model = genai.GenerativeModel('gemini-1.5-flash')

st.set_page_config(page_title="AI Interview Prep Agent", page_icon="🤖")

st.title("🤖 AI Technical Interview Coach")
st.write("Welcome to your 2nd-year prep! Let's test your knowledge.")

# Sidebar
st.sidebar.header("Interview Settings")
role = st.sidebar.selectbox("Target Role", ["Machine Learning Engineer", "Data Scientist", "Software Engineer"])
difficulty = st.sidebar.select_slider("Difficulty", options=["Intern", "Junior", "Mid-Level"])

st.subheader(f"Role: {role} ({difficulty})")

# Determine the question based on role
if role == "Machine Learning Engineer":
    question = "Explain the difference between L1 and L2 regularization, and how they affect model weights."
elif role == "Data Scientist":
    question = "How would you handle a severe class imbalance dataset when training a fraud detection model?"
else:
    question = "Walk me through the time complexity of searching a binary search tree in the worst case."

st.info(f"**Question:** {question}")

# User response
user_answer = st.text_area("Your Response:", placeholder="Type your answer here...")

# The actual AI evaluation
if st.button("Submit Answer for Evaluation"):
    if user_answer:
        with st.spinner("The AI is reviewing your answer..."):
            # We build a prompt giving the AI context on how to act
            prompt = f"""
            You are a strict but fair technical interviewer for a {difficulty} {role} position.
            The interview question was: '{question}'
            The candidate answered: '{user_answer}'
            
            Please evaluate their answer. Point out what they got right, what they missed or got wrong, 
            and give them a score out of 10. Keep your feedback concise and professional.
            """
            
            # Send it to the model
            response = model.generate_content(prompt)
            
            # Display the AI's feedback
            st.markdown("### Interviewer Feedback")
            st.write(response.text)
    else:
        st.warning("Please type an answer before submitting.")