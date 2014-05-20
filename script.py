# -*- coding: utf-8 -*-
import numpy as np
import scipy as sc
import random
#тут введи количество своих альтернатив
alt=8
print "Количество альтернатив: %s" %alt
#тут введи количество критериев, по которым будут выбираться альтернативы
krit=12
print "Количество критериев: %s" %krit
#тут задаются весовые коэффициенты для построения отношения Q2
w=np.array([0.12,0.16,0.09,0.08,0.04,0.09,0.04,0.07,0.07,0.11,0.08,0.05])
print "Весовые коэффициенты следующие: %s" %w
#это функция для вычисления одного нечеткого отношения
def array_matrix_alone():
	#это задается единичная матрица
	c = np.ones((alt,alt), dtype=np.int)
	
	for i in range(alt):
		for j in range(alt):
			if i!=j:
				#тут на некоторые позиции ставятся нули вместо единиц, кроме главной диагонали
				c[i][j]*=random.randint(0,1)
				if c[i][j]==c[j][i]==0: c[j][i]=1
				elif c[i][j]==c[j][i]==1: c[j][i]=0
	return c
#это функция для вычисления списка матриц нечеткого отношения исходя из критериев	
def array_matrix():
	global arr
	global fuzzy_set
	arr = [array_matrix_alone() for x in range(krit)]
	for a in range(len(arr)):
		print "Матрица нечетких отношений предпочтения R%d" %(a+1)
		print arr[a]
	b=[]
	for i in range(alt):
		for j in range(alt):
			for k in range(krit):
				b.append(arr[k][i][j])
	print "Нечеткое отношение имеет вид:"
	fuzzy_set = np.reshape(np.min(np.reshape(b,(alt*alt,krit)),axis=1),(alt,alt))
	print fuzzy_set
		
def non_dominated_alternatives(array_list, name_set, up):
	global x
	c = []
	for i in range(alt):
		for j in range(alt):
			c.append(array_list[j][i]-array_list[i][j])
#раскомментить блок, чтобы увидеть промежуточные действия
#тут считается подмножество недоминируемых альтернатив по формуле
#mu(ai)=1-sup(mu(aj,ai)-mu(ai,aj))
	#print c
	#print np.reshape(c,(alt,alt))
	#print "-"*20
	#print np.max(np.reshape(c,(alt,alt)),axis=1)
	x = [1]*alt-np.max(np.reshape(c,(alt,alt)),axis=1)
	if up == True: 
		print "Подмножество недоминируемых альтернатив множества %s имеет вид:" %name_set
		print x
	return x
def fuzzy_set_Q2():
	global plus
	plus = np.zeros((alt,alt))
	for i in range(krit):
		plus += w[i]*arr[i]
	print "Отношение Q2 имеет вид:"
	print plus
	return plus
	
def result():
	res=[]
	for i in zip(non_dominated_alternatives(fuzzy_set, "Q1", False),non_dominated_alternatives(plus, "Q1", False)): 
		res.append("{0:.2f}".format(min(i)))
	print "Результирующее множество недоминируемых альтернатив:" 
	print res
	print "Выбираем альтернативу %s, имеющую максимальную степень недоминируемости %s" %(res.index(max(res))+1, max(res))
	
if __name__=='__main__':
	array_matrix()
	non_dominated_alternatives(fuzzy_set, "Q1", True)
	fuzzy_set_Q2()
	non_dominated_alternatives(plus, "Q2", True)
	result()
	
	
	
	
	    
	
	
