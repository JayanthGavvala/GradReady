import streamlit as st
import google.generativeai as genai

# --- Securely configure the AI ---
genai.configure(api_key=st.secrets["GEMINI_API_KEY"])
model = genai.GenerativeModel('gemini-2.5-flash')

st.set_page_config(page_title="AI Interview Prep Agent", page_icon="🤖")

st.title("🤖 AI Technical Interview Coach")
st.write("Welcome to your 2nd-year prep! Let's test your knowledge.")

# Sidebar
st.sidebar.header("Interview Settings")
role = st.sidebar.selectbox("Target Role", ["Machine Learning Engineer", "Data Scientist", "Software Engineer"])
difficulty = st.sidebar.select_slider("Difficulty", options=["Intern", "Junior", "Mid-Level"])

st.subheader(f"Role: {role} ({difficulty})")

# --- State Management (The "Memory" feature) ---
# This stops the question from disappearing when the page refreshes
if "current_question" not in st.session_state:
    st.session_state.current_question = None

# Button to generate a brand new question
if st.button("Generate New Interview Question"):
    with st.spinner("Thinking of a tough question..."):
        # Prompt 1: Asking the AI to make a question
        question_prompt = f"""
        You are a technical interviewer hiring for a {difficulty} {role} position.
        Generate ONE realistic technical interview question. 
        Do not provide the answer, just the question. Keep it concise.
        """
        response = model.generate_content(question_prompt)
        
        # Save the AI's question into our session state memory
        st.session_state.current_question = response.text

# Only show the answer box if a question has been generated
if st.session_state.current_question:
    st.info(f"**Question:** {st.session_state.current_question}")
    
    # User response
    user_answer = st.text_area("Your Response:", placeholder="Type your answer here...")

    # The actual AI evaluation
    if st.button("Submit Answer for Evaluation"):
        if user_answer:
            with st.spinner("The AI is reviewing your answer..."):
                # Prompt 2: Asking the AI to grade the answer
                eval_prompt = f"""
                You are a strict but fair technical interviewer for a {difficulty} {role} position.
                The interview question was: '{st.session_state.current_question}'
                The candidate answered: '{user_answer}'
                
                Please evaluate their answer. Point out what they got right, what they missed or got wrong, 
                and give them a score out of 10. Keep your feedback concise and professional.
                """
                
                eval_response = model.generate_content(eval_prompt)
                
                # Display the AI's feedback
                st.markdown("### Interviewer Feedback")
                st.write(eval_response.text)
        else:
            st.warning("Please type an answer before submitting.")
else:
    st.write("👈 Click **'Generate New Interview Question'** to begin!")