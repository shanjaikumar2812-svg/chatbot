from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/chat", methods=["POST"])
def chat():
    user_message = request.json.get("message", "")
    
    knowledge_Base = {
        "hello": "Hi!! welcome to data Science",
        "hi": "Hello learner",
        "machine learning": "Machine learning is a subset of AI that enables the system to learn from the data to make predictions or decisions.",
        "what is machine learning": "Machine Learning helps systems learn from data.",
        "roadmap for data scientist": "Strong foundations in math, statistics, and Python, then progress through data analysis, machine learning, deep learning, and finally MLOps and business communication. Building a portfolio of projects is essential to stand out in internships and jobs.",
        "what is data analysis": "Data analysis is a technique to finding the trends and patterns from a given dataset.",
        "best company for data scientist role": "1. Deloitte, 2. Accenture, 3. Google, 4. Amazon, 5. Latent View",
        "python": "In the Data Science field, the most important language is Python. It is heavily used in analysis, modeling, and deployment.",
        "pandas": "A crucial Python library for data manipulation, wrangling, and cleaning structured data.",
        "numpy": "A library for the Python programming language, adding support for large, multi-dimensional arrays and matrices.",
        "scikit-learn": "A powerful Python library featuring various machine learning algorithms, perfect for predictive modeling.",
        "matplotlib": "A comprehensive library for creating static, animated, and interactive visualizations in Python.",
        "seaborn": "A Python data visualization library based on matplotlib that provides a high-level interface for drawing attractive statistical graphics.",
        "database": "An organized collection of structured information, or data, typically stored electronically in a computer system.",
        "sql": "Structured Query Language, used for communicating with and extracting data from relational databases.",
        "nosql": "Databases that store data in formats other than relational tables, highly flexible for unstructured pipelines.",
        "mongodb": "A popular NoSQL, document-oriented database that offers high flexibility for unstructured data and fast querying.",
        "data pipeline": "A set of actions that extract data from various sources, transform it, and load it into a central repository.",
        "data visualization": "The graphical representation of information and data to highlight patterns and trends.",
        "power bi": "A powerful analytics service used to convert raw data outputs into interactive, clean dashboards.",
        "tableau": "A visual analytics platform transforming the way we use data to solve problems and share insights.",
        "dashboard": "A visual display of the most important information needed to achieve one or more objectives.",
        "deployment": "The process of integrating a machine learning model into an existing production environment to make practical business decisions based on data.",
        "html": "HyperText Markup Language, the standard markup language for documents designed to be displayed in a web browser.",
        "css": "Cascading Style Sheets, used for styling, formatting, and arranging web pages.",
        "bootstrap": "A popular CSS framework used for developing responsive, mobile-first websites and interfaces quickly.",
        "api": "Application Programming Interface, a software intermediary that allows two applications to talk to each other."
    }

    # Clean the input
    user_message = user_message.lower().strip()

    # Look up the response
    if user_message in knowledge_Base:
        reply = knowledge_Base[user_message]
    else:
        reply = "Sorry, I don't understand that."
         
    return jsonify({"reply": reply})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=False)