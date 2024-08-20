from flask import Flask, render_template, request

# Create an instance of the Flask class
app = Flask(__name__)

# Route for the home page
@app.route('/')
def index():
    # Render and return the index.html file
    return render_template('index.html')

# Route that handles form submission and word counting
@app.route('/count', methods=['POST'])
def count_words():
    # Get the text input from the form
    text = request.form['text']
    
    # Split the text into a list of words
    words = text.split()
    
    # Count the total number of words
    word_count = len(words)
    
    # Create a dictionary to store word frequencies
    word_frequency = {}
    for word in words:
        # Convert the word to lowercase
        word = word.lower()
        # Count the occurrences of each word
        word_frequency[word] = word_frequency.get(word, 0) + 1

    # Render the result.html file with word count and frequency data
    return render_template('result.html', word_count=word_count, word_frequency=word_frequency)

# Start the Flask app when this script is executed
if __name__ == '__main__':
    app.run(debug=True)
