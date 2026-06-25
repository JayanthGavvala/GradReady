#  Firebase Setup Guide

## Step 1 — Create a Firebase Project

1. Go to [https://console.firebase.google.com](https://console.firebase.google.com)
2. Click **Add project**
3. Name it (e.g. `gradready`) and click through the setup wizard
4. Disable Google Analytics when asked — you do not need it

---

## Step 2 — Enable Firestore

1. In the left sidebar click **Firestore Database**
2. Click **Create database**
3. Choose **Start in test mode**
4. Pick a region close to you (e.g. `europe-west2` for UK) and click **Enable**

---

## Step 3 — Get Your Service Account Key

This is what lets your Python app talk to Firebase securely.

1. Click the ** gear icon** (top left) → **Project settings**
2. Go to the **Service accounts** tab
3. Click **Generate new private key** → **Generate key**
4. A `.json` file downloads — open it in a text editor

>  Never commit this file to GitHub. Add `*.json` to your `.gitignore`.

---

## Step 4 — Fill In Your `secrets.toml`

Create `.streamlit/secrets.toml` in your project root and copy the values from the downloaded JSON:

```toml
GEMINI_API_KEY = "your_gemini_api_key_here"

[firebase]
type                        = "service_account"
project_id                  = "your-project-id"
private_key_id              = "your-private-key-id"
private_key                 = "-----BEGIN PRIVATE KEY-----\nYour_Key_Here\n-----END PRIVATE KEY-----\n"
client_email                = "your-client-email"
client_id                   = "your-client-id"
auth_uri                    = "https://accounts.google.com/o/oauth2/auth"
token_uri                   = "https://oauth2.googleapis.com/token"
auth_provider_x509_cert_url = "https://www.googleapis.com/oauth2/v1/certs"
client_x509_cert_url        = "your-cert-url"
```

> The `private_key` value contains literal `\n` characters — paste it exactly as it appears in the JSON file, keeping those `\n` sequences intact.

---

## Step 5 — Deploying to Streamlit Cloud

Your `secrets.toml` should never be committed, so on Streamlit Cloud you add secrets manually:

1. Go to [share.streamlit.io](https://share.streamlit.io)
2. Find your app → click **⋮** → **Settings** → **Secrets**
3. Paste the entire contents of your `secrets.toml`
4. Click **Save** and reboot the app

---

## How Data is Stored

```
Firestore
└── artifacts/
    └── gradready-app/
        └── users/
            └── {username}/
                └── history: [ array of interview sessions ]
```

Each session stores the question, your answer, the AI feedback, score, role, and year — everything needed to rebuild your dashboard when you log back in.
