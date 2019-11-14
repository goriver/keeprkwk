data = ["조회수: 1,500", "조회수: 1,002", "조회수: 300", "조회수: 251",
        "조회수: 13,432", "조회수: 998"]
sum = 0

# lv 1
for i in data:
        print(i)

# lv 2
for i in data:
        print(i[5:])

print()
# lv 3
for i in data:
        hit=i[5:]
        print(hit)
        hit = hit.replace(',',"")
        sum+=int(hit)

print("총 합 : "+str(sum))