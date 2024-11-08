# app.py
import streamlit as st
import subprocess

st.title("Automated Deployment of Cafe Dynamic Website")

# Option to deploy, stop, or check status
action = st.selectbox("Choose an action", ["Deploy", "Stop", "Check Status"])

if st.button("Execute"):
    if action == "Deploy":
        st.write("Deploying application...")
        subprocess.run(["ansible-playbook", "deploy.yml"])
    elif action == "Stop":
        st.write("Stopping application...")
        subprocess.run(["ansible-playbook", "stop.yml"])
    elif action == "Check Status":
        st.write("Checking status...")
        result = subprocess.run(["docker", "ps"], capture_output=True, text=True)
        st.code(result.stdout)
