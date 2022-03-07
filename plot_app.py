from flask import Flask, send_file
from plot import plot_graph
app = Flask(__name__)

@app.route('/plots', methods=['GET'])
def result():
    bytes_obj = plot_graph()
    
    return send_file(bytes_obj,
                     attachment_filename='plot.png',
                     mimetype='image/png')

if __name__ == '__main__':
    app.run(debug=True,port=5000)