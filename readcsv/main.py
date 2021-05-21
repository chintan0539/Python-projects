# # with open("./weather_data.csv") as file:
# #     temp=file.readlines()
# # data=[]
# # for t in temp:
# #     data.append(t.strip())
# # print(data)
#
# # import csv
# #
# # with open("./weather_data.csv") as file:
# #     data=csv.reader(file)
# #     temp=[]
# #     for row in data:
# #         if row[1] == 'temp':
# #             continue
# #
# #         t=int(row[1])
# #         temp.append(t)
# #     print(temp)
#
# import pandas
#
# data=pandas.read_csv("./weather_data.csv")
#
# print(data["temp"].max())
# temp_list=data["temp"].to_list()
# print(round(sum(temp_list)/len(temp_list),2))



import pandas

data=pandas.read_csv("./2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")

grey_squ_count=len(data[data["Primary Fur Color"]=='Gray'])
black_squ_count=len(data[data["Primary Fur Color"]=='Black'])
cinnamon_squ_count=len(data[data["Primary Fur Color"]=='Cinnamon'])


data_dict={
    "Fur Color":["Gray","Black","Cinnamon"],
    "Count":[grey_squ_count,black_squ_count,cinnamon_squ_count]
}
df=pandas.DataFrame(data_dict)
df.to_csv("squ_count.csv")