# this is the backend
# This handles the logic of receiving the name via a POST request and sending it back to the page.

from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    name = None
    if request.method == "POST":
        # 'user_name' matches the 'name' attribute in your HTML input
        name = request.form.get("user_name")
    return render_template("index.html", name=name)

if __name__ == "__main__":
    app.run(debug=True)


# It is best practice to use a virtual environment so your Flask installation doesn't interfere with other Python projects. 
# Create the environment: Run python -m venv venv in the terminal (done for mac)
# Activate it:
# Windows:          .\venv\Scripts\activate
# macOS/Linux:      source venv/bin/activate


# Run and View Your App
# In the VS Code terminal, ensure you are in the webapp folder and your venv is active

# Run the app: python app.py
# VS Code will show a link like http://127.0.0.1:5000/. Ctrl + Click it to open your app in the browser


