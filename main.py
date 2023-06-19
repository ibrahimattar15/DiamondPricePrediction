from flask import Flask,render_template,request
from utils import DiamondPricePrediction

app = Flask(__name__)
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/diamond/price/prediction',methods= ['GET','POST'])
def diamond_price():
    if request.method=='POST':
        data = request.form.get
        carat = eval(data('carat'))
        cut = data('cut')
        color = data('color')
        clarity = data('clarity')
        depth = eval(data('depth'))
        table = eval(data('table'))
        x = eval(data('x'))
        y = eval(data('y'))
        z = eval(data('z'))
        model = DiamondPricePrediction(carat,cut,color,clarity,depth,table,x,y,z)
        predict = model.price_prediction()
        return render_template('index.html',prediction=predict)

if __name__ == '__main__':
    app.run(debug=True,host='0.0.0.0',port=5007)

