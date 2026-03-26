import re
import os
with open('decode3_8.v','r') as file1:
	a = file1.read();
inp = re.findall(r'(?<=input\s).*(?=[;])',a)
print(inp)
in1 = re.findall(r'(?<=input\s\[[0-9]:[0-9]\])[A-Z,a-z]+(?=[;])',a)
print(in1)
out1 = re.findall(r'(?<=output\s\[[0-9]:[0-9]\])[A-Z,a-z]+(?=[;])',a)
print(out1)
out = re.findall(r'(?<=output\s).*(?=[;])',a)
print(out)
mod = re.findall(r'(?<=module\s).*(?=[(])',a)
tb_name = "tb_"+mod[0] +".v"
mod1 = "tb_"+mod[0]
print(tb_name)
with open(tb_name,'a+') as file2:
	file2.write("module ")
	file2.write(mod1)
	file2.write(";")
	for i in inp:
		file2.write("\n\t")
		file2.write("reg ")
		file2.write(i)
		file2.write(";")
	for i in out:
		file2.write("\n\t")
		file2.write("wire ")
		file2.write(i)
		file2.write(";")
#---------------------instiating the module ----------------
	file2.write("\n\t")
	file2.write(mod[0])
	file2.write(" U1")
	file2.write("(")
	for i in in1:
		file2.write(".")
		file2.write(i)
		file2.write("(")
		file2.write(i)
		file2.write("),")
	for i in out1:
		file2.write(".")
		file2.write(i)
		file2.write("(")
		file2.write(i)
		if( i != out1[len(out1)-1]):
			file2.write("),")
		else:
			file2.write("));")

#--------------------initial block for user enterance---------	
	file2.write("\n")
	file2.write("\t")
	file2.write("initial begin")
	file2.write('\n')
	file2.write('\n')
	file2.write('\t')
	file2.write("end")
	file2.write("\n\t")
#------------------initial block for simvision------------
	file2.write("initial begin")
	file2.write("\n")
	file2.write("\t\t")
	file2.write('$recordfile("')
	file2.write(mod[0])
	file2.write('.trn");')
	file2.write('\n')
	file2.write('\t\t')
	file2.write("$recordvars();")
	file2.write("\n")
	file2.write('\t\t')
	file2.write("#150;")
	file2.write("\n")
	file2.write("\t\t")
	file2.write("$finish;")
	file2.write("\n")
	file2.write("\t")
	file2.write("end")
	file2.write("\n")
	file2.write("endmodule")

