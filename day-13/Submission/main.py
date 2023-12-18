from flask import Flask, jsonify  

app = Flask(__name__)

csv_file = 'programming_languages.csv'

def read_csv():
    pass

@app.route('/', methods=['GET'])
def get_langs():
    pass

if __name__ == '__main__':
    app.run(debug=True)