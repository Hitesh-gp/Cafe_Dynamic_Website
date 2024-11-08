import streamlit as st
import subprocess
import os

# Define the persistent directory to store your playbook files
PERSISTENT_DIR = "/home/hitesh/Cafe_Dynamic_Website"

# Function to update playbook with the GitHub repository URL
def update_playbook(git_repo_url, playbook_file):
    try:
        # Ensure the persistent directory exists
        if not os.path.exists(PERSISTENT_DIR):
            os.makedirs(PERSISTENT_DIR)

        playbook_path = os.path.join(PERSISTENT_DIR, playbook_file)

        # Read the playbook template
        with open(playbook_path, 'r') as file:
            playbook_content = file.read()

        # Replace the placeholder with the provided GitHub repository URL
        updated_playbook = playbook_content.replace("{{ repo_url }}", git_repo_url)

        # Write the updated content back to a new file in the persistent directory
        updated_playbook_file = os.path.join(PERSISTENT_DIR, playbook_file.replace(".yml", "_updated.yml"))
        with open(updated_playbook_file, 'w') as file:
            file.write(updated_playbook)

        st.success(f"Playbook updated with repository URL: {git_repo_url}")
        return updated_playbook_file

    except Exception as e:
        st.error(f"Error updating the playbook: {e}")
        return None

# Function to deploy the website on Bare Metal using Ansible
def deploy_baremetal(git_repo):
    try:
        st.text(f"Deploying website from {git_repo} on bare metal...")
        
        # Update the playbook with the GitHub repository URL
        updated_playbook = update_playbook(git_repo, 'deploy_baremetal.yml')
        
        if updated_playbook:
            # Run the updated playbook
            result = subprocess.run(['ansible-playbook', updated_playbook], capture_output=True, text=True)
            st.text(result.stdout)
            if result.returncode == 0:
                st.success("Deployment successful on Bare Metal!")
                
                # Provide the link to the deployed website
                website_url = "http://localhost/Cafe_Dynamic_Website/mompopcafe/"
                st.markdown(f"Your website has been successfully deployed! You can access it [here]({website_url}).")
            else:
                st.error("Deployment failed on Bare Metal!")
        else:
            st.error("Failed to update playbook. Deployment aborted.")
            
    except Exception as e:
        st.error(f"Error: {e}")

# Function to deploy the website using Docker
def deploy_docker(git_repo):
    try:
        st.text(f"Deploying website from {git_repo} using Docker...")
        
        # Update the playbook with the GitHub repository URL
        updated_playbook = update_playbook(git_repo, 'deploy_docker_compose.yml')
        
        if updated_playbook:
            # Run the updated playbook
            result = subprocess.run(["ansible-playbook", updated_playbook], capture_output=True, text=True)
            st.text(result.stdout)
            if result.returncode == 0:
                st.success("Deployment successful with Docker!")
                
                # Provide the link to the deployed website
                website_url = "http://localhost:80"
                st.markdown(f"Your website has been successfully deployed! You can access it [here]({website_url}).")
            else:
                st.error("Deployment failed with Docker!")
            
    except Exception as e:
        st.error(f"Error: {e}")

# Streamlit UI
st.title('Automated Deployment of Website')

# Input for GitHub Repository Link
git_repo = st.text_input("Enter the GitHub repository URL:", "")

if git_repo:
    # Choose Deployment Option
    deployment_option = st.radio(
        "Choose the deployment option:",
        ("Bare Metal", "Docker", "Kubernetes")
    )

    # Trigger deployment based on the chosen option
    if deployment_option == "Bare Metal":
        if st.button("Deploy on Bare Metal"):
            deploy_baremetal(git_repo)
    elif deployment_option == "Docker":
        if st.button("Deploy with Docker"):
            deploy_docker(git_repo)
