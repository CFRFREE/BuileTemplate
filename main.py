import os
dir = r"C:\Users\FREE\Desktop\note\ACM\模板\\"
tep = os.walk(dir)
cpplist = []
for path, dir_list, file_list in tep:
	for file_name in file_list:
		if file_name[-4::] == ".cpp":
			cpplist.append(file_name)

with open(dir + "test.md", 'w') as f1:
	for file_name in cpplist:
		f1.write("### " + file_name + "\n")
		f1.write("```cpp\n")
		with open(dir + file_name, 'r', encoding='UTF-8') as f2:
			st = f2.read()
			f1.write(st)
		f1.write("\n")
		f2.close()
		f1.write("```\n\n")
f1.close()
