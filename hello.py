from flask import Flask   # import Flask from the package flask

app = Flask(__name__)	  # create an instance of a Flask object

@app.route("/") 		  # Flask uses decorators for URL routing, so this line of code means that the function directly below it should be called whenever a user visits the main root page of our web application (which is de ned by the single forward slash).
def index():          # function that returns a simple message
	return "Hello, Worlld!"

if __name__ == '__main__':  # This is a simple conditional statement that evaluates to True if our application is run directly.
	app.run(port=5000, debug=True) # kicks off Flask's development server on our local machine. We set it to run on port 5000 (we'll use port 80 for production) and set debug to True, which will help us see detailed errors directly in our web browser.