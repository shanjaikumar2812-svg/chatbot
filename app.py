from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

# Home page
@app.route("/")
def home():
    return render_template("index.html")

# Chatbot API
@app.route("/chat", methods=["POST"])
def chat():

    user_message = request.json["message"].lower()

    # Rule-Based Replies

    if user_message == "hi":
        reply = "Hello Student!"

    elif user_message == "hello":
        reply = "Hi! Welcome to Data Science."

        reply = "DS means Data Science."

    elif user_message == "python":
        reply = "In Data Science field the most important language is python it is used in various DS field like data analysis, machine learning, Data engineering."

    elif user_message == "what is machine learning":
        reply = "Machine Learning helps systems learn from data."

    elif user_message == "roadmap for data scientist":
        reply = """Strong foundations in math, statistics, and Python,
                   then progress through data analysis, machine learning, deep learning,
                   and finally MLOps and business communication.
                   Building a portfolio of projects is essential to stand out in internships and jobs."""
    
    elif user_message == "what is data analysis":
        reply = "Data analysis is a technique to finding the trends and patterns from given dataset"
    
    elif user_message == "best company for data scientist role":
        reply = "1.Deloitte," \
        "2.Accenture," \
        "3.Google," \
        "4.Amazon," \
        "5.latent view," \
 
 
    elif user_message == "bye":
        reply = "Goodbye Student!"

    else:
        reply = "Sorry, I don't understand."

    return jsonify({
        "reply": reply
    })

# Run Flask
if __name__ == "__main__":
    app.run(debug=True)