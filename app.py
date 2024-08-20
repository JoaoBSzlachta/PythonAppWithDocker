from flask import Flask, Response
import matplotlib.pyplot as plt
import numpy as np
from io import BytesIO

app = Flask(__name__)
@app.route("/")
def grafico():
    x = [1, 2, 3, 4, 5]
    y = [2, 4, 8, 16, 32]

    plt.figure()
    plt.plot(x,y)
    
    img = BytesIO()
    plt.savefig(img, format='png')
    img.seek(0)
    return Response(img, mimetype='image/png')

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
