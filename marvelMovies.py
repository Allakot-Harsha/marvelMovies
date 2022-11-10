import json
import operator
with open('data.json') as f:
    data=json.load(f)
my_dict={}
#print(str(data[1]))
for movies in data:
    for actors in movies['stars']:
        star = movies['stars']
    star= star.split(',')
    #counting each stars name in data
    #print(star[1])
    for each in star:
        each=each.lstrip()  #to remove whitespace from name
        each=each.rstrip()
        if each in my_dict:
            key=my_dict[each]
            value=my_dict[each]+1
            my_dict[each]=value
        else:
            my_dict[each]=1
#sorted_dict=sorted(my_dict.values())
my_dict1={k: v for k, v in my_dict.items() if v>=2}
sorted_d = sorted(my_dict1.items(), key=operator.itemgetter(1))
#for each in sorted_d:
    #print(each[1])


    #print("Star Name:", each[0], "\t\t\t|Movies:", each[1])
avg_dict={}
for i in sorted_d:
    #print(i[0])
    sum = 0
    for movies in data:
        for actors in movies['stars']:
            star = movies['stars']
        star = star.split(',')

        # print(star[1])
        for each in star:

            each = each.lstrip()
            each = each.rstrip()
            rate=0

            if each==i[0]:
                sum=sum+float(movies['rating'])
                #rate=float(movies['rating'])
                rate = round(sum/my_dict1[each],2) #calculating average of the movie ratings
                avg_dict[each]=rate
#print(avg_dict)
for each in sorted_d:
    #print(each[1])
    print("Star Name:", each[0], "\t\t\t|Movies:", each[1],"\t\tAVG Rating:",avg_dict[each[0]])

