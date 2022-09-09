from flask import Flask, render_template, request, flash, redirect
app = Flask(__name__, template_folder='src/templates')
app.secret_key = 'jhaxcjasjhascjhasdjh'
PORT = 4000

todos= []

@app.before_request
def handle_path():
    print('helllo ', request.host_url)
# 
@app.route("/", methods= ['GET', 'POST'])
def index():
    if request.method == 'POST':
        todo = request.form.get("todo", '')

        if todo == '':
            flash("Please enter an item in the form.")

        elif todo.strip() in todos:
            flash('Item already exist in your todo list')
        else:
            todos.append(todo.strip())
    return render_template("index.html", todos= todos)


@app.route("/remove")
def about():
    item_index = request.args.get("item")
    if item_index and len(todos) > 0:
        item_to_delete = todos[int(item_index)]
        todos.remove(item_to_delete)
    return redirect("/")


@app.route("/contact-us")
def contact_us():
    return render_template("contact.html")

# Run app
if __name__ == "__main__":
    app.run(debug=True, port=PORT)