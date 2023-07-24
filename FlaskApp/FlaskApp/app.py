from flask import Flask, render_template


app = Flask(__name__)

@app.route("/")
def viewOne():
    return render_template('map_fire.html')

@app.route("/charts")
def viewTwo():
    return render_template('index3.html')


@app.route("/morecharts")
def viewThree():
    return render_template('linechart.html')

if __name__ == "__main__":
    app.run(host='127.0.0.1', port=8000, debug=True)