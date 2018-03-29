from flask import Flask, request
from caesar import rotate_character, alphabet_position
app = Flask(__name__)
app.config['DEBUG'] = True
header="""<!DOCTYPE html>

<html>
    <head>
        <style>
            form {
                background-color: #eee;
                padding: 20px;
                margin: 0 auto;
                width: 540px;
                font: 16px sans-serif;
                border-radius: 10px;
            }
            textarea {
                margin: 10px 0;
                width: 540px;
                height: 120px;
            }
        </style>
    </head>
    <body>"""
body="""
    <form method="post">
        <p>
            Rotate by:
            <input type="text" name="rot"/>
        </p>
        <textarea type="text" name="text">{0}</textarea>
        <input type="submit" value="submit"/>
    </form>""" 
footer="""</body>
</html>"""

@app.route("/")
def index():
    new_str = ""
    return header + body.format(new_str) + footer
    
@app.route("/", methods=['POST'])
def encrypt():
    text = request.form['text']
    rot = int(request.form['rot'])
    new_str = ""
    for i in range(len(text)):
        if text[i].isalpha():
            new_str = new_str + rotate_character(text[i], rot)
        else:
            new_str = new_str + text[i]
    return header + body.format(new_str) + footer

app.run()