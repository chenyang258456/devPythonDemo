from collections import namedtuple

Student = namedtuple('Student', ['name', 'age', 'sex'])
s = Student('小明', '18', '男')
print(s.name)

list_demo = [f'data{i}' for i in range(0, 101) if i % 2 == 0]
print(list_demo)

cookie_str = 'BAIDUID=dadasdasd;PSTM=dasdasdas'
cookie_dict = {item.split('=')[0]: item.split('=')[1] for item in cookie_str.split(';')}
print(cookie_dict)

for k in zip({"name":"chen"},{"age":18}):
    print(k)



