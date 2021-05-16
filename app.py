from flask import Flask, request, render_template
import pickle



model = pickle.load(open("DomainRFHyper.pkl","rb"))
app = Flask(__name__,template_folder='template') # Creation of Flask Application


@app.route("/") # This is Home Page  # Root Page /
def home():
    return render_template("index.html")

@app.route('/predict',methods=['POST']) # Providing Features as input to model and providing output
def predict(): # Web API
    '''
    For Rendering Results from on HTML GUI
    '''
    # Accept Input from User    
    if request.method == "POST":
        age = int (request.form.get('age'))
        height = int (request.form.get('height'))
        weight = int (request.form.get('weight'))
        sys = int (request.form.get('sysbp'))
        dys = int (request.form.get('dysbp'))
        # Convert height from cm to m
        height = int(height / 100)
        BMI = int (weight/(height**2))
        features = [[age,height,weight,sys,dys,BMI]]
        prediction = model.predict(features)
    pred = prediction[0]
    if(pred==0):
        return render_template('index.html',prediction_result="Normal Patient")
    else:
        return render_template('index.html',prediction_result="Heart Patient")

if __name__ == "__main__":
    app.run(debug=True)