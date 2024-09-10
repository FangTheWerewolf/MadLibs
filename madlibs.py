from flask import Flask, request

app = Flask(__name__)

# Simple function to create a story
def create_story(noun, verb, adjective):
    return f"Once there was a {adjective} {noun} who loved to {verb}."

@app.route("/", methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        noun = request.form.get('noun', 'default noun')
        verb = request.form.get('verb', 'default verb')
        adjective = request.form.get('adjective', 'default adjective')
        return create_story(noun, verb, adjective)
    
    return (
        "Submit a POST request to this URL with form data to generate a story.\n\n"
        "Example form data:\n"
        "noun=cat&verb=sleep&adjective=happy"
    )

if __name__ == "__main__":
    app.run(debug=True)