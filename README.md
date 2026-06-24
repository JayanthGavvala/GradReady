# ai-interview-prep-agent

⚡ NexGen AI Interview SimulatorAn AI-powered, full-stack web application designed to simulate technical interview "deep dives."Instead of generic LeetCode questions, this application parses a user's uploaded CV and generates highly specific, contextual interview questions based on their actual past projects and listed experience—exactly like a real Senior Engineering interviewer would.✨ Key FeaturesContext-Aware Interviewing: Uses PyPDF2 to extract text from uploaded CVs, injecting the user's real experience into the LLM's system prompt to generate highly personalized technical questions.Multi-Modal Responses: Integrates browser-based Speech-to-Text (streamlit-mic-recorder), allowing users to practice speaking their answers out loud, or fallback to standard text input.Instant AI Feedback: Leverages the Google Gemini 2.5 API to act as a strict technical interviewer, evaluating answers for accuracy, pointing out missing concepts, and grading the response out of 10.Cloud Progress Tracking: Connects to a Google Firebase (Firestore) backend to permanently store user profiles, interview transcripts, and plot historical performance trends on a live dashboard.Modern UI/UX: Built with Streamlit but heavily customized with injected CSS to create a sleek, single-page "scrollytelling" interface native to modern SaaS platforms.🛠️ Tech StackFrontend: Python, Streamlit, HTML/CSS (Custom styling)Backend: Google Firebase (Firestore Cloud Database)AI/LLM: Google Generative AI (Gemini 2.5 Flash)Utilities: PyPDF2 (Document parsing), Streamlit Mic Recorder (Audio processing), RegEx (Data extraction)🚀 Running the Project LocallyIf you would like to run this application on your local machine, follow these steps:1. Clone the repositorygit clone [https://github.com/yourusername/ai-interview-prep-agent.git](https://github.com/yourusername/ai-interview-prep-agent.git)
cd ai-interview-prep-agent
2. Set up a Virtual Environmentpython3 -m venv venv
source venv/bin/activate  # On Windows use `venv\Scripts\activate`
3. Install Dependenciespip install -r requirements.txt
4. Configure Environment SecretsYou will need a Gemini API Key and a Google Firebase Service Account JSON.Create a folder named .streamlit in the root directory, and inside it, create a file named secrets.toml. Format it like this:GEMINI_API_KEY = "your_gemini_api_key_here"

[firebase]
type = "service_account"
project_id = "your_project_id"
private_key_id = "your_private_key_id"
private_key = "-----BEGIN PRIVATE KEY-----\nYour_Key_Here\n-----END PRIVATE KEY-----\n"
client_email = "your_client_email"
client_id = "your_client_id"
auth_uri = "[https://accounts.google.com/o/oauth2/auth](https://accounts.google.com/o/oauth2/auth)"
token_uri = "[https://oauth2.googleapis.com/token](https://oauth2.googleapis.com/token)"
auth_provider_x509_cert_url = "[https://www.googleapis.com/oauth2/v1/certs](https://www.googleapis.com/oauth2/v1/certs)"
client_x509_cert_url = "your_cert_url"
5. Launch the Applicationstreamlit run app.py
📈 Future RoadmapImplementing an "Export Transcript" feature to download PDF reports of past interview sessions.Adding a global leaderboard for users to compare their average scores against other candidates.
