from random import choice

#将学生姓名赋值给students_names这个变量
students_names = 'students_names.txt'

#将已抽到的学生姓名储存到列表pass_students_names
pass_students_names = []

#将学生姓名储存在一个空列表中
with open(students_names) as s_n:
	lines = s_n.readlines()

#随机抽取一个幸运学生，打印其名字
while True:
	user_answer = input("您想继续吗？【y/n】")
	if user_answer == "y":
		luckly_student = choice(lines)
		if luckly_student in pass_students_names:
			continue
		else:
			print(f"幸运学生：{luckly_student}")
			pass_students_names.append(luckly_student)
	elif user_answer == "n":
		print("感谢您的使用！")
		break
	else:
		print("请输入正确的选项！")
