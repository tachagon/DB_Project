#-*-coding: utf-8 -*-
#!/usr/local/bin/python

import bs4
import requests
from bs4 import NavigableString
def arrUnicode(myArr):
    uniStr = [unicode(i, encoding='utf-8') if isinstance(i, basestring) else i for i in myArr]
    s = repr(uniStr).decode('unicode_escape').encode('utf-8')
    if s.startswith("[u'"):
        s2 = s.replace("u'", "'")
    elif s.startswith('[u"'):
        s2 = s.replace('u"', '"')
    else:
        return s
    return s2

html = requests.get("http://www.finance.oop.kmutnb.ac.th/old/index.php?option=com_content&view=category&id=7:2010-07-05-08-41-28&Itemid=30&layout=default").text
b = bs4.BeautifulSoup(html)
m = b.find(id='art-main')
#odd = m.findAll("tr",{ "class" : "sectiontableentry1" })
odd  = m.findAll("a")
even = m.findAll("tr",{ "class" : "sectiontableentry2" })
count= 0
count2 = 0
end = 0
start =0
old_list = ["โอนเข้าบัญชีวันที่ 29 มิถุนายน 2558 (ราชการ)",
            "โอนเข้าบัญชีวันที่ 2 มิถุนายน 2558 (พนักงานมหาวิทยาลัย)",
    	    "โอนเข้าบัญชีวันที่ 23 มิถุนายน 25558 (ราชการ)",
            "โอนเข้าบัญชีวันที่ 23 มิถุนาบย 2558 (พนักงานมหาวิทยาลัย)",
            "โอนเข้าบัญชีวันที่ 23 มิถุนายน 2558 (พนักงานมหาวิทยาลัย)",
            "โอนเข้าบัญชีวันที่ 19 มิถุนายน 2558 (ราชการ)"]
list_name = []
name_list = []
ser_list = []
cost_list = []
accnum_list = []
list_ = []
url_list = []
odd = odd[34:-4]

####################################################################

for row in range(0,6):
    url = "http://www.finance.oop.kmutnb.ac.th"
    temp = str(odd[row])
    for index in range(0,len(temp)):
        link = temp.find('<a href="')
        if temp[index] == '>' :
            start = index
            count2 +=  1
        elif temp[index] == '<' :
            end = index
            count += 1
        if count2 == 1:
            test = temp[link+9:start-1]
            count2 = 0
        if count == 2:
            cut = temp[start+1:end]
            break
    url_list.append(url+test)
    cut = cut[4:]
    list_name.append(cut)
    #kind = temp[startcut+1:endcut]
    count = 0  # reset count
####################################################################
num = 0
new_url = []
temp_list = []
index2 = 0
for j in range(0,len(old_list)):
    if old_list[j] != list_name[j]:
	if j == 0 :
	    new_url.append(url_list[j])
	    num  += 1
	else:
	    if old_list[j-1] == list_name[j]:
		break
	    else:
		new_url.append(url_list[j])
		num  += 1
    else:
	print 'No change',j
for n in range(0,len(old_list)):
    old_list[n] = list_name[n]
####################################################################

    update_list = [0 for x in range(num)]
for k in range(0,num):
    urls = str(new_url[k])
    html = requests.get(urls).text
    ##if has update
    b = bs4.BeautifulSoup(html)
    m = b.find(id='art-main')
    qq = m.findAll("strong")
    count= 0
    count2 = 0
    end = 0
    start =0
    pos = 0

    for row in range(0,len(qq)):
        temp = str(qq[row])
        for index in range(0,len(temp)):
        	if temp[index] == '>' :
        	    start = index
        	elif temp[index] == '<' :
        	    end = index
        	    count += 1
        	if count == 3 :
        	    cut = temp[start+1:end]
        	    if len(cut) != 0:
        	        break
        	    else: pass
	        elif count == 4:
	    	    cut = temp[start+1:end]
        	    if len(cut) != 0 :
        	        break
	            else:
	                pass
	        elif count == 6:
	            cut = temp[start+1:end]
		    if len(cut) != 0:
                        break
                    else: pass
	if len(cut) >= 18:
	    if cut.find("นาย") == 0:
	        cut = cut[9:len(cut)]
	    elif cut.find("นาง") == 0 and cut.find("สาว") != 9:
	        cut = cut[9:len(cut)]
	    elif cut.find("นางสาว") == 0:
	        cut = cut[18:len(cut)]
	        #print cut
	#print cut
	if len(cut) != 1 and len(cut) != 2: #except numeric and blank
	    pos += 1

	    if pos == 1:
	        name_list.append(cut)
		index2 += 1
	    elif pos == 2:
	        ser_list.append(cut)
	    elif pos == 3:
	        cost_list.append(cut)
	    else:
	        accnum_list.append(cut)
	        pos = 0
	count = 0  # reset count
    update_list[k] = index2
    index2 = 0
#print arrUnicode(name_list)

print update_list
#print list_[1]

