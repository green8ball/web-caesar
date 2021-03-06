from flask import Flask, request
from caesar import rotate_string

app = Flask(__name__)
app.config['DEBUG'] = True

form = """

<!DOCTYPE html>

<html>
    <head>
        <style>
            form {{
                background-color: #eee;
                padding: 20px;
                margin: 0 auto;
                width: 540px;
                font: 16px sans-serif;
                border-radius: 10px;
            }}
            textarea {{
                margin: 10px 0;
                width: 540px;
                height: 120px;
            }}
        </style>
    </head>
    <body>
        <form action="/" method="post">
            <label for="rot" value="Rotate By:">
                Rotate by:
                <input type="text" id="rot" name="rot" value="{0}"/>
                <textarea id="text" name="text">{1}</textarea>
            </label>
            <input type="submit" value="Submit Query"/>
        </form>
    </body>
</html>

"""

@app.route("/", methods=['POST'])
def encrypt():
    rot = int(request.form['rot'])
    text = request.form['text']
    rotated_string = rotate_string(text, rot)

    response_string = ""
    response_string += "<h1>" + rotated_string + "</h1>"

    return form.format(rot, rotated_string)


@app.route("/")
def index():
    return form.format('','')

app.run()