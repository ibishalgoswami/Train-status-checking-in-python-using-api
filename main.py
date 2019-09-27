#https://indianrailapi.com/dashboard/api-key(Get your api key from here)
import requests
import re

print("Press 1 to know the live Station Status \nPress 2 to know the Train between stations")
choice=int(input('Enter your  choice here 1 or 2 -->'))

if choice == 1:
    stationName = input('Provide the Station code here to know about the current station status-->')
    stationName = stationName.strip()

    url = f'https://indianrailapi.com/api/v2/LiveStation/apikey/yourApiKey/StationCode/{stationName}/Hours/4'
    res = requests.get(url)
    data = res.json()
    if data['ResponseCode'] == '201':
        print("Railway Server is busy,Please try again after some time")
    if data['ResponseCode'] == '200':
        con = data['Message']
        con = re.findall(r'\d+', con)
        for i in con:
            print(i)
        noOfTrains = int(i)
        count = 0
        while noOfTrains != 0:
            for j in range(0, noOfTrains):
                Num = data['Trains'][j]['Number']
                Name = data['Trains'][j]['Name']
                ScheduleArrival = data['Trains'][j]['ScheduleArrival']
                ScheduleDeparture = data['Trains'][j]['ScheduleDeparture']
                print(f"Train : {Name} , Train Number : {Num} , ScheduleArrival time : {ScheduleArrival} , ScheduleDeparture time : {ScheduleDeparture}")
            count = count + 1
            if noOfTrains > count:
                break

elif choice == 2:

    src = input('Enter your source station code')
    dst = input('Enter your destination station code')

    url = f'https://indianrailapi.com/api/v2/TrainBetweenStation/apikey/yourApiKey/From/{src}/To/{dst}'
    res = requests.get(url)
    data = res.json()
    if data['ResponseCode'] == '201':
        print("Railway Server is busy,Please try again after some time")
    if data['ResponseCode'] == '200':
        con = data['TotalTrains']
        con = re.findall(r'\d+', con)
        for i in con:
            print(f"Total No Of Trains : {i}\n")
        noOfTrains = int(i)
        count = 0
        while noOfTrains != 0:
            for j in range(0, noOfTrains):
                TrainNo = data['Trains'][j]['TrainNo']
                TrainName = data['Trains'][j]['TrainName']
                Source = data['Trains'][j]['Source']
                DepartureTime = data['Trains'][j]['DepartureTime']
                Destination = data['Trains'][j]['Destination']
                ArrivalTime = data['Trains'][j]['ArrivalTime']
                print(
                    f"Train : {TrainName} , Train Number : {TrainNo} , Source : {Source} , Departure Time : {DepartureTime} , Destination : {Destination} , ArrivalTime : {ArrivalTime} ")
            count = count + 1
            if noOfTrains > count:
                break