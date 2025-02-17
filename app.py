from flask import Flask, render_template, request, flash, redirect, url_for

app = Flask(__name__)

app.secret_key = "panchait" # necessary, if we are using flash and session


@app.route("/home", methods=['POST','GET'])
def index():
    expression = ""
    if request.method == 'POST':

        current_value = request.form['expression']  # Get previous expression
        new_value = request.form['button']  # Get clicked button value
            
        if new_value == "C":
            expression = ""
        
        elif new_value == "D":
            expression = current_value[:len(current_value)-1] # removing last sting character and saving the remaining string in a variable
            
        elif new_value == "=":
            try:
                expression = str(eval(current_value))  # Convert result to string (if we use int(eval()) then it will convert the decimal into integer)
            except:
                expression = "Error"  # Handle invalid expressions, like dividing by 0 
            
        else:
            expression = current_value + new_value  # Append the new value (in calculator)

    
    return render_template("index.html", expression = expression)


@app.route("/", methods=['POST', 'GET'])
def register():

    name = ""
    password = ""

    if request.method == 'POST':
        name = request.form['name']
        password = request.form['pass']

    
        with open("D:\\Name.txt", "a+") as file:
            file.seek(0)
            names = file.read().splitlines()
        
        with open("D:\\Password.txt", "a+") as file:
            file.seek(0) # when we open in append the pointer is in the end of the file so we move it to the start
            passwords = file.read().splitlines()
        
        if name in names or password in passwords:
            flash("User_name Or Password Is Already In Use !", "danger")
            return  redirect(url_for('register'))
            
        with open("D:\\Name.txt", "a") as file:
            file.write(name + "\n")
        
        with open("D:\\Password.txt", "a") as file:
            file.write(password + "\n")
        
        flash("Successfuly Registered !", "success")
        return redirect(url_for('login'))
    
    return render_template('register.html')

@app.route("/login", methods=['POST', 'GET'])
def login():

    name = ""
    password = ""

    if request.method == 'POST':
        name = request.form['name']
        password = request.form['pass']
    
        with open("D:\\Name.txt", "a+") as file:
            file.seek(0)
            names = file.read().splitlines()
        
        with open("D:\\Password.txt", "a+") as file:
            file.seek(0) # when we open in append the pointer is in the end of the file so we move it to the start
            passwords = file.read().splitlines()
        
        if name in names and password in passwords:
            return redirect(url_for('index')) # using redirect instead of render tamplate is because it will remove the flash meassage once its show, in render tamplate it permenantly remain
        
        else:
            flash("Wrong Password/Name !", "danger")
            return redirect(url_for("login"))
    
    # When the request method is GET, just render the login page
    return render_template('login.html')


if __name__ == "__main__":
    app.run(debug=True)