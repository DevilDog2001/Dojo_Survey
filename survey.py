from flask import Flask,render_template,request,redirect,session
app = Flask(__name__)   
app.secret_key="Mr.Python" 
@app.route('/')       
def form():
    return render_template("survey.html")
@app.post('/result')        
def result_post():
    name = request.form["name"]
    location = request.form["location"]
    language = request.form["language"]
    comments = request.form["comments"]
    return render_template("results.html",name=name,location=location,language=language,comments=comments)
@app.get('/result')        
def result_get():
    return redirect('/')
if __name__=="__main__":       
    app.run(debug=True)    