from flask import Flask, render_template, request
from transformers import pipeline

# Initialize the Flask app
app = Flask(__name__)

# Load the summarization pipeline
summarizer = pipeline("summarization", model="t5-small")

# Define the main route
@app.route('/', methods=['GET', 'POST'])
def home():
    summary_text = None
    if request.method == 'POST':
        # Get text from the form
        text_to_summarize = request.form['text_to_summarize']
        
        # Use the summarizer pipeline
        # Note: The result is a list with a dictionary inside
        result = summarizer(text_to_summarize, max_length=150, min_length=30, do_sample=False)
        
        # Extract the summary text
        summary_text = result[0]['summary_text']
        
    return render_template('index.html', summary=summary_text)

# This block allows us to run the app directly
if __name__ == '__main__':
    app.run(debug=True)