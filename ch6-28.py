# ch6-28.py
cars = ['Honda','bmw','Toyota','Ford','bmw']
print("目前串列內容 = ",cars)
# 直接列印[::-1]顛倒排列，不更改串列內容
print("列印使用[::-1]顛倒排序\n",cars[::-1])
#更改串列內容
print("使用reverse( )顛倒排序串列元素")
cars.reverse( )
print("新的串列內容 = ",cars)
