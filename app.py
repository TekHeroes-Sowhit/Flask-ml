
from flask import Flask,render_template,request
from joblib import load
import numpy as np
import pandas as pd
app=Flask(__name__)

app=Flask(__name__)

# @app.route('/')
# def hello_world():
#     test_np_input=np.array([[1],[2],[3]])
#     model=load('model.joblib')
#     preds=model.predict(test_np_input)
#     preds_as_str=str(preds)
#     return preds_as_str
@app.route('/',methods=["GET","POST"])
def hello():
    if request.method=="GET":
         return render_template('index.html',href='static/simple.png')
    else:
        text=request.form['text']
        path="predictions_pic.svg"
        model=load('model.joblib')
        np_arr=float_string_to_np_arr(text)
        make_picture('AgesAndHeights.pkl',model,np_arr,path)
        return  render_template('index.html',href=path)

# https://www.youtube.com/watch?v=qNF1HqBvpGE

def make_picture(training_data_filename,moedl,new_inp_np_arr,output_file):
    data=pd.read_pickle()
    age=data['age']
    data=data[age>0]
    heights=data['Height']
    x_new=np.array(list(range(19))).reshape(19,1)
    preds=model.predict(x_new)
    fig=px.scatter(x=age,y=height,labels={'x':'Age','y':'Height'})
    fig.add_trace(go.Scatter(x=x_new.reshape(19),y=preds,mode='lines',nane='model'))
    new_prds=model.predict(new_input_arr.reshape(len(new_input_arr)),y=new_preds,name='output')
    fig.write_image(output_file)
    fig.show()
def  float_string_to_np_arr(floats_str):
    def is_float(s):
        try:
            float(s)
            return True
        except:
            return False
    floats=np.array([float(x) for x in floats_str.split(',')if is_float(x)])
    return floats.reshape(len(floats),1)




app.run()
