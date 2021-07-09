import csv
# 表头
field_order = ["姓名", '年龄', '性别']
with open("src/main/java/com/ner/demo/txts/test.csv", 'w', encoding="utf-8", newline='') as csvfile:
    writer = csv.DictWriter(csvfile, field_order)
    writer.writeheader()
    writer.writerow(dict(zip(field_order, ["张三", 20, "男"])))
    writer.writerow(dict(zip(field_order, ["李四", 10, "男"])))
    writer.writerow(dict(zip(field_order, ["王五", 30, "男"])))