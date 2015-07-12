#-*- coding: utf-8 -*-
from django import template
from login.models import *

#regieter this custom template tag to template library
register = template.Library()

#template tag to get data from list at index
@register.filter(name='get_at_index')
def get_at_index(list, index):
    return list[index]

#template tag to get id from list at index
@register.filter(name='get_id_at_index')
def get_id_at_index(list, index):
    return list[index].id

#template tag to get prefix name english for student and officer
@register.filter(name='get_prefix_name_en')
def get_prefix_name_en(index):
    prefix_name_list_en = ['Mr.', 'Mrs.', 'Miss.', 'Dr.']
    return prefix_name_list_en[int(index)]

#template tag to get prefix name thai for student and officer
@register.filter(name='get_prefix_name_th')
def get_prefix_name_th(index):
    prefix_name_list_th = ['นาย', 'นาง', 'นางสาว', 'ดร.']
    return prefix_name_list_th[int(index)]

#template tag to get prefix name english for teacher
@register.filter(name='get_prefix_name_en_teacher')
def get_prefix_name_en_teacher(index_academic,index):
    academic_position = ['','Asst.Prof.', 'Assoc.Prof.', 'Prof.']
    prefix_name_list_en = ['Mr.', 'Mrs.', 'Miss.', 'Dr.']
    if int(index_academic)!=0 and int(index)==3: #check if teacher have academic position and Dr.
        return academic_position[int(index_academic)]+prefix_name_list_en[int(index)] #return academic position and Dr.
    elif int(index_academic)!=0: #if have only academic position
        return academic_position[int(index_academic)] #return only academic position
    else:
        return prefix_name_list_en[int(index)] #return only prefix name

#template tag to get prefix name thai for teacher
@register.filter(name='get_prefix_name_th_teacher')
def get_prefix_name_th_teacher(index_academic,index):
    academic_position = ['อ.','ผศ.', 'รศ.', 'ศ.']
    prefix_name_list_th = ['นาย', 'นาง', 'นางสาว', 'ดร.']
    if int(index_academic)!=0 and int(index)==3: #check if teacher have academic position and Dr.
        return academic_position[int(index_academic)]+prefix_name_list_th[int(index)] #return academic position and Dr.
    elif int(index_academic)!=0: #if have only academic position
        return academic_position[int(index_academic)] #return only academic position
    elif int(index_academic)==0 and int(index)==3: #if not have academic position but are Dr.
        return prefix_name_list_th[int(index)] #return only prefix name
    else:
        return academic_position[int(index_academic)] #return only academic position

#template tag to get size of list
@register.filter(name='get_list_size')
def get_list_size(lists):
    return len(lists)

#template tag to get prefix name thai for teacher in view notification page
@register.filter(name='get_prefix_name_th_teacher_message')
def get_prefix_name_th_teacher_message(index):
    u = UserProfile.objects.get(id=index) #get userprofile object from index
    t = Teacher.objects.get(userprofile=u) #get teacher object from userprofile
    return get_prefix_name_th_teacher(t.academic_position,u.prefix_name) #return prefix name by get_prefix_name_th_teacher
