#-*- coding: utf-8 -*-
from django import template

register = template.Library()

@register.filter(name='get_at_index')
def get_at_index(list, index):
    return list[index]

@register.filter(name='get_id_at_index')
def get_id_at_index(list, index):
    return list[index].id

@register.filter(name='get_prefix_name_en')
def get_prefix_name_en(index):
    prefix_name_list_en = ['Mr.', 'Mrs.', 'Miss.', 'Dr.']
    return prefix_name_list_en[int(index)]

@register.filter(name='get_prefix_name_th')
def get_prefix_name_th(index):
    prefix_name_list_th = ['นาย', 'นาง', 'นางสาว', 'ดร.']
    return prefix_name_list_th[int(index)]

@register.filter(name='get_prefix_name_en_teacher')
def get_prefix_name_en_teacher(index_academic,index):
    academic_position = ['','Asst.Prof.', 'Assoc.Prof.', 'Prof.']
    prefix_name_list_en = ['Mr.', 'Mrs.', 'Miss.', 'Dr.']
    if int(index_academic)!=0 and int(index)==3:
        return academic_position[int(index_academic)]+prefix_name_list_en[int(index)]
    elif int(index_academic)!=0:
        return academic_position[int(index_academic)]
    else:
        return prefix_name_list_en[int(index)]

@register.filter(name='get_prefix_name_th_teacher')
def get_prefix_name_th_teacher(index_academic,index):
    academic_position = ['อ.','ผศ.', 'รศ.', 'ศ.']
    prefix_name_list_th = ['นาย', 'นาง', 'นางสาว', 'ดร.']
    if int(index_academic)!=0 and int(index)==3:
        return academic_position[int(index_academic)]+prefix_name_list_th[int(index)]
    elif int(index_academic)!=0:
        return academic_position[int(index_academic)]
    elif int(index_academic)==0 and int(index)==3:
        return prefix_name_list_th[int(index)]
    else:
        return academic_position[int(index_academic)]
