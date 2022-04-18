from django.http import HttpRequest, HttpResponse
from django.shortcuts import render
from .data_preprocess import pre_data_cols, shape_pre_data,data_cols,data_shape
from CropAPP.models import Data
from datetime import datetime
print('Loading the dataset.....')
print('Columns in the dataset are: ',data_shape)
print("Performing data-cleaning and saving data into a new file....")
#print('Columns in the dataset after cleaning are: ',pre_data_cols)
print("Shape of the new dataset: ",shape_pre_data)
# Create your views here.

def index(request):
    return render(request,'index.html')
    
def input_data(request):
    if(request.method=="POST"):
        state=request.POST.get("country-state")
        print("Entered state is:=======",state)

        area =request.POST.get("crop-area")
        print("Entered Area is:====== ",area)

        season = request.POST.get("crop-season")
        print("Entered Season is:======",season)

        crop_name =  request.POST.get("crop")
        print("Entered crop name is:=======",crop_name)

        now = datetime.now()
        current_time = now.strftime("%H:%M:%S")
        a= Data(created_on=current_time,state=state,area=area,season=season,crop_name=crop_name)
        a.save()
        print("^^^^^^^^^^^Saved===== ",a)
    return render(request, 'index.html')