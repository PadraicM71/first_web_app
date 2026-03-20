# this is the backend
# This handles the logic of receiving the name via a POST request and sending it back to the page.
import os

from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    name = None
    if request.method == "POST":
        # 'user_name' matches the 'name' attribute in your HTML input
        name = request.form.get("user_name")
    return render_template("index.html", name=name)


##### this is for local host:
# if __name__ == "__main__":
#     app.run(debug=True)

if __name__ == "__main__":
    # This picks up the port Render assigns automatically
    port = int(os.environ.get("PORT", 5000))
    # '0.0.0.0' makes it public instead of just "localhost"
    app.run(host='0.0.0.0', port=port)


# It is best practice to use a virtual environment so your Flask installation doesn't interfere with other Python projects. 
# Create the environment: Run python -m venv venv in the terminal (done for mac)
# Activate it:
# Windows:          .\venv\Scripts\activate
# macOS/Linux:      source venv/bin/activate


# Run and View Your App
# In the VS Code terminal, ensure you are in the webapp folder and your venv is active

# Run the app: python app.py
# VS Code will show a link like http://127.0.0.1:5000/. Ctrl + Click it to open your app in the browser




# To push your code to GitHub, you first need a place for it to live online (a repository) and then a few commands to "ship" it from your computer to that repository. 

# 1. Create a Repository on GitHub 
# Log in to GitHub.
# Click the + icon in the top-right corner and select New repository.
# Give it a name (e.g., my-first-project).
# Important: Do not check the boxes for "Add a README", ".gitignore", or "license" if you already have files on your computer; it is easier to add these later.
# Click Create repository.
# Copy the HTTPS URL provided on the next page (it looks like https://github.com). 

# 2. Connect Your Local Code to GitHub
# Open your terminal (inside your project folder) and run these commands in order: 
# Initialize Git: This turns your folder into a local Git repository.
# bash
# git init


# Stage Your Files: This tells Git which files you want to include in the upload.
# bash
# git add .


# Commit the Changes: This creates a "snapshot" of your code with a descriptive label.
# bash
# git commit -m "Initial commit"


# Rename the Branch: Sets your default branch to "main" (modern standard).
# bash
# git branch -M main


# Link to GitHub: Connects your local folder to the online repository you just created. Paste your URL here.
# bash
# git remote add origin PASTE_YOUR_COPIED_URL_HERE


# Push Your Code: Uploads your files to GitHub.
# bash
# git push -u origin main





# ******************************************** IMPORTANT - updates!
# 3. Future Updates
# After you've done this the first time, you only need three commands to send new changes to GitHub: 
# git add .
# git commit -m "Update message"
# git push 
# ******************************************** IMPORTANT - updates!





# Now that your code is on GitHub, you can use a hosting service to pull that code and turn it into a live website. For beginners in 2024-2025, Render and PythonAnywhere are the most reliable free options. 
# Step 1: Prepare Your Project for the Web
# Before hosting, the server needs to know which libraries to install. In your terminal (on your computer), run:
# bash
# pip freeze > requirements.txt
# Use code with caution.

# This creates a file called requirements.txt. Add, commit, and push this new file to GitHub just like you did before. 




# Step 2: Choose Your Hosting Method
# Option A: Render (Best for most modern apps)
# Render automatically updates your site every time you push new code to GitHub. 

# Sign up at Render and connect your GitHub account.
# Click New + > Web Service.
# Select your GitHub repository from the list.
# Configure Settings:
# Name: Anything you like.
# Runtime: Python.
# Build Command: pip install -r requirements.txt.
# Start Command: If using Flask, use gunicorn app:app. If it's a simple script, use python app.py (i used this here)
# Click Create Web Service. Within a few minutes, Render will give you a public onrender.com URL to share. 
# ME: CHECK HOE RENDER UPDATES COMMITS AUTOMATICALLY!!!



# ******************************************** IMPORTANT - updates!
# 3. Future Updates

# if needed:
# pip freeze > requirements.txt

# After you've done this the first time, you only need three commands to send new changes to GitHub: 
# git add .
# git commit -m "Update message"
# git push 
# ******************************************** IMPORTANT - updates!




