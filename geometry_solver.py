#
#   Geometry Solver
#

lines = ['ls1','ls2','ls3','ls4','ls5','ls6','ls7','ls8','ls9','ls10','ls11','ls12']
arcs = ['as1','as2','as3','as4','as5','as6','as7']
areas = ['ar1','ar2','ar3','ar4','ar5','ar6','ar7','ar8','ar9']
angles = ['a1','a2','a3','a4','a5','a6','a7','a8','a9','b1','b2','b3','b4','b5','b6','c1','c2','c3','c4','c5','c6','d1','d2','d3','d4','d5','d6']

dictionary = {}
class null:
    flag = False

def add_to_dictionary(key, name1, name2, value='NULL'):
    dictionary.setdefault(key,[])
    newList = dictionary[key]
    if(key == 'fraction' or key == 'sum_value'):
        newList.append([name1,name2,value])
    else:
        newList.append([name1,name2])
    dictionary[key] = newList

def check_dictionary(key, name1, name2, value='NULL'):
    dictionary.setdefault(key,[])
    if(value == 'NULL'):
        return [name1,name2] in dictionary[key] or [name2,name1] in dictionary[key]
    if(key == 'sum_value'):
        return [name1,name2,value] in dictionary[key] or [name2,name1,value] in dictionary[key]
    return [name1,name2,value] in dictionary[key]
    
#Predicates

def set_parallel(name1, name2):
    add_to_dictionary('parallel', name1, name2)
    
    if(name1 in ['ls1','ls2','ls3','ls10']):
        if(name2 in ['ls1','ls2','ls3','ls10']):
            return
        else:
            #NULL
            null.flag = True
            return
    elif(name1 in ['ls4','ls5','ls6','ls11']):
        if(name2 in ['ls4','ls5','ls6','ls11']):
            return
        else:
            #NULL
            null.flag = True
            return
    elif(name1 in ['ls7','ls8','ls9','ls12','ls4','ls5','ls6','ls11']):
        if(name2 in ['ls7','ls8','ls9','ls12']):
            #do nothing
            return
        else:
            #NULL
            null.flag = True
            return
    else:
        #NULL
        return
    return

def set_perpendicular(name1, name2):
    add_to_dictionary('perpendicular', name1, name2)

    if(name1 in ['ls1','ls2','ls3','ls10']):
        if(name2 in ['ls1','ls2','ls3','ls10']):
            #NULL
            null.flag = True
            return
        elif(name2 in ['ls4','ls5','ls6','ls11']):
            know_call(name1,name2)
            return
        elif(name2 in ['ls7','ls8','ls9','ls12']):
            know_call(name1,name2)
            return
        else:
            #NULL
            null.flag = True
            return
    elif(name1 in ['ls4','ls5','ls6','ls11']):
        if(name2 in ['ls1','ls2','ls3','ls10']):
            know_call(name1,name2)
            return
        elif(name2 in ['ls4','ls5','ls6','ls11']):
            #NULL
            null.flag = True
            return
        elif(name2 in ['ls7','ls8','ls9','ls12']):
            know_call(name1,name2)
            return
        else:
            #NULL
            null.flag = True
            return
    elif(name1 in ['ls7','ls8','ls9','ls12']):
        if(name2 in ['ls1','ls2','ls3','ls10']):
            know_call(name1,name2)
            return
        elif(name2 in ['ls4','ls5','ls6','ls11']):
            know_call(name1,name2)
            return
        else:
            #NULL
            null.flag = True
            return
    return

def set_equal(name1, name2):
    add_to_dictionary('equal', name1, name2)
    if(name1 == 'ls1'):
        if(name2 == 'ls9'):
            know_call(name1,name2)
            return
    elif(name1 == 'ls2'):
        if(name2 == 'ls5'):
            know_call(name1,name2)
            return
        if(name2 == 'ls8'):
            know_call(name1,name2)
            return
    elif(name1 == 'ls3'):
        if(name2 == 'ls4'):
            know_call(name1,name2)
            return
        return
    elif(name1 == 'ls4'):
        if(name2 == 'ls3'):
            know_call(name1,name2)
            return
        return
    elif(name1 == 'ls5'):
        if(name2 == 'ls2'):
            know_call(name1,name2)
            return
        if(name2 == 'ls8'):
            know_call(name1,name2)
            return
        return
    elif(name1 == 'ls6'):
        if(name2 == 'ls7'):
            know_call(name1,name2)
            return
        return
    elif(name1 == 'ls7'):
        if(name2 == 'ls6'):
            know_call(name1,name2)
            return
        return
    elif(name1 == 'ls8'):
        if(name2 == 'ls2'):
            know_call(name1,name2)
            return
        if(name2 == 'ls5'):
            know_call(name1,name2)
            return
        return
    elif(name1 == 'ls9'):
        if(name2 == 'ls1'):
            know_call(name1,name2)
            return
        return
    elif(name1 == 'ls10'):
        if(name2 == 'ls11'):
            know_call(name1,name2)
            return
        if(name2 == 'ls12'):
            know_call(name1,name2)
            return
        return
    elif(name1 == 'ls11'):
        if(name2 == 'ls10'):
            know_call(name1,name2)
            return
        if(name2 == 'ls12'):
            know_call(name1,name2)
            return
        return
    elif(name1 == 'ls12'):
        if(name2 == 'ls10'):
            know_call(name1,name2)
            return
        if(name2 == 'ls11'):
            know_call(name1,name2)
            return
        return
    #ARCS
    elif(name1 == 'as1'):
        return
    elif(name1 == 'as2'):
        if(name2 == 'as4'):
            know_call(name1,name2)
            return
        if(name2 == 'as6'):
            know_call(name1,name2)
            return
        return
    elif(name1 == 'as3'):
        return
    elif(name1 == 'as4'):
        if(name2 == 'as2'):
            know_call(name1,name2)
            return
        if(name2 == 'as6'):
            know_call(name1,name2)
            return
        return
    elif(name1 == 'as5'):
        know_call(name1,name2)
        return
    elif(name1 == 'as6'):
        if(name2 == 'as2'):
            know_call(name1,name2)
            return
        if(name2 == 'as4'):
            know_call(name1,name2)
            return
        return
    elif(name1 == 'as7'):
        #NULL
        null.flag = True
        return
    #AREAS
    elif(name1 in ['ar8','ar9'] or name2 in ['ar8','ar9']):
        if(name1 != name2 and name1 in ['ar8','ar9'] and name2 in ['ar8','ar9']):
            know_call(name1,name2)
            return
        null.flag = True
        return
    elif(name1 in areas and name2 in areas):
        know_call(name1,name2)
    #ANGLES
    elif(name1 in angles and name2 in angles):
        know_call(name1,name2)
    else:
        null.flag = True
        return

def set_fraction(name1, name2, fraction):
    add_to_dictionary('fraction', name1, name2,fraction)
    know_call(name1,name2)
    return

def set_sum_value(name1, name2, sum_value):
    add_to_dictionary('sum_value', name1, name2, sum_value)
    if(name1 in angles and name2 in angles and sum_value > 360):
        #NULL
        null.flag = True
        return
        
    if(sum_value == 0):
        #NULL
        null.flag = True
        return
    
    know_call(name1,name2)
    return

def set_tan(name1, name2):
    #NULL
    null.flag = True
    return

#NOT INPUTS
def set_similar(name1, name2):
    add_to_dictionary('similar',name1,name2)
    know_call(name1,name2)
    return

def set_congruent(name1, name2):
    add_to_dictionary('congruent',name1,name2)
    know_call(name1,name2)
    return

#Knowables

#ANGLES

def know_a1():
    if check_dictionary("sum_value", "a1", "a9", 90) == False and check_dictionary("perpendicular", "ls10", "ls11"):
        add_to_dictionary("sum_value", "a1", "a9", 90);
        know_a9();
    if check_dictionary("sum_value", "a1", "a5", 90) == False and check_dictionary("perpendicular", "ls12", "ls11"):
        add_to_dictionary("sum_value", "a1", "a5", 90);
        know_a5();

    if check_dictionary("sum_value", "a1", "a9", 90) and check_dictionary("perpendicular", "ls10", "ls11") == False:
        add_to_dictionary("perpendicular", "ls10", "ls11");
        know_ls10();
        know_ls11();
    if check_dictionary("sum_value", "a1", "a5", 90) and check_dictionary("perpendicular", "ls12", "ls11") == False:
        add_to_dictionary("perpendicular", "ls12", "ls11");
        know_ls11();
        know_ls12();
        
    return

def know_a2():

    if check_dictionary("equal", "ls1", "ls9") and check_dictionary("equal", "a2", "a3") == False :
        add_to_dictionary("equal", "a2", "a3");
        know_a3();

    if check_dictionary("equal", "a2", "a3") or check_dictionary("equal", "a2", "a7"):
        if check_dictionary("equal", "ls1", "ls9") == False:
            add_to_dictionary("equal", "ls1", "ls9");
            know_ls1();
            know_ls9();
        if check_dictionary("equal", "a2", "a3") == False:
            add_to_dictionary("equal", "a2", "a3");
            know_a2();
            know_a3();
        if check_dictionary("equal", "a2", "a7") == False:
            add_to_dictionary("equal", "a2", "a7");
            know_a2();
            know_a7();
        if check_dictionary("equal", "a3", "a4") == False:
            add_to_dictionary("equal", "a3", "a4");
            know_a3();
            know_a4();
        if check_dictionary("congruent", "ar4", "ar6") == False:
            add_to_dictionary("congruent", "ar4", "ar6");
            know_ar4();
            know_ar6();
        
        
    return

def know_a3():
    
    if check_dictionary("equal", "a2", "a3") or check_dictionary("equal", "a3", "a4"):
        if check_dictionary("equal", "ls1", "ls9") == False:
            add_to_dictionary("equal", "ls1", "ls9");
            know_ls1();
            know_ls9();
        if check_dictionary("equal", "a2", "a3") == False:
            add_to_dictionary("equal", "a2", "a3");
            know_a2();
            know_a3();
        if check_dictionary("equal", "a2", "a7") == False:
            add_to_dictionary("equal", "a2", "a7");
            know_a2();
            know_a7();
        if check_dictionary("equal", "a3", "a4") == False:
            add_to_dictionary("equal", "a3", "a4");
            know_a3();
            know_a4();
        if check_dictionary("congruent", "ar4", "ar6") == False:
            add_to_dictionary("congruent", "ar4", "ar6");
            know_ar4();
            know_ar6();
    return

def know_a4():

    if check_dictionary("equal", "a4", "a6") or check_dictionary("equal", "a8", "a4"):
        if check_dictionary("equal", "ls3", "ls4") == False:
            add_to_dictionary("equal", "ls3", "ls4");
            know_ls3();
            know_ls4();
        if check_dictionary("equal", "a2", "a6") == False:
            add_to_dictionary("equal", "a2", "a6");
            know_a2();
            know_a3();
        if check_dictionary("equal", "a4", "a6") == False:
            add_to_dictionary("equal", "a4", "a6");
            know_a2();
            know_a7();
        if check_dictionary("equal", "a8", "a4") == False:
            add_to_dictionary("equal", "a8", "a4");
            know_a8();
            know_a4();
        if check_dictionary("congruent", "ar4", "ar5") == False:
            add_to_dictionary("congruent", "ar4", "ar5");
            know_ar4();
            know_ar5();
    return

def know_a5():
    if check_dictionary("sum_value", "a5", "a9", 90) == False and check_dictionary("perpendicular", "ls10", "ls12"):
        add_to_dictionary("sum_value", "a5", "a9", 90);
        know_a9();
    if check_dictionary("sum_value", "a5", "a1", 90) == False and check_dictionary("perpendicular", "ls12", "ls11"):
        add_to_dictionary("sum_value", "a5", "a1", 90);
        know_a1();

    if check_dictionary("sum_value", "a5", "a9", 90) and check_dictionary("perpendicular", "ls10", "ls12") == False:
        add_to_dictionary("perpendicular", "ls10", "ls12");
        know_ls10();
        know_ls12();
    if check_dictionary("sum_value", "a1", "a5", 90) and check_dictionary("perpendicular", "ls12", "ls11") == False:
        add_to_dictionary("perpendicular", "ls12", "ls11");
        know_ls11();
        know_ls12();
    return

def know_a6():

    if check_dictionary("equal", "a4", "a6") or check_dictionary("equal", "a6", "a2"):
        if check_dictionary("equal", "ls3", "ls4") == False:
            add_to_dictionary("equal", "ls3", "ls4");
            know_ls3();
            know_ls4();
        if check_dictionary("equal", "a2", "a6") == False:
            add_to_dictionary("equal", "a2", "a6");
            know_a2();
            know_a3();
        if check_dictionary("equal", "a4", "a6") == False:
            add_to_dictionary("equal", "a4", "a6");
            know_a2();
            know_a7();
        if check_dictionary("equal", "a8", "a4") == False:
            add_to_dictionary("equal", "a8", "a4");
            know_a8();
            know_a4();
        if check_dictionary("congruent", "ar4", "ar5") == False:
            add_to_dictionary("congruent", "ar4", "ar5");
            know_ar4();
            know_ar5();
    return

def know_a7():
    
    if check_dictionary("equal", "a7", "a8") or check_dictionary("equal", "a7", "a6"):
        if check_dictionary("equal", "ls6", "ls7") == False:
            add_to_dictionary("equal", "ls6", "ls7");
            know_ls6();
            know_ls7();
        if check_dictionary("equal", "a8", "a3") == False:
            add_to_dictionary("equal", "a8", "a3");
            know_a8();
            know_a3();
        if check_dictionary("equal", "a7", "a6") == False:
            add_to_dictionary("equal", "a7", "a6");
            know_a7();
            know_a6();
        if check_dictionary("equal", "a7", "a8") == False:
            add_to_dictionary("equal", "a7", "a8");
            know_a7();
            know_a8();
        if check_dictionary("congruent", "ar6", "ar5") == False:
            add_to_dictionary("congruent", "ar6", "ar5");
            know_ar6();
            know_ar5();
    return

def know_a8():
    if check_dictionary("equal", "a7", "a8") or check_dictionary("equal", "a8", "a3"):
        if check_dictionary("equal", "ls6", "ls7") == False:
            add_to_dictionary("equal", "ls6", "ls7");
            know_ls6();
            know_ls7();
        if check_dictionary("equal", "a8", "a3") == False:
            add_to_dictionary("equal", "a8", "a3");
            know_a8();
            know_a3();
        if check_dictionary("equal", "a7", "a6") == False:
            add_to_dictionary("equal", "a7", "a6");
            know_a7();
            know_a6();
        if check_dictionary("equal", "a7", "a8") == False:
            add_to_dictionary("equal", "a7", "a8");
            know_a7();
            know_a8();
        if check_dictionary("congruent", "ar6", "ar5") == False:
            add_to_dictionary("congruent", "ar6", "ar5");
            know_ar6();
            know_ar5();
    return

def know_a9():
    if check_dictionary("sum_value", "a1", "a9", 90) == False and check_dictionary("perpendicular", "ls10", "ls11"):
        add_to_dictionary("sum_value", "a1", "a9", 90);
        know_a1();
    if check_dictionary("sum_value", "a5", "a9", 90) == False and check_dictionary("perpendicular", "ls10", "ls12"):
        add_to_dictionary("sum_value", "a5", "a9", 90);
        know_a5();

    if check_dictionary("sum_value", "a5", "a9", 90) and check_dictionary("perpendicular", "ls10", "ls12") == False:
        add_to_dictionary("perpendicular", "ls10", "ls12");
        know_ls10();
        know_ls12();
    if check_dictionary("sum_value", "a1", "a9", 90) and check_dictionary("perpendicular", "ls10", "ls11") == False:
        add_to_dictionary("perpendicular", "ls10", "ls11");
        know_ls11();
        know_ls10();
    return

def know_b1():
    if check_dictionary("equal", "b1", "b6"):
        if check_dictionary("equal", "ls1", "ls9") == False:
            add_to_dictionary("equal", "ls1", "ls9");
            know_ls1();
            know_ls9();
        if check_dictionary("equal", "a2", "a3") == False:
            add_to_dictionary("equal", "a2", "a3");
            know_a2();
            know_a3();
        if check_dictionary("equal", "a2", "a7") == False:
            add_to_dictionary("equal", "a2", "a7");
            know_a2();
            know_a7();
        if check_dictionary("equal", "a3", "a4") == False:
            add_to_dictionary("equal", "a3", "a4");
            know_a3();
            know_a4();
        if check_dictionary("congruent", "ar4", "ar6") == False:
            add_to_dictionary("congruent", "ar4", "ar6");
            know_ar4();
            know_ar6();
    return

def know_b2():
    if check_dictionary("equal", "b2", "b3"):
        if check_dictionary("equal", "ls3", "ls4") == False:
            add_to_dictionary("equal", "ls3", "ls4");
            know_ls3();
            know_ls4();
        if check_dictionary("equal", "a2", "a6") == False:
            add_to_dictionary("equal", "a2", "a6");
            know_a2();
            know_a3();
        if check_dictionary("equal", "a4", "a6") == False:
            add_to_dictionary("equal", "a4", "a6");
            know_a2();
            know_a7();
        if check_dictionary("equal", "a8", "a4") == False:
            add_to_dictionary("equal", "a8", "a4");
            know_a8();
            know_a4();
        if check_dictionary("congruent", "ar4", "ar5") == False:
            add_to_dictionary("congruent", "ar4", "ar5");
            know_ar4();
            know_ar5();
    
    return

def know_b3():
    if check_dictionary("equal", "b2", "b3"):
        if check_dictionary("equal", "ls3", "ls4") == False:
            add_to_dictionary("equal", "ls3", "ls4");
            know_ls3();
            know_ls4();
        if check_dictionary("equal", "a2", "a6") == False:
            add_to_dictionary("equal", "a2", "a6");
            know_a2();
            know_a3();
        if check_dictionary("equal", "a4", "a6") == False:
            add_to_dictionary("equal", "a4", "a6");
            know_a2();
            know_a7();
        if check_dictionary("equal", "a8", "a4") == False:
            add_to_dictionary("equal", "a8", "a4");
            know_a8();
            know_a4();
        if check_dictionary("congruent", "ar4", "ar5") == False:
            add_to_dictionary("congruent", "ar4", "ar5");
            know_ar4();
            know_ar5();

    return

def know_b4():
    if check_dictionary("equal", "b4", "b5") :
        if check_dictionary("equal", "ls6", "ls7") == False:
            add_to_dictionary("equal", "ls6", "ls7");
            know_ls6();
            know_ls7();
        if check_dictionary("equal", "a8", "a3") == False:
            add_to_dictionary("equal", "a8", "a3");
            know_a8();
            know_a3();
        if check_dictionary("equal", "a7", "a6") == False:
            add_to_dictionary("equal", "a7", "a6");
            know_a7();
            know_a6();
        if check_dictionary("equal", "a7", "a8") == False:
            add_to_dictionary("equal", "a7", "a8");
            know_a7();
            know_a8();
        if check_dictionary("congruent", "ar6", "ar5") == False:
            add_to_dictionary("congruent", "ar6", "ar5");
            know_ar6();
            know_ar5();

    return

def know_b5():
    if check_dictionary("equal", "b4", "b5") :
        if check_dictionary("equal", "ls6", "ls7") == False:
            add_to_dictionary("equal", "ls6", "ls7");
            know_ls6();
            know_ls7();
        if check_dictionary("equal", "a8", "a3") == False:
            add_to_dictionary("equal", "a8", "a3");
            know_a8();
            know_a3();
        if check_dictionary("equal", "a7", "a6") == False:
            add_to_dictionary("equal", "a7", "a6");
            know_a7();
            know_a6();
        if check_dictionary("equal", "a7", "a8") == False:
            add_to_dictionary("equal", "a7", "a8");
            know_a7();
            know_a8();
        if check_dictionary("congruent", "ar6", "ar5") == False:
            add_to_dictionary("congruent", "ar6", "ar5");
            know_ar6();
            know_ar5();

    return

def know_b6():
    if check_dictionary("equal", "b1", "b6"):
        if check_dictionary("equal", "ls1", "ls9") == False:
            add_to_dictionary("equal", "ls1", "ls9");
            know_ls1();
            know_ls9();
        if check_dictionary("equal", "a2", "a3") == False:
            add_to_dictionary("equal", "a2", "a3");
            know_a2();
            know_a3();
        if check_dictionary("equal", "a2", "a7") == False:
            add_to_dictionary("equal", "a2", "a7");
            know_a2();
            know_a7();
        if check_dictionary("equal", "a3", "a4") == False:
            add_to_dictionary("equal", "a3", "a4");
            know_a3();
            know_a4();
        if check_dictionary("congruent", "ar4", "ar6") == False:
            add_to_dictionary("congruent", "ar4", "ar6");
            know_ar4();
            know_ar6();

    return

def know_c1():
    return

def know_c2():
    
    return

def know_c3():
    
    return

def know_c4():
    
    return

def know_c5():
    
    return

def know_c6():
    
    return

def know_d1():
   
    return

def know_d2():
    
    return

def know_d3():
    
    return

def know_d4():
   
    return

def know_d5():
   
    return

def know_d6():
    
    return

#LINE SEGMENTS

def know_ls1():
    if check_dictionary("equal", "ls1", "ls9"):
        if check_dictionary("equal", "a2", "a3") == False:
            add_to_dictionary("equal", "a2", "a3");
            know_a2();
            know_a3();
        if check_dictionary("equal", "a2", "a7") == False:
            add_to_dictionary("equal", "a2", "a7");
            know_a2();
            know_a7();
        if check_dictionary("equal", "a3", "a4") == False:
            add_to_dictionary("equal", "a3", "a4");
            know_a3();
            know_a4();
        if check_dictionary("congruent", "ar4", "ar6") == False:
            add_to_dictionary("congruent", "ar4", "ar6");
            know_ar4();
            know_ar6();

    if check_dictionary("perpendicular", "ls10", "ls11") == False and (check_dictionary("perpendicular", "ls1", "ls11") or check_dictionary("perpendicular", "ls1", "ls4") or check_dictionary("perpendicular", "ls1", "ls5") or check_dictionary("perpendicular", "ls1", "ls6")) :
        add_to_dictionary("perpendicular", "ls10", "ls11");
        know_ls11();
    if check_dictionary("perpendicular", "ls10", "ls12") == False and (check_dictionary("perpendicular", "ls1", "ls12") or check_dictionary("perpendicular", "ls1", "ls7") or check_dictionary("perpendicular", "ls1", "ls8") or check_dictionary("perpendicular", "ls1", "ls9")) :
        add_to_dictionary("perpendicular", "ls10", "ls12");
        know_ls12();
    return

def know_ls2():
    
    
    if check_dictionary("perpendicular", "ls10", "ls11") == False and (check_dictionary("perpendicular", "ls2", "ls11") or check_dictionary("perpendicular", "ls2", "ls4") or check_dictionary("perpendicular", "ls2", "ls5") or check_dictionary("perpendicular", "ls2", "ls6")):
        add_to_dictionary("perpendicular", "ls10", "ls11");
        know_ls11();
    if check_dictionary("perpendicular", "ls10", "ls12") == False and (check_dictionary("perpendicular", "ls2", "ls12") or check_dictionary("perpendicular", "ls2", "ls7") or check_dictionary("perpendicular", "ls2", "ls8") or check_dictionary("perpendicular", "ls2", "ls9")):
        add_to_dictionary("perpendicular", "ls10", "ls12");
        know_ls12();

    if check_dictionary("equal", "ls5", "ls2"):
        if check_dictionary("equal", "ls3", "ls4") == False:
            add_to_dictionary("equal", "ls3", "ls4");
            know_ls3();
            know_ls4();
        if check_dictionary("equal", "a2", "a6") == False:
            add_to_dictionary("equal", "a2", "a6");
            know_a2();
            know_a3();
        if check_dictionary("equal", "a4", "a6") == False:
            add_to_dictionary("equal", "a4", "a6");
            know_a2();
            know_a7();
        if check_dictionary("equal", "a8", "a4") == False:
            add_to_dictionary("equal", "a8", "a4");
            know_a8();
            know_a4();
        if check_dictionary("congruent", "ar5", "ar4") == False:
            add_to_dictionary("congruent", "ar5", "ar4");
            know_ar5();
            know_ar4();
        
    if check_dictionary("equal", "ls2", "ls8"):
        if check_dictionary("equal", "ls1", "ls9") == False:
            add_to_dictionary("equal", "ls1", "ls9");
            know_ls1();
            know_ls9();
        if check_dictionary("equal", "a2", "a3") == False:
            add_to_dictionary("equal", "a2", "a3");
            know_a2();
            know_a3();
        if check_dictionary("equal", "a2", "a7") == False:
            add_to_dictionary("equal", "a2", "a7");
            know_a2();
            know_a7();
        if check_dictionary("equal", "a3", "a4") == False:
            add_to_dictionary("equal", "a3", "a4");
            know_a3();
            know_a4();
        if check_dictionary("congruent", "ar4", "ar6") == False:
            add_to_dictionary("congruent", "ar4", "ar6");
            know_ar4();
            know_ar6();
    return

def know_ls3():
    if check_dictionary("equal", "ls3", "ls4") :
        if check_dictionary("equal", "a2", "a6") == False:
            add_to_dictionary("equal", "a2", "a6");
            know_a2();
            know_a3();
        if check_dictionary("equal", "a4", "a6") == False:
            add_to_dictionary("equal", "a4", "a6");
            know_a2();
            know_a7();
        if check_dictionary("equal", "a8", "a4") == False:
            add_to_dictionary("equal", "a8", "a4");
            know_a8();
            know_a4();
        if check_dictionary("congruent", "ar4", "ar5") == False:
            add_to_dictionary("congruent", "ar4", "ar5");
            know_ar4();
            know_ar5();

    if check_dictionary("perpendicular", "ls10", "ls11") == False and (check_dictionary("perpendicular", "ls3", "ls11") or check_dictionary("perpendicular", "ls3", "ls4") or check_dictionary("perpendicular", "ls3", "ls5") or check_dictionary("perpendicular", "ls3", "ls6")):
        add_to_dictionary("perpendicular", "ls10", "ls11");
        know_ls11();
    if check_dictionary("perpendicular", "ls10", "ls12") == False and (check_dictionary("perpendicular", "ls3", "ls12") or check_dictionary("perpendicular", "ls3", "ls7") or check_dictionary("perpendicular", "ls3", "ls8") or check_dictionary("perpendicular", "ls3", "ls9")):
        add_to_dictionary("perpendicular", "ls10", "ls12");
        know_ls12();
    return

def know_ls4():
    if check_dictionary("equal", "ls3", "ls4") :
        if check_dictionary("equal", "a2", "a6") == False:
            add_to_dictionary("equal", "a2", "a6");
            know_a2();
            know_a3();
        if check_dictionary("equal", "a4", "a6") == False:
            add_to_dictionary("equal", "a4", "a6");
            know_a2();
            know_a7();
        if check_dictionary("equal", "a8", "a4") == False:
            add_to_dictionary("equal", "a8", "a4");
            know_a8();
            know_a4();
        if check_dictionary("congruent", "ar4", "ar5") == False:
            add_to_dictionary("congruent", "ar4", "ar5");
            know_ar4();
            know_ar5();

    if check_dictionary("perpendicular", "ls10", "ls11") == False and (check_dictionary("perpendicular", "ls4", "ls10") or check_dictionary("perpendicular", "ls1", "ls4") or check_dictionary("perpendicular", "ls2", "ls4") or check_dictionary("perpendicular", "ls3", "ls4")):
        add_to_dictionary("perpendicular", "ls10", "ls11");
        know_ls10();
    if check_dictionary("perpendicular", "ls11", "ls12") == False and (check_dictionary("perpendicular", "ls4", "ls12") or check_dictionary("perpendicular", "ls9", "ls4") or check_dictionary("perpendicular", "ls8", "ls4") or check_dictionary("perpendicular", "ls7", "ls4")):
        add_to_dictionary("perpendicular", "ls11", "ls12");
        know_ls12();
    return

def know_ls5():
    if check_dictionary("perpendicular", "ls10", "ls11") == False and (check_dictionary("perpendicular", "ls5", "ls10") or check_dictionary("perpendicular", "ls1", "ls5") or check_dictionary("perpendicular", "ls2", "ls5") or check_dictionary("perpendicular", "ls3", "ls5")):
        add_to_dictionary("perpendicular", "ls10", "ls11");
        know_ls10();
    if check_dictionary("perpendicular", "ls11", "ls12") == False and (check_dictionary("perpendicular", "ls5", "ls12") or check_dictionary("perpendicular", "ls9", "ls5") or check_dictionary("perpendicular", "ls8", "ls5") or check_dictionary("perpendicular", "ls7", "ls5")):
        add_to_dictionary("perpendicular", "ls11", "ls12");

    if check_dictionary("equal", "ls5", "ls8"):
        if check_dictionary("equal", "ls6", "ls7") == False:
            add_to_dictionary("equal", "ls6", "ls7");
            know_ls6();
            know_ls7();
        if check_dictionary("equal", "a8", "a3") == False:
            add_to_dictionary("equal", "a8", "a3");
            know_a8();
            know_a3();
        if check_dictionary("equal", "a7", "a6") == False:
            add_to_dictionary("equal", "a7", "a6");
            know_a7();
            know_a6();
        if check_dictionary("equal", "a7", "a8") == False:
            add_to_dictionary("equal", "a7", "a8");
            know_a7();
            know_a8();
        if check_dictionary("congruent", "ar6", "ar5") == False:
            add_to_dictionary("congruent", "ar6", "ar5");
            know_ar6();
            know_ar5();
        
        
    if check_dictionary("equal", "ls2", "ls5"):
        if check_dictionary("equal", "ls3", "ls4") == False:
            add_to_dictionary("equal", "ls3", "ls4");
            know_ls3();
            know_ls4();
        if check_dictionary("equal", "a2", "a6") == False:
            add_to_dictionary("equal", "a2", "a6");
            know_a2();
            know_a3();
        if check_dictionary("equal", "a4", "a6") == False:
            add_to_dictionary("equal", "a4", "a6");
            know_a2();
            know_a7();
        if check_dictionary("equal", "a8", "a4") == False:
            add_to_dictionary("equal", "a8", "a4");
            know_a8();
            know_a4();
        if check_dictionary("congruent", "ar5", "ar4") == False:
            add_to_dictionary("congruent", "ar5", "ar4");
            know_ar5();
            know_ar4();
        
        
    return

def know_ls6():
    if check_dictionary("equal", "ls6", "ls7") :
        if check_dictionary("equal", "a8", "a3") == False:
            add_to_dictionary("equal", "a8", "a3");
            know_a8();
            know_a3();
        if check_dictionary("equal", "a7", "a6") == False:
            add_to_dictionary("equal", "a7", "a6");
            know_a7();
            know_a6();
        if check_dictionary("equal", "a7", "a8") == False:
            add_to_dictionary("equal", "a7", "a8");
            know_a7();
            know_a8();
        if check_dictionary("congruent", "ar5", "ar6") == False:
            add_to_dictionary("congruent", "ar5", "ar6");
            know_ar5();
            know_ar6();

    if check_dictionary("perpendicular", "ls10", "ls11") == False and (check_dictionary("perpendicular", "ls6", "ls10") or check_dictionary("perpendicular", "ls1", "ls6") or check_dictionary("perpendicular", "ls2", "ls6") or check_dictionary("perpendicular", "ls3", "ls6")):
        add_to_dictionary("perpendicular", "ls10", "ls11");
        know_ls10();
    if check_dictionary("perpendicular", "ls11", "ls12") == False and (check_dictionary("perpendicular", "ls6", "ls12") or check_dictionary("perpendicular", "ls9", "ls6") or check_dictionary("perpendicular", "ls8", "ls6") or check_dictionary("perpendicular", "ls7", "ls6")):
        add_to_dictionary("perpendicular", "ls11", "ls12");
    return

def know_ls7():
    if check_dictionary("equal", "ls6", "ls7") :
        if check_dictionary("equal", "a8", "a3") == False:
            add_to_dictionary("equal", "a8", "a3");
            know_a8();
            know_a3();
        if check_dictionary("equal", "a7", "a6") == False:
            add_to_dictionary("equal", "a7", "a6");
            know_a7();
            know_a6();
        if check_dictionary("equal", "a7", "a8") == False:
            add_to_dictionary("equal", "a7", "a8");
            know_a7();
            know_a8();
        if check_dictionary("congruent", "ar5", "ar6") == False:
            add_to_dictionary("congruent", "ar5", "ar6");
            know_ar5();
            know_ar6();
        
    if check_dictionary("perpendicular", "ls10", "ls12") == False and (check_dictionary("perpendicular", "ls7", "ls10") or check_dictionary("perpendicular", "ls1", "ls7") or check_dictionary("perpendicular", "ls2", "ls7") or check_dictionary("perpendicular", "ls3", "ls7")):
        add_to_dictionary("perpendicular", "ls10", "ls12");
        know_ls10();
    if check_dictionary("perpendicular", "ls11", "ls12") == False and (check_dictionary("perpendicular", "ls7", "ls11") or check_dictionary("perpendicular", "ls4", "ls7") or check_dictionary("perpendicular", "ls5", "ls7") or check_dictionary("perpendicular", "ls6", "ls7")):
        add_to_dictionary("perpendicular", "ls11", "ls12");

    return

def know_ls8():
    if check_dictionary("perpendicular", "ls10", "ls12") == False and (check_dictionary("perpendicular", "ls8", "ls10") or check_dictionary("perpendicular", "ls1", "ls8") or check_dictionary("perpendicular", "ls2", "ls8") or check_dictionary("perpendicular", "ls3", "ls8")):
        add_to_dictionary("perpendicular", "ls10", "ls12");
        know_ls10();
    if check_dictionary("perpendicular", "ls11", "ls12") == False and (check_dictionary("perpendicular", "ls8", "ls11") or check_dictionary("perpendicular", "ls4", "ls8") or check_dictionary("perpendicular", "ls5", "ls8") or check_dictionary("perpendicular", "ls6", "ls8")):
        add_to_dictionary("perpendicular", "ls11", "ls12");

    if check_dictionary("equal", "ls5", "ls8"):
        if check_dictionary("equal", "ls6", "ls7") == False:
            add_to_dictionary("equal", "ls6", "ls7");
            know_ls6();
            know_ls7();
        if check_dictionary("equal", "a8", "a3") == False:
            add_to_dictionary("equal", "a8", "a3");
            know_a8();
            know_a3();
        if check_dictionary("equal", "a7", "a6") == False:
            add_to_dictionary("equal", "a7", "a6");
            know_a7();
            know_a6();
        if check_dictionary("equal", "a7", "a8") == False:
            add_to_dictionary("equal", "a7", "a8");
            know_a7();
            know_a8();
        if check_dictionary("congruent", "ar6", "ar5") == False:
            add_to_dictionary("congruent", "ar6", "ar5");
            know_ar6();
            know_ar5();
        
        
    if check_dictionary("equal", "ls2", "ls8"):
        if check_dictionary("equal", "ls1", "ls9") == False:
            add_to_dictionary("equal", "ls1", "ls9");
            know_ls1();
            know_ls9();
        if check_dictionary("equal", "a2", "a3") == False:
            add_to_dictionary("equal", "a2", "a3");
            know_a2();
            know_a3();
        if check_dictionary("equal", "a2", "a7") == False:
            add_to_dictionary("equal", "a2", "a7");
            know_a2();
            know_a7();
        if check_dictionary("equal", "a3", "a4") == False:
            add_to_dictionary("equal", "a3", "a4");
            know_a3();
            know_a4();
        if check_dictionary("congruent", "ar4", "ar6") == False:
            add_to_dictionary("congruent", "ar4", "ar6");
            know_ar4();
            know_ar6();

        
    return

def know_ls9():
    if check_dictionary("equal", "ls1", "ls9"):
        if check_dictionary("equal", "a2", "a3") == False:
            add_to_dictionary("equal", "a2", "a3");
            know_a2();
            know_a3();
        if check_dictionary("equal", "a2", "a7") == False:
            add_to_dictionary("equal", "a2", "a7");
            know_a2();
            know_a7();
        if check_dictionary("equal", "a3", "a4") == False:
            add_to_dictionary("equal", "a3", "a4");
            know_a3();
            know_a4();
        if check_dictionary("congruent", "ar4", "ar6") == False:
            add_to_dictionary("congruent", "ar4", "ar6");
            know_ar4();
            know_ar6();

    if check_dictionary("perpendicular", "ls10", "ls12") == False and (check_dictionary("perpendicular", "ls9", "ls10") or check_dictionary("perpendicular", "ls1", "ls9") or check_dictionary("perpendicular", "ls2", "ls9") or check_dictionary("perpendicular", "ls3", "ls9")):
        add_to_dictionary("perpendicular", "ls10", "ls12");
        know_ls10();
    if check_dictionary("perpendicular", "ls11", "ls12") == False and (check_dictionary("perpendicular", "ls9", "ls11") or check_dictionary("perpendicular", "ls4", "ls9") or check_dictionary("perpendicular", "ls5", "ls9") or check_dictionary("perpendicular", "ls6", "ls9")):
        add_to_dictionary("perpendicular", "ls11", "ls12");
    return

def know_ls10():
    if check_dictionary("perpendicular", "ls10", "ls11") :
        if check_dictionary("perpendicular", "ls10", "ls4") == False:
            add_to_dictionary("perpendicular", "ls10", "ls4");
            know_ls10();
            know_ls4();
        if check_dictionary("perpendicular", "ls4", "ls3") == False:
            add_to_dictionary("perpendicular", "ls4", "ls3");
            know_ls3();
            know_ls4();
        if check_dictionary("perpendicular", "ls4", "ls2") == False:
            add_to_dictionary("perpendicular", "ls4", "ls2");
            know_ls2();
            know_ls4();
        if check_dictionary("perpendicular", "ls4", "ls1") == False:
            add_to_dictionary("perpendicular", "ls4", "ls1");
            know_ls1();
            know_ls4();
        if check_dictionary("perpendicular", "ls10", "ls5") == False:
            add_to_dictionary("perpendicular", "ls10", "ls5");
            know_ls10();
            know_ls5();
        if check_dictionary("perpendicular", "ls5", "ls3") == False:
            add_to_dictionary("perpendicular", "ls5", "ls3");
            know_ls5();
            know_ls3();
        if check_dictionary("perpendicular", "ls5", "ls2") == False:
            add_to_dictionary("perpendicular", "ls5", "ls2");
            know_ls5();
            know_ls2();
        if check_dictionary("perpendicular", "ls5", "ls1") == False:
            add_to_dictionary("perpendicular", "ls5", "ls1");
            know_ls5();
            know_ls1();
        if check_dictionary("perpendicular", "ls10", "ls6") == False:
            add_to_dictionary("perpendicular", "ls10", "ls6");
            know_ls10();
            know_ls6();
        if check_dictionary("perpendicular", "ls6", "ls3") == False:
            add_to_dictionary("perpendicular", "ls6", "ls3");
            know_ls6();
            know_ls3();
        if check_dictionary("perpendicular", "ls6", "ls2") == False:
            add_to_dictionary("perpendicular", "ls6", "ls2");
            know_ls6();
            know_ls2();
        if check_dictionary("perpendicular", "ls6", "ls1") == False:
            add_to_dictionary("perpendicular", "ls6", "ls1");
            know_ls6();
            know_ls1();

        
        if check_dictionary("perpendicular", "ls11", "ls1") == False:
            add_to_dictionary("perpendicular", "ls11", "ls1");
            know_ls11();
            know_ls1();
        if check_dictionary("perpendicular", "ls1", "ls4") == False:
            add_to_dictionary("perpendicular", "ls1", "ls4");
            know_ls1();
            know_ls4();
        if check_dictionary("perpendicular", "ls1", "ls5") == False:
            add_to_dictionary("perpendicular", "ls1", "ls5");
            know_ls1();
            know_ls5();
        if check_dictionary("perpendicular", "ls1", "ls6") == False:
            add_to_dictionary("perpendicular", "ls1", "ls6");
            know_ls1();
            know_ls6();
        if check_dictionary("perpendicular", "ls11", "ls2") == False:
            add_to_dictionary("perpendicular", "ls11", "ls2");
            know_ls11();
            know_ls2();
        if check_dictionary("perpendicular", "ls2", "ls4") == False:
            add_to_dictionary("perpendicular", "ls2", "ls4");
            know_ls2();
            know_ls4();
        if check_dictionary("perpendicular", "ls2", "ls5") == False:
            add_to_dictionary("perpendicular", "ls2", "ls5");
            know_ls2();
            know_ls5();
        if check_dictionary("perpendicular", "ls2", "ls6") == False:
            add_to_dictionary("perpendicular", "ls2", "ls6");
            know_ls2();
            know_ls6();
        if check_dictionary("perpendicular", "ls11", "ls3") == False:
            add_to_dictionary("perpendicular", "ls11", "ls3");
            know_ls11();
            know_ls3();
        if check_dictionary("perpendicular", "ls3", "ls4") == False:
            add_to_dictionary("perpendicular", "ls3", "ls4");
            know_ls3();
            know_ls4();
        if check_dictionary("perpendicular", "ls3", "ls5") == False:
            add_to_dictionary("perpendicular", "ls3", "ls5");
            know_ls3();
            know_ls5();
        if check_dictionary("perpendicular", "ls3", "ls6") == False:
            add_to_dictionary("perpendicular", "ls3", "ls6");
            know_ls3();
            know_ls6();
        
    if check_dictionary("perpendicular", "ls10", "ls12") :
        if check_dictionary("perpendicular", "ls10", "ls7") == False:
            add_to_dictionary("perpendicular", "ls10", "ls7");
            know_ls10();
            know_ls7();
        if check_dictionary("perpendicular", "ls7", "ls3") == False:
            add_to_dictionary("perpendicular", "ls7", "ls3");
            know_ls7();
            know_ls3();
        if check_dictionary("perpendicular", "ls7", "ls2") == False:
            add_to_dictionary("perpendicular", "ls7", "ls2");
            know_ls7();
            know_ls2();
        if check_dictionary("perpendicular", "ls7", "ls1") == False:
            add_to_dictionary("perpendicular", "ls7", "ls1");
            know_ls7();
            know_ls1();
        if check_dictionary("perpendicular", "ls10", "ls8") == False:
            add_to_dictionary("perpendicular", "ls10", "ls8");
            know_ls10();
            know_ls8();
        if check_dictionary("perpendicular", "ls8", "ls3") == False:
            add_to_dictionary("perpendicular", "ls8", "ls3");
            know_ls8();
            know_ls3();
        if check_dictionary("perpendicular", "ls8", "ls2") == False:
            add_to_dictionary("perpendicular", "ls8", "ls2");
            know_ls8();
            know_ls3();
        if check_dictionary("perpendicular", "ls8", "ls1") == False:
            add_to_dictionary("perpendicular", "ls8", "ls1");
            know_ls8();
            know_ls1();
        if check_dictionary("perpendicular", "ls10", "ls9") == False:
            add_to_dictionary("perpendicular", "ls10", "ls9");
            know_ls10();
            know_ls9();
        if check_dictionary("perpendicular", "ls9", "ls3") == False:
            add_to_dictionary("perpendicular", "ls9", "ls3");
            know_ls9();
            know_ls3();
        if check_dictionary("perpendicular", "ls9", "ls2") == False:
            add_to_dictionary("perpendicular", "ls9", "ls2");
            know_ls9();
            know_ls2();
        if check_dictionary("perpendicular", "ls9", "ls1") == False:
            add_to_dictionary("perpendicular", "ls9", "ls1");
            know_ls9();
            know_ls1();

        
        if check_dictionary("perpendicular", "ls12", "ls1") == False:
            add_to_dictionary("perpendicular", "ls12", "ls1");
            know_ls12();
            know_ls1();
        if check_dictionary("perpendicular", "ls1", "ls7") == False:
            add_to_dictionary("perpendicular", "ls1", "ls7");
            know_ls1();
            know_ls7();
        if check_dictionary("perpendicular", "ls1", "ls8") == False:
            add_to_dictionary("perpendicular", "ls1", "ls8");
            know_ls1();
            know_ls8();
        if check_dictionary("perpendicular", "ls1", "ls9") == False:
            add_to_dictionary("perpendicular", "ls1", "ls9");
            know_ls1();
            know_ls9();
        if check_dictionary("perpendicular", "ls12", "ls2") == False:
            add_to_dictionary("perpendicular", "ls12", "ls2");
            know_ls12();
            know_ls2();
        if check_dictionary("perpendicular", "ls2", "ls7") == False:
            add_to_dictionary("perpendicular", "ls2", "ls7");
            know_ls2();
            know_ls7();
        if check_dictionary("perpendicular", "ls2", "ls8") == False:
            add_to_dictionary("perpendicular", "ls2", "ls8");
            know_ls2();
            know_ls8();
        if check_dictionary("perpendicular", "ls2", "ls9") == False:
            add_to_dictionary("perpendicular", "ls2", "ls9");
            know_ls2();
            know_ls9();
        if check_dictionary("perpendicular", "ls12", "ls3") == False:
            add_to_dictionary("perpendicular", "ls12", "ls3");
            know_ls12();
            know_ls3();
        if check_dictionary("perpendicular", "ls3", "ls7") == False:
            add_to_dictionary("perpendicular", "ls3", "ls7");
            know_ls3();
            know_ls7();
        if check_dictionary("perpendicular", "ls3", "ls8") == False:
            add_to_dictionary("perpendicular", "ls3", "ls8");
            know_ls3();
            know_ls8();
        if check_dictionary("perpendicular", "ls3", "ls9") == False:
            add_to_dictionary("perpendicular", "ls3", "ls9");
            know_ls3();
            know_ls9();
        
    return

def know_ls11():
    if check_dictionary("perpendicular", "ls10", "ls11") :
        if check_dictionary("perpendicular", "ls10", "ls4") == False:
            add_to_dictionary("perpendicular", "ls10", "ls4");
            know_ls10();
            know_ls4();
        if check_dictionary("perpendicular", "ls4", "ls3") == False:
            add_to_dictionary("perpendicular", "ls4", "ls3");
            know_ls3();
            know_ls4();
        if check_dictionary("perpendicular", "ls4", "ls2") == False:
            add_to_dictionary("perpendicular", "ls4", "ls2");
            know_ls2();
            know_ls4();
        if check_dictionary("perpendicular", "ls4", "ls1") == False:
            add_to_dictionary("perpendicular", "ls4", "ls1");
            know_ls1();
            know_ls4();
        if check_dictionary("perpendicular", "ls10", "ls5") == False:
            add_to_dictionary("perpendicular", "ls10", "ls5");
            know_ls10();
            know_ls5();
        if check_dictionary("perpendicular", "ls5", "ls3") == False:
            add_to_dictionary("perpendicular", "ls5", "ls3");
            know_ls5();
            know_ls3();
        if check_dictionary("perpendicular", "ls5", "ls2") == False:
            add_to_dictionary("perpendicular", "ls5", "ls2");
            know_ls5();
            know_ls2();
        if check_dictionary("perpendicular", "ls5", "ls1") == False:
            add_to_dictionary("perpendicular", "ls5", "ls1");
            know_ls5();
            know_ls1();
        if check_dictionary("perpendicular", "ls10", "ls6") == False:
            add_to_dictionary("perpendicular", "ls10", "ls6");
            know_ls10();
            know_ls6();
        if check_dictionary("perpendicular", "ls6", "ls3") == False:
            add_to_dictionary("perpendicular", "ls6", "ls3");
            know_ls10();
            know_ls4();
        if check_dictionary("perpendicular", "ls6", "ls2") == False:
            add_to_dictionary("perpendicular", "ls6", "ls2");
            know_ls6();
            know_ls2();
        if check_dictionary("perpendicular", "ls6", "ls1") == False:
            add_to_dictionary("perpendicular", "ls6", "ls1");
            know_ls6();
            know_ls1();

        
        if check_dictionary("perpendicular", "ls11", "ls1") == False:
            add_to_dictionary("perpendicular", "ls11", "ls1");
            know_ls11();
            know_ls1();
        if check_dictionary("perpendicular", "ls1", "ls4") == False:
            add_to_dictionary("perpendicular", "ls1", "ls4");
            know_ls1();
            know_ls4();
        if check_dictionary("perpendicular", "ls1", "ls5") == False:
            add_to_dictionary("perpendicular", "ls1", "ls5");
            know_ls1();
            know_ls5();
        if check_dictionary("perpendicular", "ls1", "ls6") == False:
            add_to_dictionary("perpendicular", "ls1", "ls6");
            know_ls1();
            know_ls6();
        if check_dictionary("perpendicular", "ls11", "ls2") == False:
            add_to_dictionary("perpendicular", "ls11", "ls2");
            know_ls11();
            know_ls2();
        if check_dictionary("perpendicular", "ls2", "ls4") == False:
            add_to_dictionary("perpendicular", "ls2", "ls4");
            know_ls2();
            know_ls4();
        if check_dictionary("perpendicular", "ls2", "ls5") == False:
            add_to_dictionary("perpendicular", "ls2", "ls5");
            know_ls2();
            know_ls5();
        if check_dictionary("perpendicular", "ls2", "ls6") == False:
            add_to_dictionary("perpendicular", "ls2", "ls6");
            know_ls2();
            know_ls6();
        if check_dictionary("perpendicular", "ls11", "ls3") == False:
            add_to_dictionary("perpendicular", "ls11", "ls3");
            know_ls11();
            know_ls3();
        if check_dictionary("perpendicular", "ls3", "ls4") == False:
            add_to_dictionary("perpendicular", "ls3", "ls4");
            know_ls3();
            know_ls4();
        if check_dictionary("perpendicular", "ls3", "ls5") == False:
            add_to_dictionary("perpendicular", "ls3", "ls5");
            know_ls3();
            know_ls5();
        if check_dictionary("perpendicular", "ls3", "ls6") == False:
            add_to_dictionary("perpendicular", "ls3", "ls6");
            know_ls3();
            know_ls6();
        
        
    if check_dictionary("perpendicular", "ls11", "ls12") :
        if check_dictionary("perpendicular", "ls11", "ls7") == False:
            add_to_dictionary("perpendicular", "ls11", "ls7");
            know_ls11();
            know_ls7();
        if check_dictionary("perpendicular", "ls7", "ls6") == False:
            add_to_dictionary("perpendicular", "ls7", "ls6");
            know_ls7();
            know_ls6();
        if check_dictionary("perpendicular", "ls7", "ls5") == False:
            add_to_dictionary("perpendicular", "ls7", "ls5");
            know_ls7();
            know_ls5();
        if check_dictionary("perpendicular", "ls7", "ls4") == False:
            add_to_dictionary("perpendicular", "ls7", "ls4");
            know_ls7();
            know_ls4();
        if check_dictionary("perpendicular", "ls11", "ls8") == False:
            add_to_dictionary("perpendicular", "ls11", "ls8");
            know_ls11();
            know_ls8();
        if check_dictionary("perpendicular", "ls8", "ls6") == False:
            add_to_dictionary("perpendicular", "ls8", "ls6");
            know_ls8();
            know_ls6();
        if check_dictionary("perpendicular", "ls8", "ls5") == False:
            add_to_dictionary("perpendicular", "ls8", "ls5");
            know_ls8();
            know_ls5();
        if check_dictionary("perpendicular", "ls8", "ls4") == False:
            add_to_dictionary("perpendicular", "ls8", "ls4");
            know_ls8();
            know_ls4();
        if check_dictionary("perpendicular", "ls11", "ls9") == False:
            add_to_dictionary("perpendicular", "ls11", "ls9");
            know_ls11();
            know_ls9();
        if check_dictionary("perpendicular", "ls9", "ls6") == False:
            add_to_dictionary("perpendicular", "ls9", "ls6");
            know_ls9();
            know_ls6();
        if check_dictionary("perpendicular", "ls9", "ls5") == False:
            add_to_dictionary("perpendicular", "ls9", "ls5");
            know_ls9();
            know_ls5();
        if check_dictionary("perpendicular", "ls9", "ls4") == False:
            add_to_dictionary("perpendicular", "ls9", "ls4");
            know_ls9();
            know_ls4();

        
        if check_dictionary("perpendicular", "ls12", "ls4") == False:
            add_to_dictionary("perpendicular", "ls12", "ls4");
            know_ls12();
            know_ls4();
        if check_dictionary("perpendicular", "ls4", "ls7") == False:
            add_to_dictionary("perpendicular", "ls4", "ls7");
            know_ls4();
            know_ls7();
        if check_dictionary("perpendicular", "ls4", "ls8") == False:
            add_to_dictionary("perpendicular", "ls4", "ls8");
            know_ls8();
            know_ls4();
        if check_dictionary("perpendicular", "ls4", "ls9") == False:
            add_to_dictionary("perpendicular", "ls4", "ls9");
            know_ls9();
            know_ls4();
        if check_dictionary("perpendicular", "ls12", "ls5") == False:
            add_to_dictionary("perpendicular", "ls12", "ls5");
            know_ls12();
            know_ls5();
        if check_dictionary("perpendicular", "ls5", "ls7") == False:
            add_to_dictionary("perpendicular", "ls5", "ls7");
            know_ls5();
            know_ls7();
        if check_dictionary("perpendicular", "ls5", "ls8") == False:
            add_to_dictionary("perpendicular", "ls5", "ls8");
            know_ls5();
            know_ls8();
        if check_dictionary("perpendicular", "ls5", "ls9") == False:
            add_to_dictionary("perpendicular", "ls5", "ls9");
            know_ls5();
            know_ls9();
        if check_dictionary("perpendicular", "ls12", "ls6") == False:
            add_to_dictionary("perpendicular", "ls12", "ls6");
            know_ls12();
            know_ls6();
        if check_dictionary("perpendicular", "ls6", "ls7") == False:
            add_to_dictionary("perpendicular", "ls6", "ls7");
            know_ls6();
            know_ls7();
        if check_dictionary("perpendicular", "ls6", "ls8") == False:
            add_to_dictionary("perpendicular", "ls6", "ls8");
            know_ls6();
            know_ls8();
        if check_dictionary("perpendicular", "ls6", "ls9") == False:
            add_to_dictionary("perpendicular", "ls6", "ls9");
            know_ls6();
            know_ls9();
    return

def know_ls12():
    if check_dictionary("perpendicular", "ls10", "ls12") :
        if check_dictionary("perpendicular", "ls10", "ls7") == False:
            add_to_dictionary("perpendicular", "ls10", "ls7");
            know_ls10();
            know_ls7();
        if check_dictionary("perpendicular", "ls7", "ls3") == False:
            add_to_dictionary("perpendicular", "ls7", "ls3");
            know_ls7();
            know_ls3();
        if check_dictionary("perpendicular", "ls7", "ls2") == False:
            add_to_dictionary("perpendicular", "ls7", "ls2");
            know_ls7();
            know_ls2();
        if check_dictionary("perpendicular", "ls7", "ls1") == False:
            add_to_dictionary("perpendicular", "ls7", "ls1");
            know_ls7();
            know_ls1();
        if check_dictionary("perpendicular", "ls10", "ls8") == False:
            add_to_dictionary("perpendicular", "ls10", "ls8");
            know_ls10();
            know_ls8();
        if check_dictionary("perpendicular", "ls8", "ls3") == False:
            add_to_dictionary("perpendicular", "ls8", "ls3");
            know_ls8();
            know_ls3();
        if check_dictionary("perpendicular", "ls8", "ls2") == False:
            add_to_dictionary("perpendicular", "ls8", "ls2");
            know_ls8();
            know_ls2();
        if check_dictionary("perpendicular", "ls8", "ls1") == False:
            add_to_dictionary("perpendicular", "ls8", "ls1");
            know_ls8();
            know_ls1();
        if check_dictionary("perpendicular", "ls10", "ls9") == False:
            add_to_dictionary("perpendicular", "ls10", "ls9");
            know_ls10();
            know_ls9();
        if check_dictionary("perpendicular", "ls9", "ls3") == False:
            add_to_dictionary("perpendicular", "ls9", "ls3");
            know_ls9();
            know_ls3();
        if check_dictionary("perpendicular", "ls9", "ls2") == False:
            add_to_dictionary("perpendicular", "ls9", "ls2");
            know_ls9();
            know_ls2();
        if check_dictionary("perpendicular", "ls9", "ls1") == False:
            add_to_dictionary("perpendicular", "ls9", "ls1");
            know_ls9();
            know_ls1();

        
        if check_dictionary("perpendicular", "ls11", "ls7") == False:
            add_to_dictionary("perpendicular", "ls11", "ls7");
            know_ls11();
            know_ls7();
        if check_dictionary("perpendicular", "ls7", "ls4") == False:
            add_to_dictionary("perpendicular", "ls7", "ls4");
            know_ls7();
            know_ls4();
        if check_dictionary("perpendicular", "ls7", "ls5") == False:
            add_to_dictionary("perpendicular", "ls7", "ls5");
            know_ls7();
            know_ls5();
        if check_dictionary("perpendicular", "ls7", "ls6") == False:
            add_to_dictionary("perpendicular", "ls7", "ls6");
            know_ls7();
            know_ls6();
        if check_dictionary("perpendicular", "ls11", "ls8") == False:
            add_to_dictionary("perpendicular", "ls11", "ls8");
            know_ls11();
            know_ls8();
        if check_dictionary("perpendicular", "ls8", "ls4") == False:
            add_to_dictionary("perpendicular", "ls8", "ls4");
            know_ls8();
            know_ls4();
        if check_dictionary("perpendicular", "ls8", "ls5") == False:
            add_to_dictionary("perpendicular", "ls8", "ls5");
            know_ls8();
            know_ls5();
        if check_dictionary("perpendicular", "ls8", "ls6") == False:
            add_to_dictionary("perpendicular", "ls8", "ls6");
            know_ls8();
            know_ls6();
        if check_dictionary("perpendicular", "ls11", "ls9") == False:
            add_to_dictionary("perpendicular", "ls11", "ls9");
            know_ls11();
            know_ls9();
        if check_dictionary("perpendicular", "ls9", "ls4") == False:
            add_to_dictionary("perpendicular", "ls9", "ls4");
            know_ls9();
            know_ls4();
        if check_dictionary("perpendicular", "ls9", "ls5") == False:
            add_to_dictionary("perpendicular", "ls9", "ls5");
            know_ls9();
            know_ls5();
        if check_dictionary("perpendicular", "ls9", "ls6") == False:
            add_to_dictionary("perpendicular", "ls9", "ls6");
            know_ls9();
            know_ls6();
        
    if check_dictionary("perpendicular", "ls10", "ls12") :
        if check_dictionary("perpendicular", "ls10", "ls7") == False:
            add_to_dictionary("perpendicular", "ls10", "ls7");
            know_ls10();
            know_ls7();
        if check_dictionary("perpendicular", "ls7", "ls3") == False:
            add_to_dictionary("perpendicular", "ls7", "ls3");
            know_ls7();
            know_ls3();
        if check_dictionary("perpendicular", "ls7", "ls2") == False:
            add_to_dictionary("perpendicular", "ls7", "ls2");
            know_ls7();
            know_ls2();
        if check_dictionary("perpendicular", "ls7", "ls1") == False:
            add_to_dictionary("perpendicular", "ls7", "ls1");
            know_ls7();
            know_ls1();
        if check_dictionary("perpendicular", "ls10", "ls8") == False:
            add_to_dictionary("perpendicular", "ls10", "ls8");
            know_ls10();
            know_ls8();
        if check_dictionary("perpendicular", "ls8", "ls3") == False:
            add_to_dictionary("perpendicular", "ls8", "ls3");
            know_ls8();
            know_ls3();
        if check_dictionary("perpendicular", "ls8", "ls2") == False:
            add_to_dictionary("perpendicular", "ls8", "ls2");
            know_ls8();
            know_ls2();
        if check_dictionary("perpendicular", "ls8", "ls1") == False:
            add_to_dictionary("perpendicular", "ls8", "ls1");
            know_ls8();
            know_ls1();
        if check_dictionary("perpendicular", "ls10", "ls9") == False:
            add_to_dictionary("perpendicular", "ls10", "ls9");
            know_ls10();
            know_ls9();
        if check_dictionary("perpendicular", "ls9", "ls3") == False:
            add_to_dictionary("perpendicular", "ls9", "ls3");
            know_ls9();
            know_ls3();
        if check_dictionary("perpendicular", "ls9", "ls2") == False:
            add_to_dictionary("perpendicular", "ls9", "ls2");
            know_ls9();
            know_ls2();
        if check_dictionary("perpendicular", "ls9", "ls1") == False:
            add_to_dictionary("perpendicular", "ls9", "ls1");
            know_ls9();
            know_ls1();

        
        if check_dictionary("perpendicular", "ls12", "ls1") == False:
            add_to_dictionary("perpendicular", "ls12", "ls1");
            know_ls12();
            know_ls1();
        if check_dictionary("perpendicular", "ls1", "ls7") == False:
            add_to_dictionary("perpendicular", "ls1", "ls7");
            know_ls1();
            know_ls7();
        if check_dictionary("perpendicular", "ls1", "ls8") == False:
            add_to_dictionary("perpendicular", "ls1", "ls8");
            know_ls1();
            know_ls8();
        if check_dictionary("perpendicular", "ls1", "ls9") == False:
            add_to_dictionary("perpendicular", "ls1", "ls9");
            know_ls1();
            know_ls9();
        if check_dictionary("perpendicular", "ls12", "ls2") == False:
            add_to_dictionary("perpendicular", "ls12", "ls2");
            know_ls12();
            know_ls2();
        if check_dictionary("perpendicular", "ls2", "ls7") == False:
            add_to_dictionary("perpendicular", "ls2", "ls7");
            know_ls2();
            know_ls7();
        if check_dictionary("perpendicular", "ls2", "ls8") == False:
            add_to_dictionary("perpendicular", "ls2", "ls8");
            know_ls2();
            know_ls8();
        if check_dictionary("perpendicular", "ls2", "ls9") == False:
            add_to_dictionary("perpendicular", "ls2", "ls9");
            know_ls2();
            know_ls9();
        if check_dictionary("perpendicular", "ls12", "ls3") == False:
            add_to_dictionary("perpendicular", "ls12", "ls3");
            know_ls12();
            know_ls3();
        if check_dictionary("perpendicular", "ls3", "ls7") == False:
            add_to_dictionary("perpendicular", "ls3", "ls7");
            know_ls3();
            know_ls7();
        if check_dictionary("perpendicular", "ls3", "ls8") == False:
            add_to_dictionary("perpendicular", "ls3", "ls8");
            know_ls3();
            know_ls8();
        if check_dictionary("perpendicular", "ls3", "ls9") == False:
            add_to_dictionary("perpendicular", "ls3", "ls9");
            know_ls3();
            know_ls9();
        
    return

#ARC SEGMENTS

def know_as1():
    return

def know_as2():
    if check_dictionary("equal", "as2", "as4"):
        if check_dictionary("equal", "ls3", "ls4") == False:
            add_to_dictionary("equal", "ls3", "ls4");
            know_ls3();
            know_ls4();
        if check_dictionary("equal", "a2", "a6") == False:
            add_to_dictionary("equal", "a2", "a6");
            know_a2();
            know_a3();
        if check_dictionary("equal", "a4", "a6") == False:
            add_to_dictionary("equal", "a4", "a6");
            know_a2();
            know_a7();
        if check_dictionary("equal", "a8", "a4") == False:
            add_to_dictionary("equal", "a8", "a4");
            know_a8();
            know_a4();
        if check_dictionary("congruent", "ar4", "ar5") == False:
            add_to_dictionary("congruent", "ar4", "ar5");
            know_ar4();
            know_ar5();
        
        
    if check_dictionary("equal", "as2", "as6"):
        if check_dictionary("equal", "ls1", "ls9") == False:
            add_to_dictionary("equal", "ls1", "ls9");
            know_ls1();
            know_ls9();
        if check_dictionary("equal", "a2", "a3") == False:
            add_to_dictionary("equal", "a2", "a3");
            know_a2();
            know_a3();
        if check_dictionary("equal", "a2", "a7") == False:
            add_to_dictionary("equal", "a2", "a7");
            know_a2();
            know_a7();
        if check_dictionary("equal", "a3", "a4") == False:
            add_to_dictionary("equal", "a3", "a4");
            know_a3();
            know_a4();
        if check_dictionary("congruent", "ar4", "ar6") == False:
            add_to_dictionary("congruent", "ar4", "ar6");
            know_ar4();
            know_ar6();
        
        
    return

def know_as3():
    return

def know_as4():
    if check_dictionary("equal", "as2", "as4"):
        if check_dictionary("equal", "ls3", "ls4") == False:
            add_to_dictionary("equal", "ls3", "ls4");
            know_ls3();
            know_ls4();
        if check_dictionary("equal", "a2", "a6") == False:
            add_to_dictionary("equal", "a2", "a6");
            know_a2();
            know_a3();
        if check_dictionary("equal", "a4", "a6") == False:
            add_to_dictionary("equal", "a4", "a6");
            know_a2();
            know_a7();
        if check_dictionary("equal", "a8", "a4") == False:
            add_to_dictionary("equal", "a8", "a4");
            know_a8();
            know_a4();
        if check_dictionary("congruent", "ar4", "ar5") == False:
            add_to_dictionary("congruent", "ar4", "ar5");
            know_ar4();
            know_ar5();
        
        
    if check_dictionary("equal", "as4", "as6"):
        if check_dictionary("equal", "ls6", "ls7") == False:
            add_to_dictionary("equal", "ls6", "ls7");
            know_ls6();
            know_ls7();
        if check_dictionary("equal", "a8", "a3") == False:
            add_to_dictionary("equal", "a8", "a3");
            know_a8();
            know_a3();
        if check_dictionary("equal", "a7", "a6") == False:
            add_to_dictionary("equal", "a7", "a6");
            know_a7();
            know_a6();
        if check_dictionary("equal", "a7", "a8") == False:
            add_to_dictionary("equal", "a7", "a8");
            know_a7();
            know_a8();
        if check_dictionary("congruent", "ar6", "ar5") == False:
            add_to_dictionary("congruent", "ar6", "ar5");
            know_ar6();
            know_ar5();
        
        
    return

def know_as5():
    return

def know_as6():
    if check_dictionary("equal", "as4", "as6"):
        if check_dictionary("equal", "ls6", "ls7") == False:
            add_to_dictionary("equal", "ls6", "ls7");
            know_ls6();
            know_ls7();
        if check_dictionary("equal", "a8", "a3") == False:
            add_to_dictionary("equal", "a8", "a3");
            know_a8();
            know_a3();
        if check_dictionary("equal", "a7", "a6") == False:
            add_to_dictionary("equal", "a7", "a6");
            know_a7();
            know_a6();
        if check_dictionary("equal", "a7", "a8") == False:
            add_to_dictionary("equal", "a7", "a8");
            know_a7();
            know_a8();
        if check_dictionary("congruent", "ar6", "ar5") == False:
            add_to_dictionary("congruent", "ar6", "ar5");
            know_ar6();
            know_ar5();
        
        
    if check_dictionary("equal", "as2", "as6"):
        if check_dictionary("equal", "ls1", "ls9") == False:
            add_to_dictionary("equal", "ls1", "ls9");
            know_ls1();
            know_ls9();
        if check_dictionary("equal", "a2", "a3") == False:
            add_to_dictionary("equal", "a2", "a3");
            know_a2();
            know_a3();
        if check_dictionary("equal", "a2", "a7") == False:
            add_to_dictionary("equal", "a2", "a7");
            know_a2();
            know_a7();
        if check_dictionary("equal", "a3", "a4") == False:
            add_to_dictionary("equal", "a3", "a4");
            know_a3();
            know_a4();
        if check_dictionary("congruent", "ar4", "ar6") == False:
            add_to_dictionary("congruent", "ar4", "ar6");
            know_ar4();
            know_ar6();
        
        
    return

def know_as7():
    #circle circumference
    return

#AREAS

def know_ar1():
    
    return

def know_ar2():
    return

def know_ar3():
    return

def know_ar4():
    if check_dictionary("congruent", "ar4", "ar5") or check_dictionary("equal", "ar4", "ar5"):
        if check_dictionary("equal", "ls3", "ls4") == False:
            add_to_dictionary("equal", "ls3", "ls4");
            know_ls3();
            know_ls4();
        if check_dictionary("equal", "a2", "a6") == False:
            add_to_dictionary("equal", "a2", "a6");
            know_a2();
            know_a3();
        if check_dictionary("equal", "a4", "a6") == False:
            add_to_dictionary("equal", "a4", "a6");
            know_a2();
            know_a7();
        if check_dictionary("equal", "a8", "a4") == False:
            add_to_dictionary("equal", "a8", "a4");
            know_a8();
            know_a4();
        
        
        

    if check_dictionary("congruent", "ar4", "ar6") or check_dictionary("equal", "ar4", "ar6"):
        if check_dictionary("equal", "ls1", "ls9") == False:
            add_to_dictionary("equal", "ls1", "ls9");
            know_ls1();
            know_ls9();
        if check_dictionary("equal", "a2", "a3") == False:
            add_to_dictionary("equal", "a2", "a3");
            know_a2();
            know_a3();
        if check_dictionary("equal", "a2", "a7") == False:
            add_to_dictionary("equal", "a2", "a7");
            know_a2();
            know_a7();
        if check_dictionary("equal", "a3", "a4") == False:
            add_to_dictionary("equal", "a3", "a4");
            know_a3();
            know_a4();
        
        
        
    return

def know_ar5():
    if check_dictionary("congruent", "ar4", "ar5") or check_dictionary("equal", "ar4", "ar5"):
        if check_dictionary("equal", "ls3", "ls4") == False:
            add_to_dictionary("equal", "ls3", "ls4");
            know_ls3();
            know_ls4();
        if check_dictionary("equal", "a2", "a6") == False:
            add_to_dictionary("equal", "a2", "a6");
            know_a2();
            know_a3();
        if check_dictionary("equal", "a4", "a6") == False:
            add_to_dictionary("equal", "a4", "a6");
            know_a2();
            know_a7();
        if check_dictionary("equal", "a8", "a4") == False:
            add_to_dictionary("equal", "a8", "a4");
            know_a8();
            know_a4();
       

    if check_dictionary("congruent", "ar5", "ar6") or check_dictionary("equal", "ar5", "ar6"):
        if check_dictionary("equal", "ls6", "ls7") == False:
            add_to_dictionary("equal", "ls6", "ls7");
            know_ls6();
            know_ls7();
        if check_dictionary("equal", "a8", "a3") == False:
            add_to_dictionary("equal", "a8", "a3");
            know_a8();
            know_a3();
        if check_dictionary("equal", "a7", "a6") == False:
            add_to_dictionary("equal", "a7", "a6");
            know_a7();
            know_a6();
        if check_dictionary("equal", "a7", "a8") == False:
            add_to_dictionary("equal", "a7", "a8");
            know_a7();
            know_a8();
   
    return

def know_ar6():
    if check_dictionary("congruent", "ar4", "ar6") or check_dictionary("equal", "ar4", "ar6"):
        if check_dictionary("equal", "ls1", "ls9") == False:
            add_to_dictionary("equal", "ls1", "ls9");
            know_ls1();
            know_ls9();
        if check_dictionary("equal", "a2", "a3") == False:
            add_to_dictionary("equal", "a2", "a3");
            know_a2();
            know_a3();
        if check_dictionary("equal", "a2", "a7") == False:
            add_to_dictionary("equal", "a2", "a7");
            know_a2();
            know_a7();
        if check_dictionary("equal", "a3", "a4") == False:
            add_to_dictionary("equal", "a3", "a4");
            know_a3();
            know_a4();
        
        
        

    if check_dictionary("congruent", "ar5", "ar6") or check_dictionary("equal", "ar5", "ar6"):
        if check_dictionary("equal", "ls6", "ls7") == False:
            add_to_dictionary("equal", "ls6", "ls7");
            know_ls6();
            know_ls7();
        if check_dictionary("equal", "a8", "a3") == False:
            add_to_dictionary("equal", "a8", "a3");
            know_a8();
            know_a3();
        if check_dictionary("equal", "a7", "a6") == False:
            add_to_dictionary("equal", "a7", "a6");
            know_a7();
            know_a6();
        if check_dictionary("equal", "a7", "a8") == False:
            add_to_dictionary("equal", "a7", "a8");
            know_a7();
            know_a8();
   
    return

def know_ar7():
    return

def know_ar8():
    return

def know_ar9():
    return

def know_call(name1, name2):
    if(name1 == 'ls1' or name2 == 'ls1'):
        know_ls1()
    if(name1 == 'ls2' or name2 == 'ls2'):
        know_ls2()
    if(name1 == 'ls3' or name2 == 'ls3'):
        know_ls3()
    if(name1 == 'ls4' or name2 == 'ls4'):
        know_ls4()
    if(name1 == 'ls5' or name2 == 'ls5'):
        know_ls5()
    if(name1 == 'ls6' or name2 == 'ls6'):
        know_ls6()
    if(name1 == 'ls7' or name2 == 'ls7'):
        know_ls7()
    if(name1 == 'ls8' or name2 == 'ls8'):
        know_ls8()
    if(name1 == 'ls9' or name2 == 'ls9'):
        know_ls9()
    if(name1 == 'ls10' or name2 == 'ls10'):
        know_ls10()
    if(name1 == 'ls11' or name2 == 'ls11'):
        know_ls11()
    if(name1 == 'ls12' or name2 == 'ls12'):
        know_ls12()
    #ARCS
    if(name1 == 'as1' or name2 == 'as1'):
        know_as1()
    if(name1 == 'as2' or name2 == 'as2'):
        know_as2()
    if(name1 == 'as3' or name2 == 'as3'):
        know_as3()
    if(name1 == 'as4' or name2 == 'as4'):
        know_as4()
    if(name1 == 'as5' or name2 == 'as5'):
        know_as5()
    if(name1 == 'as6' or name2 == 'as6'):
        know_as6()
    if(name1 == 'as7' or name2 == 'as7'):
        know_as7()
        
    #ANGLES
    if(name1 == 'a1' or name2 == 'a1'):
        know_a1()
    if(name1 == 'a2' or name2 == 'a2'):
        know_a2()
    if(name1 == 'a3' or name2 == 'a3'):
        know_a3()
    if(name1 == 'a4' or name2 == 'a4'):
        know_a4()
    if(name1 == 'a5' or name2 == 'a5'):
        know_a5()
    if(name1 == 'a6' or name2 == 'a6'):
        know_a6()
    if(name1 == 'a7' or name2 == 'a7'):
        know_a7()
    if(name1 == 'a8' or name2 == 'a8'):
        know_a8()
    if(name1 == 'a9' or name2 == 'a9'):
        know_a9()
    if(name1 == 'b1' or name2 == 'b1'):
        know_b1()
    if(name1 == 'b2' or name2 == 'b2'):
        know_b2()
    if(name1 == 'b3' or name2 == 'b3'):
        know_b3()
    if(name1 == 'b4' or name2 == 'b4'):
        know_b4()
    if(name1 == 'b5' or name2 == 'b5'):
        know_b5()
    if(name1 == 'b6' or name2 == 'b6'):
        know_b6()
    if(name1 == 'c1' or name2 == 'c1'):
        know_c1()
    if(name1 == 'c2' or name2 == 'c2'):
        know_c2()
    if(name1 == 'c3' or name2 == 'c3'):
        know_c3()
    if(name1 == 'c4' or name2 == 'c4'):
        know_c4()
    if(name1 == 'c5' or name2 == 'c5'):
        know_c5()
    if(name1 == 'c6' or name2 == 'c6'):
        know_c6()
    if(name1 == 'd1' or name2 == 'd1'):
        know_d1()
    if(name1 == 'd2' or name2 == 'd2'):
        know_d2()
    if(name1 == 'd3' or name2 == 'd3'):
        know_d3()
    if(name1 == 'd4' or name2 == 'd4'):
        know_d4()
    if(name1 == 'd5' or name2 == 'd5'):
        know_d5()
    if(name1 == 'd6' or name2 == 'd6'):
        know_d6()
        
    #AREAS
    if(name1 == 'ar1' or name2 == 'ar1'):
        know_ar1()
    if(name1 == 'ar2' or name2 == 'ar2'):
        know_ar2()
    if(name1 == 'ar3' or name2 == 'ar3'):
        know_ar3()
    if(name1 == 'ar4' or name2 == 'ar4'):
        know_ar4()
    if(name1 == 'ar5' or name2 == 'ar5'):
        know_ar5()
    if(name1 == 'ar6' or name2 == 'ar6'):
        know_ar6()
    if(name1 == 'ar7' or name2 == 'ar7'):
        know_ar7()
    if(name1 == 'ar8' or name2 == 'ar8'):
        know_ar8()
    if(name1 == 'ar9' or name2 == 'ar9'):
        know_ar9()
#output

def get_all():
    if(null.flag):
        return 'null'
    dictionary_keys = list(dictionary.keys())
    for key in dictionary_keys:
        if(dictionary[key] == []):
            del dictionary[key]
    return dictionary
