import jinja2
print(jinja2.__file__)


from flask import Flask
from flask import request
from flask import render_template_string

app = Flask(__name__)
app.secret_key = "TmV2ZXIgR29ubmEgR2l2ZSBZb3UgVXA="

@app.route('/')
def index():
    name = request.args.get('name') or "Kenobi"
    template = f"<h1>- Hello There!<br>- General {name}!</h1>"
    return render_template_string(template)

if __name__ =='__main__':
    app.run(port=5000)
