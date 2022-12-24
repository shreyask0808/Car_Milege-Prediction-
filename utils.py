import numpy as np
import pickle
import json
# import config 
class CarMilege():
    def __init__(self,cyl,disp,hp,wt,acc,yr,car_type,origin):
        self.cyl=cyl
        self.disp=disp
        self.hp=hp
        self.wt=wt
        self.acc=acc
        self.yr=yr
        self.car_type=car_type
        self.origin='origin_'+origin

    def load_model(self):
        with open('linear_Model.pkl','rb')as f:
            self.model=pickle.load(f)
        
        with open('project_data.json','r')as f:
            self.json_data=json.load(f)    
        

    def get_predicted_mileges(self):
        self.load_model()
        origin_index=self.json_data['columns'].index(self.origin)

        test_array=np.zeros(len(self.json_data['columns']))
    
        test_array[0]= self.cyl
        test_array[1]= self.disp
        test_array[2]= self.hp
        test_array[3]= self.wt
        test_array[4]= self.acc
        test_array[5]= self.yr
        test_array[6]= self.car_type
        test_array[origin_index]=1


        print("Test Array: ",test_array)
        predicted_milege=np.around(self.model.predict([test_array])[0],2)
        print(predicted_milege)
        return predicted_milege

if __name__=="__main__":
    cyl= 4
    disp= 107
    hp= 90
    wt= 2430
    acc= 14.5
    yr= 70
    car_type= 1
    origin= 'europe'
    car_mpg=CarMilege(cyl,disp, hp, wt, acc, yr, car_type,origin)
    car_mpg.get_predicted_mileges()