# ch6-27.py
cars = ['Honda','bmw','Toyota','Ford','bmw']
print("目前串列內容 = ",cars)
print("使用remove( )刪除串列元素")
expensive = 'bmw'
cars.remove(expensive)
print(f"所刪除的內容是：{expensive.upper()}因為太貴了")
print("目前串列內容 = ",cars)
