from flask import Flask, render_template
from flask import request

from block import write_block,check_integrity


app = Flask(__name__)


@app.route('/', methods=['POST', 'GET'])
def index():
    if request.method == 'POST':
        adhar_number = request.form.get('adhar_number')
        pan_number = request.form.get('pan_number')
        driving_license = request.form.get('driving_license')
        email = request.form.get('Email')
        
        write_block(adhar_number=adhar_number,pancard = pan_number,driving_license=driving_license,email = email)
        
    return render_template('detail.html')

@app.route('')
@app.route('/checking')
def check():
    results = check_integrity()
    return render_template('detail.html', checking_results = results)


if __name__ == '__main__':
    app.run(debug = True)