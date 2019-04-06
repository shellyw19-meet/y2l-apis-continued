from flask import Flask, render_template, request
import requests, json 
app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/study_image', methods = ['POST'])
def study_image():
    
	image_url = request.form['url-input']
	headers = {'Authorization': 'Key 7b213217187e43eeaab874c849f449ec'}

	url = "https://api.clarifai.com/v2/models/aaa03c23b3724a16a56b629203edc62c/outputs"

	pic ={"inputs": [
	      {
	        "data": {
	          "image": {
	            "url": image_url
	          }
	        }
	      }
	    ]}

	requesti = requests.post(url, headers=headers, data=json.dumps(pic))
	return render_template('home.html', results=requesti.content)

if __name__ == '__main__':
    app.run(debug=True)