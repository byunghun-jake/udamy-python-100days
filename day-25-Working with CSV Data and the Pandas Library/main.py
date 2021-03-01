# with open("./weather_data.csv") as file:
#     data = file.readlines()
#     print(data)

# import csv
#
# with open("weather_data.csv") as data_file:
#     data = csv.reader(data_file)
#     # 1. 온도 정보를 temperature 배열에 저장하기
#     temperatures = []
#     for row in data:
#         if row[1] != "temp":
#             temperatures.append(int(row[1]))
#     print(temperatures)


# 3. pandas 라이브러리를 사용해보기
import pandas

data = pandas.read_csv("./weather_data.csv")
# print(type(data))
# print(data)
# print(type(data["temp"]))
# print(data["temp"])

# # 4. DataFrame을 Dict으로 변환해보자
# data_dict = data.to_dict()
# print(data_dict)
#
# # 5. Series를 list로 변환해보자
# temp_list = data["temp"].to_list()
# print(temp_list)
# # 6. 평균 온도를 구해보자
# average_temp = sum(temp_list) / len(temp_list)
# print(average_temp)
# print(data["temp"].mean())
# # 7. 온도 중 가장 큰 값을 구해보자
# print(data["temp"].max())
#
# # 8. condition 컬럼 읽기
# print(data["condition"])
# print(data.condition)

# # 9. Get Data in Row
# print(data[data.day == "Monday"])
#
# # 10. Print the row of data which had the highest temperature.
# print(data[data.temp == data.temp.max()])

# 11. Convert Monday's temperature to Fahrenheit
# monday = data[data.day == "Monday"]
# print((monday.temp * 9 / 5) + 32)

# # 12. Create a dataframe from scratch
# data_dict = {
#     "students": ["Amy", "James", "Angela"],
#     "scores": [76, 56, 65]
# }
# data = pandas.DataFrame(data_dict)
# data.to_csv("./new_data.csv")


# Challenge
data = pandas.read_csv("./2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")
fur_gray = data[data["Primary Fur Color"] == "Gray"]
gray_count = len(fur_gray)

fur_cinnamon = data[data["Primary Fur Color"] == "Cinnamon"]
cinnamon_count = len(fur_cinnamon)

fur_black = data[data["Primary Fur Color"] == "Black"]
black_count = len(fur_black)

data_dict = {
    "Fur Color": ["gray", "red", "black"],
    "Count": [gray_count, cinnamon_count, black_count]
}

new_data = pandas.DataFrame(data_dict)
new_data.to_csv("./squirrel_count")
























