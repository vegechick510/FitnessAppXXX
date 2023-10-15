from apps import App
app = App()
mongo = app.mongo


def insertfooddata():
    f = open('food_data/calories.csv', 'r', encoding = "ISO-8859-1")
    l = f.readlines()

    for i in range(1, len(l)):
        l[i] = l[i][1:len(l[i]) - 2]

    for i in range(1, len(l)):
        temp = l[i].split(",")
        mongo.db.food.update_one({'food': temp[0]},{'$set': {'calories': temp[1]}},upsert=True)
