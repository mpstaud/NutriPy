from flask import Flask, render_template, request

app = Flask(__name__)

class User:
    def __init__(self, name, username , password, height, weight, activity, goal):
        self.name = name
        self.username = username
        self.password = password
        self.height = height
        self.weight = weight
        self.activity = activity
        self.goal = goal

class ActivityProfile:
    def __init__(self,factor):
        self.factor = factor
    def display(self):
        print("Activity Factor: ", self.factor)

@app.route("/")
def index():
    return render_template('./index.html')
# takes user to the login screen
@app.route('/login', methods=['GET','POST'])
def login():
    username = request.form['username']
    password = request.form['password']
    correctpass = 'Chel$e@D@gg3r1988'
    userExists = 'mpstauds'
    # evaluate entered credentials
    if password != correctpass or username != userExists:
        return render_template('./index.html')
    elif username == userExists and password == correctpass:
        return render_template('./login.html')
# takes user to the sign-up page if they select it   
@app.route('/signup', methods=['GET','POST'])
def signup():
    name = request.form['name']
    username = request.form['username']
    password = request.form['password']
    newuser = User(name, username, password, None, None, None, None)
    return render_template()
    
@app.route('/OK', methods=['POST'])
def OK():
    global height_ft
    global height_in
    global weight
    # retrieve form data
    height_ft = request.form['height-ft']
    height_in = request.form['height-in']
    weight = request.form['weight']
    print(height_ft, height_in, weight)
    if request.method == "POST":
        return "Height: " + str(height_ft) + "' " + str(height_in) + '" ' + "Weight: " + str(weight) + " lbs"
    return render_template('./results.html', height_ft=height_ft,height_in=height_in,weight=weight)

if __name__ == "__main__":
    app.run(debug=True)