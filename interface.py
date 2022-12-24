from flask import Flask,request,jsonify
from utils import CarMilege


app=Flask(__name__)

@app.route('/')

def hello_flask():
    print('Welcome to check the car milege')
    return 'Hello'

@app.route('/predict_milege')
def get_predicted_mil():
    
    
    data=request.form #to get data from users
    print("DATA is: ",data)
    cyl=float(data['cyl'])
    disp=float(data['disp'])
    hp=float(data['hp'])
    wt= float(data['wt'])
    acc= float(data['acc'])
    yr= float(data['yr'])
    car_type= float(data['car_type'])
    
    origin=data['origin']
    car_mpg=CarMilege(cyl,disp, hp, wt, acc, yr, car_type,origin)
    milege=car_mpg.get_predicted_mileges()

    return jsonify({"MSG":f"Predicted Car Milege is {milege}"})
    # return jsonify({"MSG":"SUCCESS"})


if __name__ == '__main__':
    app.run(debug=True)