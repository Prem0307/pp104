from collections import Counter
import csv


def get_mean(total_weight,total_entries):
    mean=total_weight/total_entries
    print("mean is "+str(mean))

def get_median(total_entries,s_data):
    if total_entries % 2 == 0:
        med1=float(s_data[total_entries//2])
        med2=float(s_data[total_entries//2-1])
        median= (med1 + med2)/2
    else:
        median=float(s_data[total_entries//2])
    
    print("median is {median:2f}")


def get_mode(s_data):
    data=Counter(new_data)
    mode_datafor_range  = {
                            "75-85":0,
                            "85-95":0,
                            "95-105":0,
                            "105-115":0,
                            "115-125":0,
                            "125-135":0,
                            "135-145":0,
                            "145-155":0,
                            "155-165":0,
                            "165-175":0
                          }
    for weight,occur in data.items():
        if 75 < weight < 85:
            mode_datafor_range["75-85"] += occur
        elif 85 < weight < 95:
            mode_datafor_range["85-95"] += occur
        elif 95 < weight < 105:
            mode_datafor_range["95-105"] += occur
        elif 105 < weight < 115:
            mode_datafor_range["105-115"] += occur
        elif 115 < weight < 125:
            mode_datafor_range["115-125"] += occur
        elif 125 < weight < 135:
            mode_datafor_range["125-135"] += occur
        elif 135 < weight < 145:
            mode_datafor_range["135-145"] += occur
        elif 145 < weight < 155:
            mode_datafor_range["145-155"] += occur
        elif 155 < weight < 165:
            mode_datafor_range["155-165"] += occur
        elif 165 < weight < 175:
            mode_datafor_range["165-175"] += occur
    mode_range,mode_occur=0,0

    for range,occur in mode_datafor_range.items():
     if occur > mode_occur:
         mode_range,mode_occur=[int(range.split('-')[0]),int(range.split('-')[1])],occur
    mode=float((mode_range[0]+mode_range[1])/2)
    print(f'mode is -> {mode:2f}') 

  

with open('SOCR-HeightWeight.csv',newline='') as f:
    reader=csv.reader(f)
    file_data= list(reader)

file_data.pop(0)

total_weight=0,
total_entries=len(file_data)
s_data=[]

for perdata in file_data:
    total_weight = float(perdata[1])
    s_data.append(float(perdata[1]))

s_data.sort()

get_mean(total_weight,total_entries)
get_median(total_weight,total_entries)
get_mode(s_data)

   

   



