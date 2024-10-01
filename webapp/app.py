from flask import Flask, request

app = Flask(__name__)

@app.route('/')
def home():
    page = """
    <h1>Home - Subtraction<h1>
    <a href="/multiply">Multiplication</a>
    <br>
    <a href="/divide">Division</a>
    <form action=/ method=get>
        <input name=a />
        <input name=b />
        <input type=submit />
    </form>
    """
    try:
        a = int(request.args["a"])
        b = int(request.args["b"])
        page += f" <p>The difference is {a-b}</p>"
    except:
        pass
    
    return page


@app.route('/multiply')
def multiply():
    page = """
    <h1>Multiplication<h1>
    <a href="/">Home</a>
    <br>
    <a href="/divide">Division</a>
    <form action=/multiply method=get>
        <input name=a />
        <input name=b />
        <input type=submit />
    </form>
    """
    try:
        a = int(request.args["a"])
        b = int(request.args["b"])
        page += f" <p>The product is {a*b}</p>"
    except:
        pass
    
    return page

@app.route('/divide')
def divide():
    page = """
    <h1>Division<h1>
    <a href="/">Home</a>
    <br>
    <a href="/multiply">Multiplication</a>
    <form action=/divide method=get>
        <input name=a />
        <input name=b />
        <input type=submit />
    </form>
    """
    try:
        a = int(request.args["a"])
        b = int(request.args["b"])
        page += f" <p>The quotient is {a/b}</p>"
    except:
        pass
    
    return page