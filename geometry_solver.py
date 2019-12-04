#
#   Geometry Solver
#

lines = ['ls1','ls2','ls3','ls4','ls5','ls6','ls7','ls8','ls9','ls10','ls11','ls12']
arcs = ['as1','as2','as3','as4','as5','as6','as7']
areas = ['ar1','ar2','ar3','ar4','ar5','ar6','ar7','ar8','ar9']
angles = ['a1','a2','a3','a4','a5','a6','a7','a8','a9','b1','b2','b3','b4','b5','b6','c1','c2','c3','c4','c5','c6','d1','d2','d3','d4','d5','d6']

dictionary = {}

def add_to_dictionary(key, name1, name2, value='NULL'):
    dictionary.setdefault(key,[])
    newList = dictionary[key]
    if(key == 'fraction' or key == 'sum_value'):
        newList.append([name1,name2,value])
    else:
        newList.append([name1,name2])
    dictionary[key] = newList

def check_dictionary(key, name1, name2, value='NULL'):
    # if exists return true
    # else return null/false

#Predicates

def set_parallel(name1, name2):
    if(name1 in ['ls1','ls2','ls3','ls10']):
        if(name2 in ['ls1','ls2','ls3','ls10']):
            #do nothing
            return
        elif(name2 in ['ls4','ls5','ls6','ls11']):
            #set a5, ar1, ar2, ar3, ar7, ar8 to zero
            #   also a1 if ls1 > 0
            return
        elif(name2 in ['ls7','ls8','ls9','ls12']):
            #set a1, ar1, ar2, ar3, ar7, ar8 to zero
            #   also a5 if ls3 > 0
            return
        else:
            #NULL
            return
    elif(name1 in ['ls4','ls5','ls6','ls11']):
        if(name2 in ['ls1','ls2','ls3','ls10']):
            #set a5, ar1, ar2, ar3, ar7, ar8 to zero
            #   also a1 if ls1 > 0
            return
        elif(name2 in ['ls4','ls5','ls6','ls11']):
            #do nothing
            return
        elif(name2 in ['ls7','ls8','ls9','ls12']):
            #set a9, ar1, ar2, ar3, ar7, ar8 to zero
            #   also a1 if ls9 > 0
            return
        else:
            #NULL
            return
    elif(name1 in ['ls7','ls8','ls9','ls12']):
        if(name2 in ['ls1','ls2','ls3','ls10']):
            #set a1, ar1, ar2, ar3, ar7, ar8 to zero
            #   also a5 if ls3 > 0
            return
        elif(name2 in ['ls4','ls5','ls6','ls11']):
            #set a9, ar1, ar2, ar3, ar7, ar8 to zero
            #   also a1 if ls9 > 0
            return
        elif(name2 in ['ls7','ls8','ls9','ls12']):
            #do nothing
            return
        else:
            #NULL
            return
    else:
        #NULL? or make circle a line -> triangle a line
        return
    return

def set_perpendicular(name1, name2):
    if(name1 in ['ls1','ls2','ls3','ls10']):
        if(name2 in ['ls1','ls2','ls3','ls10']):
            #NULL
            return
        elif(name2 in ['ls4','ls5','ls6','ls11']):
            #
            return
        elif(name2 in ['ls7','ls8','ls9','ls12']):
            #
            return
        else:
            #NULL
            return
    elif(name1 in ['ls4','ls5','ls6','ls11']):
        if(name2 in ['ls1','ls2','ls3','ls10']):
            #
            return
        elif(name2 in ['ls4','ls5','ls6','ls11']):
            #NULL
            return
        elif(name2 in ['ls7','ls8','ls9','ls12']):
            #
            return
        else:
            #NULL
            return
    elif(name1 in ['ls7','ls8','ls9','ls12']):
        if(name2 in ['ls1','ls2','ls3','ls10']):
            #
            return
        elif(name2 in ['ls4','ls5','ls6','ls11']):
            #
            return
        elif(name2 in ['ls7','ls8','ls9','ls12']):
            #NULL
            return
        else:
            #NULL
            return
    return

def set_equal(name1, name2):
    if(name1 == 'ls1'):
        if(name2 == 'ls9'):
            #a2 == a3, a2 == b1, a3 == b6
            return
    elif(name1 == 'ls2'):
        if(name2 == 'ls5'):
            #as2 == as4
            #check if ls8 is equal
            return
        if(name2 == 'ls8'):
            #as2 == as6
            #check if ls5 is equal
            return
    elif(name1 == 'ls3'):
        if(name2 == 'ls4'):
            #a4 == a6
            return
        return
    elif(name1 == 'ls4'):
        if(name2 == 'ls3'):
            #a4 == a6
            return
        return
    elif(name1 == 'ls5'):
        if(name2 == 'ls2'):
            #as4 == as2
            #check if ls5 is equal
            return
        if(name2 == 'ls8'):
            #as4 == as6
            #check if ls2 is equal
            return
        return
    elif(name1 == 'ls6'):
        if(name2 == 'ls7'):
            #a7 == a8
            return
        return
    elif(name1 == 'ls7'):
        if(name2 == 'ls6'):
            #a7 == a8
            return
        return
    elif(name1 == 'ls8'):
        if(name2 == 'ls2'):
            #as6 == as2
            #check if ls5 is equal
            return
        if(name2 == 'ls5'):
            #as6 == as4
            #check if ls2 is equal
            return
        return
    elif(name1 == 'ls9'):
        if(name2 == 'ls1'):
            #a2 == a3
            return
        return
    elif(name1 == 'ls10'):
        if(name2 == 'ls11'):
            #a1 == a9
            return
        if(name2 == 'ls12'):
            #a5 == a9
            return
        return
    elif(name1 == 'ls11'):
        if(name2 == 'ls10'):
            #a1 == a9
            return
        if(name2 == 'ls12'):
            #a1 == a5
            return
        return
    elif(name1 == 'ls12'):
        if(name2 == 'ls10'):
            #a5 == a9
            return
        if(name2 == 'ls11'):
            #a1 == a9
            return
        return
    #ARCS
    elif(name1 == 'as1'):
        if(name2 == 'as3'):
            #a1 == a5 ?
            return
        if(name2 == 'as5'):
            #a1 == a9 ?
            return
        return
    elif(name1 == 'as2'):
        if(name2 == 'as4'):
            #ls2 == ls5
            #ar4 == ar5
            return
        if(name2 == 'as6'):
            #ls2 == ls8
            #ar4 == ar6
            return
        return
    elif(name1 == 'as3'):
        if(name2 == 'as1'):
            #a5 == a1 ?
            return
        if(name2 == 'as5'):
            #a5 == a9 ?
            return
        return
    elif(name1 == 'as4'):
        if(name2 == 'as2'):
            #ls5 == ls2
            #ar5 == ar4
            return
        if(name2 == 'as6'):
            #ls5 == ls8
            #ar5 == ar6
            return
        return
    elif(name1 == 'as5'):
        if(name2 == 'as1'):
            #a9 == a1 ?
            return
        if(name2 == 'as3'):
            #a9 == a5 ?
            return
        return
    elif(name1 == 'as6'):
        if(name2 == 'as2'):
            #ls8 == ls2
            #ar6 == ar4
            return
        if(name2 == 'as4'):
            #ls8 == ls5
            #ar6 == ar5
            return
        return
    elif(name1 == 'as7'):
        #?
        return
    #AREAS
    elif(name1 == 'ar1'):
        return
    elif(name1 == 'ar2'):
        return
    elif(name1 == 'ar3'):
        return
    elif(name1 == 'ar4'):
        if(name2 == 'ar5'):
            #check ls3 == ls4 or a4 == a6
            #   ar4 is congruent to ar5
            return
        elif(name2 == 'ar6'):
            #check ls1 == ls9 or a2 == a3
            #   ar4 is congruent to ar6
            return
        return
    elif(name1 == 'ar5'):
        return
    elif(name1 == 'ar6'):
        return
    elif(name1 == 'ar7'):
        return
    elif(name1 == 'ar8'):
        return
    #ANGLES
    elif(name1 == 'a1'):
        if(name2 == 'a5'):
            #ls11 == ls12
            return
        elif(name2 == 'a9'):
            #ls10 == ls12
            return
        return
    elif(name1 == 'a2'):
        if(name2 == 'a3'):
            #ls1 == ls9
            return
        return
    elif(name1 == 'a3'):
        if(name2 == 'a2'):
            #ls1 == ls9
            return
        return
    elif(name1 == 'a4'):
        if(name2 == 'a6'):
            #ls3 == ls4
            return
        return
    elif(name1 == 'a5'):
        if(name2 == 'a1'):
            #ls11 == ls12
            return
        elif(name2 == 'a9'):
            #ls10 == ls12
            return
        return
    elif(name1 == 'a6'):
        if(name2 == 'a4'):
            #ls3 == ls4
            return
        return
    elif(name1 == 'a7'):
        if(name2 == 'a8'):
            #ls6 == ls7
            return
        return
    elif(name1 == 'a8'):
        if(name2 == 'a7'):
            #ls6 == ls7
            return
        return
    elif(name1 == 'a9'):
        if(name2 == 'a1'):
            #ls10 == ls11
            return
        elif(name2 == 'a5'):
            #ls10 == ls12
            return
        return
    elif(name1 == 'b1'):
        if(name2 == 'c1' or name2 == 'd1'):
            #b1 = c1 = d1 = a2 = 90
            #set_sum_value_value(b1, c1, 180)
            #set_sum_value_value(b1, d1, 180)
            return
        return
    elif(name1 == 'b2'):
        if(name2 == 'c2' or name2 == 'd2'):
            #b2 = c2 = d2 = a4 = 90
            #set_sum_value_value(b2, c2, 180)
            #set_sum_value_value(b2, d2, 180)
            return
        return
    elif(name1 == 'b3'):
        if(name2 == 'c3' or name2 == 'd3'):
            #b3 = c3 = d3 = a6 = 90
            #set_sum_value_value(b3, c3, 180)
            #set_sum_value_value(b3, d3, 180)
            return
        return
    elif(name1 == 'b4'):
        if(name2 == 'c4' or name2 == 'd4'):
            #b4 = c4 = d4 = a8 = 90
            #set_sum_value_value(b4, c4, 180)
            #set_sum_value_value(b4, d4, 180)
            return
        return
    elif(name1 == 'b5'):
        if(name2 == 'c5' or name2 == 'd5'):
            #b5 = c5 = d5 = a7 = 90
            #set_sum_value_value(b5, c5, 180)
            #set_sum_value_value(b5, d5, 180)
            return
        return
    elif(name1 == 'b6'):
        if(name2 == 'c6' or name2 == 'd6'):
            #b6 = c6 = d6 = a3 = 90
            #set_sum_value_value(b6, c6, 180)
            #set_sum_value_value(b6, d6, 180)
            return
        return
    elif(name1 == 'c1'):
        if(name2 == 'b1' or name2 == 'a2'):
            #b1 = c1 = d1 = a2 = 90
            return
        return
    elif(name1 == 'c2'):
        if(name2 == 'b2' or name2 == 'a4'):
            #b2 = c2 = d2 = a4 = 90
            return
        return
    elif(name1 == 'c3'):
        if(name2 == 'b3' or name2 == 'a6'):
            #b3 = c3 = d3 = a6 = 90
            return
        return
    elif(name1 == 'c4'):
        if(name2 == 'b4' or name2 == 'a8'):
            #b4 = c4 = d4 = a8 = 90
            return
        return
    elif(name1 == 'c5'):
        if(name2 == 'b5' or name2 == 'a7'):
            #b5 = c5 = d5 = a7 = 90
            return
        return
    elif(name1 == 'c6'):
        if(name2 == 'b6' or name2 == 'a3'):
            #b6 = c6 = d6 = a3 = 90
            return
        return
    elif(name1 == 'd1'):
        if(name2 == 'b1' or name2 == 'a2'):
            #b1 = c1 = d1 = a2 = 90
            return
        return
    elif(name1 == 'd2'):
        if(name2 == 'b2' or name2 == 'a4'):
            #b2 = c2 = d2 = a4 = 90
            return
        return
    elif(name1 == 'd3'):
        if(name2 == 'b3' or name2 == 'a6'):
            #b3 = c3 = d3 = a6 = 90
            return
        return
    elif(name1 == 'd4'):
        if(name2 == 'b4' or name2 == 'a8'):
            #b4 = c4 = d4 = a8 = 90
            return
        return
    elif(name1 == 'd5'):
        if(name2 == 'b5' or name2 == 'a7'):
            #b5 = c5 = d5 = a7 = 90
            return
        return
    elif(name1 == 'd6'):
        if(name2 == 'b6' or name2 == 'a3'):
            #b6 = c6 = d6 = a3 = 90
            return
        return

def set_fraction(name1, name2, fraction):
    return

def set_sum_value(name1, name2, sum_value):
    return

def set_tan(name1, name2):
    return

#NOT INPUTS
def set_similar(name1, name2):
    return

def set_congruent(name1, name2):
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
        
    return

def know_a2():
    if check_dictionary("equal", "a2", "b1") == False :
        add_to_dictionary("equal", "a2", "b1");
        know_b1();
    return

def know_a3():
    if check_dictionary("equal", "a3", "b6") == False :
        add_to_dictionary("equal", "a3", "b6");
        know_b6();
    return

def know_a4():
    if check_dictionary("equal", "a4", "b2") == False :
        add_to_dictionary("equal", "a4", "b2");
        know_b2();
    return

def know_a5():
    if check_dictionary("sum_value", "a5", "a9", 90) == False and check_dictionary("perpendicular", "ls10", "ls12"):
        add_to_dictionary("sum_value", "a5", "a9", 90);
        know_a9();
    if check_dictionary("sum_value", "a5", "a1", 90) == False and check_dictionary("perpendicular", "ls12", "ls11"):
        add_to_dictionary("sum_value", "a5", "a1", 90);
        know_a1();
    return

def know_a6():
    if check_dictionary("equal", "a6", "b3") == False :
        add_to_dictionary("equal", "a6", "b3");
        know_b3();
    return

def know_a7():
    if check_dictionary("equal", "a7", "b5") == False :
        add_to_dictionary("equal", "a7", "b5");
        know_b5();
    return

def know_a8():
    if check_dictionary("equal", "a8", "b4") == False :
        add_to_dictionary("equal", "a8", "b4");
        know_b4();
    return

def know_a9():
    if check_dictionary("sum_value", "a1", "a9", 90) == False and check_dictionary("perpendicular", "ls10", "ls11"):
        add_to_dictionary("sum_value", "a1", "a9", 90);
        know_a1();
        if check_dictionary("sum_value", "a5", "a9", 90) == False and check_dictionary("perpendicular", "ls10", "ls12"):
        add_to_dictionary("sum_value", "a5", "a9", 90);
        know_a5();
    return

def know_b1():
    if check_dictionary("equal", "b1", "a2") == False :
        add_to_dictionary("equal", "b1", "a2");
        know_a2();

    
    return

def know_b2():
    if check_dictionary("equal", "b2", "a4") == False :
        add_to_dictionary("equal", "b2", "a4");
        know_a4();    
    return

def know_b3():
    if check_dictionary("equal", "b3", "a6") == False :
        add_to_dictionary("equal", "b3", "a6");
        know_a6();
    return

def know_b4():
    if check_dictionary("equal", "b4", "a8") == False :
        add_to_dictionary("equal", "b4", "a8");
        know_a8();
    return

def know_b5():
    if check_dictionary("equal", "b5", "a7") == False :
        add_to_dictionary("equal", "b5", "a7");
        know_a7();
    return

def know_b6():
    if check_dictionary("equal", "b6", "a3") == False :
        add_to_dictionary("equal", "b6", "a3");
        know_a3();
    return

def know_c1():
    if check_dictionary("equal", "c1", "d1") == False :
        add_to_dictionary("equal", "c1", "d1");
        know_d1();
    return

def know_c2():
    if check_dictionary("equal", "c2", "d2") == False :
        add_to_dictionary("equal", "c2", "d2");
        know_d2();
    return

def know_c3():
    if check_dictionary("equal", "c3", "d3") == False :
        add_to_dictionary("equal", "c3", "d3");
        know_d3();
    return

def know_c4():
    if check_dictionary("equal", "c4", "d4") == False :
        add_to_dictionary("equal", "c4", "d4");
        know_d4();
    return

def know_c5():
    if check_dictionary("equal", "c5", "d5") == False :
        add_to_dictionary("equal", "c5", "d5");
        know_d5();
    return

def know_c6():
    if check_dictionary("equal", "c6", "d6") == False :
        add_to_dictionary("equal", "c6", "d6");
        know_d6();
    return

def know_d1():
    if check_dictionary("equal", "c1", "d1") == False :
        add_to_dictionary("equal", "c1", "d1");
        know_c1();
    return

def know_d2():
    if check_dictionary("equal", "c2", "d2") == False :
        add_to_dictionary("equal", "c2", "d2");
        know_c2();
    return

def know_d3():
    if check_dictionary("equal", "c3", "d3") == False :
        add_to_dictionary("equal", "c3", "d3");
        know_c3();
    return

def know_d4():
    if check_dictionary("equal", "c4", "d4") == False :
        add_to_dictionary("equal", "c4", "d4");
        know_c4();
    return

def know_d5():
    if check_dictionary("equal", "c5", "d5") == False :
        add_to_dictionary("equal", "c5", "d5");
        know_c5();
    return

def know_d6():
    if check_dictionary("equal", "c6", "d6") == False :
        add_to_dictionary("equal", "c6", "d6");
        know_c6();
    return

#LINE SEGMENTS

def know_ls1():
    if check_dictionary("equal", "a2", "a3") == True and check_dictionary("equal", "ls1", "ls9") == False :
        add_to_dictionary("equal", "ls1", "ls9");
        know_ls9();

    if check_dictionary("perpendicular", "ls10", "ls11") == False and check_dictionary("perpendicular", "ls1", "ls11"):
        add_to_dictionary("perpendicular", "ls10", "ls11");
        know_ls11();
    if check_dictionary("perpendicular", "ls10", "ls12") == False and check_dictionary("perpendicular", "ls1", "ls12"):
        add_to_dictionary("perpendicular", "ls10", "ls12");
        know_ls12();
    return

def know_ls2():
    if check_dictionary("perpendicular", "ls10", "ls11") == False and check_dictionary("perpendicular", "ls2", "ls11"):
        add_to_dictionary("perpendicular", "ls10", "ls11");
        know_ls11();
    if check_dictionary("perpendicular", "ls10", "ls12") == False and check_dictionary("perpendicular", "ls2", "ls12"):
        add_to_dictionary("perpendicular", "ls10", "ls12");
        know_ls12();
    return

def know_ls3():
    if check_dictionary("equal", "a4", "a6") == True and check_dictionary("equal", "ls3", "ls4") == False :
        add_to_dictionary("equal", "ls3", "ls4");
        know_ls4();

    if check_dictionary("perpendicular", "ls10", "ls11") == False and check_dictionary("perpendicular", "ls3", "ls11"):
        add_to_dictionary("perpendicular", "ls10", "ls11");
        know_ls11();
    if check_dictionary("perpendicular", "ls10", "ls12") == False and check_dictionary("perpendicular", "ls3", "ls12"):
        add_to_dictionary("perpendicular", "ls10", "ls12");
        know_ls12();
    return

def know_ls4():
    if check_dictionary("equal", "a4", "a6") == True and check_dictionary("equal", "ls3", "ls4") == False :
        add_to_dictionary("equal", "ls3", "ls4");
        know_ls3();

    if check_dictionary("perpendicular", "ls10", "ls11") == False and check_dictionary("perpendicular", "ls4", "ls10"):
        add_to_dictionary("perpendicular", "ls10", "ls11");
        know_ls10();
    if check_dictionary("perpendicular", "ls11", "ls12") == False and check_dictionary("perpendicular", "ls4", "ls12"):
        add_to_dictionary("perpendicular", "ls11", "ls12");
        know_ls12();
    return

def know_ls5():
    if check_dictionary("perpendicular", "ls10", "ls11") == False and check_dictionary("perpendicular", "ls5", "ls10"):
        add_to_dictionary("perpendicular", "ls10", "ls11");
        know_ls10();
    if check_dictionary("perpendicular", "ls11", "ls12") == False and check_dictionary("perpendicular", "ls5", "ls12"):
        add_to_dictionary("perpendicular", "ls11", "ls12");
    return

def know_ls6():
    if check_dictionary("equal", "a7", "a8") == True and check_dictionary("equal", "ls6", "ls7") == False :
        add_to_dictionary("equal", "ls6", "ls7");
        know_ls7();

    if check_dictionary("perpendicular", "ls10", "ls11") == False and check_dictionary("perpendicular", "ls6", "ls10"):
        add_to_dictionary("perpendicular", "ls10", "ls11");
        know_ls10();
    if check_dictionary("perpendicular", "ls11", "ls12") == False and check_dictionary("perpendicular", "ls6", "ls12"):
        add_to_dictionary("perpendicular", "ls11", "ls12");
    return

def know_ls7():
    if check_dictionary("equal", "a7", "a8") == True and check_dictionary("equal", "ls6", "ls7") == False:
        add_to_dictionary("equal", "ls6", "ls7");
        know_ls6();
    return

if check_dictionary("perpendicular", "ls10", "ls12") == False and check_dictionary("perpendicular", "ls7", "ls10"):
        add_to_dictionary("perpendicular", "ls10", "ls12");
        know_ls10();
    if check_dictionary("perpendicular", "ls11", "ls12") == False and check_dictionary("perpendicular", "ls7", "ls11"):
        add_to_dictionary("perpendicular", "ls11", "ls12");

def know_ls8():
    if check_dictionary("perpendicular", "ls10", "ls12") == False and check_dictionary("perpendicular", "ls8", "ls10"):
        add_to_dictionary("perpendicular", "ls10", "ls12");
        know_ls10();
    if check_dictionary("perpendicular", "ls11", "ls12") == False and check_dictionary("perpendicular", "ls8", "ls11"):
        add_to_dictionary("perpendicular", "ls11", "ls12");
    return

def know_ls9():
    if check_dictionary("equal", "a2", "a3") == True and check_dictionary("equal", "ls1", "ls9") == False:
        add_to_dictionary("equal", "ls1", "ls9");
        know_ls1();

    if check_dictionary("perpendicular", "ls10", "ls12") == False and check_dictionary("perpendicular", "ls9", "ls10"):
        add_to_dictionary("perpendicular", "ls10", "ls12");
        know_ls10();
    if check_dictionary("perpendicular", "ls11", "ls12") == False and check_dictionary("perpendicular", "ls9", "ls11"):
        add_to_dictionary("perpendicular", "ls11", "ls12");
    return

def know_ls10():
    if check_dictionary("perpendicular", "ls10", "ls11") :
        if check_dictionary("perpendicular", "ls10", "ls4") == False:
            add_to_dictionary("perpendicular", "ls10", "ls4");
        if check_dictionary("perpendicular", "ls4", "ls3") == False:
            add_to_dictionary("perpendicular", "ls4", "ls3");
        if check_dictionary("perpendicular", "ls4", "ls2") == False:
            add_to_dictionary("perpendicular", "ls4", "ls2");
        if check_dictionary("perpendicular", "ls4", "ls1") == False:
            add_to_dictionary("perpendicular", "ls4", "ls1");
        if check_dictionary("perpendicular", "ls10", "ls5") == False:
            add_to_dictionary("perpendicular", "ls10", "ls5");
        if check_dictionary("perpendicular", "ls5", "ls3") == False:
            add_to_dictionary("perpendicular", "ls5", "ls3");
        if check_dictionary("perpendicular", "ls5", "ls2") == False:
            add_to_dictionary("perpendicular", "ls5", "ls2");
        if check_dictionary("perpendicular", "ls5", "ls1") == False:
            add_to_dictionary("perpendicular", "ls5", "ls1");
        if check_dictionary("perpendicular", "ls10", "ls6") == False:
            add_to_dictionary("perpendicular", "ls10", "ls6");
        if check_dictionary("perpendicular", "ls6", "ls3") == False:
            add_to_dictionary("perpendicular", "ls6", "ls3");
        if check_dictionary("perpendicular", "ls6", "ls2") == False:
            add_to_dictionary("perpendicular", "ls6", "ls2");
        if check_dictionary("perpendicular", "ls6", "ls1") == False:
            add_to_dictionary("perpendicular", "ls6", "ls1");

        
        if check_dictionary("perpendicular", "ls11", "ls1") == False:
            add_to_dictionary("perpendicular", "ls11", "ls1");
        if check_dictionary("perpendicular", "ls1", "ls4") == False:
            add_to_dictionary("perpendicular", "ls1", "ls4");
        if check_dictionary("perpendicular", "ls1", "ls5") == False:
            add_to_dictionary("perpendicular", "ls1", "ls5");
        if check_dictionary("perpendicular", "ls1", "ls6") == False:
            add_to_dictionary("perpendicular", "ls1", "ls6");
        if check_dictionary("perpendicular", "ls11", "ls2") == False:
            add_to_dictionary("perpendicular", "ls11", "ls2");
        if check_dictionary("perpendicular", "ls2", "ls4") == False:
            add_to_dictionary("perpendicular", "ls2", "ls4");
        if check_dictionary("perpendicular", "ls2", "ls5") == False:
            add_to_dictionary("perpendicular", "ls2", "ls5");
        if check_dictionary("perpendicular", "ls2", "ls6") == False:
            add_to_dictionary("perpendicular", "ls2", "ls6");
        if check_dictionary("perpendicular", "ls11", "ls3") == False:
            add_to_dictionary("perpendicular", "ls11", "ls3");
        if check_dictionary("perpendicular", "ls3", "ls4") == False:
            add_to_dictionary("perpendicular", "ls3", "ls4");
        if check_dictionary("perpendicular", "ls3", "ls5") == False:
            add_to_dictionary("perpendicular", "ls3", "ls5");
        if check_dictionary("perpendicular", "ls3", "ls6") == False:
            add_to_dictionary("perpendicular", "ls3", "ls6");
        know_ls1();
        know_ls2();
        know_ls3();
        know_ls4();
        know_ls5();
        know_ls6();
        know_ls11();
        
    if check_dictionary("perpendicular", "ls10", "ls12") :
        if check_dictionary("perpendicular", "ls10", "ls7") == False:
            add_to_dictionary("perpendicular", "ls10", "ls7");
        if check_dictionary("perpendicular", "ls7", "ls3") == False:
            add_to_dictionary("perpendicular", "ls7", "ls3");
        if check_dictionary("perpendicular", "ls7", "ls2") == False:
            add_to_dictionary("perpendicular", "ls7", "ls2");
        if check_dictionary("perpendicular", "ls7", "ls1") == False:
            add_to_dictionary("perpendicular", "ls7", "ls1");
        if check_dictionary("perpendicular", "ls10", "ls8") == False:
            add_to_dictionary("perpendicular", "ls10", "ls8");
        if check_dictionary("perpendicular", "ls8", "ls3") == False:
            add_to_dictionary("perpendicular", "ls8", "ls3");
        if check_dictionary("perpendicular", "ls8", "ls2") == False:
            add_to_dictionary("perpendicular", "ls8", "ls2");
        if check_dictionary("perpendicular", "ls8", "ls1") == False:
            add_to_dictionary("perpendicular", "ls8", "ls1");
        if check_dictionary("perpendicular", "ls10", "ls9") == False:
            add_to_dictionary("perpendicular", "ls10", "ls9");
        if check_dictionary("perpendicular", "ls9", "ls3") == False:
            add_to_dictionary("perpendicular", "ls9", "ls3");
        if check_dictionary("perpendicular", "ls9", "ls2") == False:
            add_to_dictionary("perpendicular", "ls9", "ls2");
        if check_dictionary("perpendicular", "ls9", "ls1") == False:
            add_to_dictionary("perpendicular", "ls9", "ls1");

        
        if check_dictionary("perpendicular", "ls12", "ls1") == False:
            add_to_dictionary("perpendicular", "ls12", "ls1");
        if check_dictionary("perpendicular", "ls1", "ls7") == False:
            add_to_dictionary("perpendicular", "ls1", "ls7");
        if check_dictionary("perpendicular", "ls1", "ls8") == False:
            add_to_dictionary("perpendicular", "ls1", "ls8");
        if check_dictionary("perpendicular", "ls1", "ls9") == False:
            add_to_dictionary("perpendicular", "ls1", "ls9");
        if check_dictionary("perpendicular", "ls12", "ls2") == False:
            add_to_dictionary("perpendicular", "ls12", "ls2");
        if check_dictionary("perpendicular", "ls2", "ls7") == False:
            add_to_dictionary("perpendicular", "ls2", "ls7");
        if check_dictionary("perpendicular", "ls2", "ls8") == False:
            add_to_dictionary("perpendicular", "ls2", "ls8");
        if check_dictionary("perpendicular", "ls2", "ls9") == False:
            add_to_dictionary("perpendicular", "ls2", "ls9");
        if check_dictionary("perpendicular", "ls12", "ls3") == False:
            add_to_dictionary("perpendicular", "ls12", "ls3");
        if check_dictionary("perpendicular", "ls3", "ls7") == False:
            add_to_dictionary("perpendicular", "ls3", "ls7");
        if check_dictionary("perpendicular", "ls3", "ls8") == False:
            add_to_dictionary("perpendicular", "ls3", "ls8");
        if check_dictionary("perpendicular", "ls3", "ls9") == False:
            add_to_dictionary("perpendicular", "ls3", "ls9");
        know_ls1();
        know_ls2();
        know_ls3();
        know_ls7();
        know_ls8();
        know_ls9();
        know_ls12();
    return

def know_ls11():
    #too tired to continue
    return

def know_ls12():
    return

#ARC SEGMENTS

def know_as1():
    return

def know_as2():
    if check_dictionary("equal", "as2", "as4") and check_dictionary("equal", "ls2", "ls5") == False:
        add_to_dictionary("equal", "ls2", "ls5");
        add_to_dictionary("equal", "ar4", "ar5");
        add_to_dictionary("congruent", "ar4", "ar5");
        know_ls2();
        know_ls5();
        know_a4();
        know_a5();
    if check_dictionary("equal", "as2", "as6") and check_dictionary("equal", "ls2", "ls8") == False:
        add_to_dictionary("equal", "ls2", "ls8");
        add_to_dictionary("equal", "ar4", "ar6");
        add_to_dictionary("congruent", "ar4", "ar6");
        know_ls2();
        know_ls8();
        know_a4();
        know_a6();
    return

def know_as3():
    return

def know_as4():
    if check_dictionary("equal", "as2", "as4") and check_dictionary("equal", "ls2", "ls5") == False:
        add_to_dictionary("equal", "ls2", "ls5");
        add_to_dictionary("equal", "ar4", "ar5");
        add_to_dictionary("congruent", "ar4", "ar5");
        know_ls2();
        know_ls5();
        know_a4();
        know_a5();
    if check_dictionary("equal", "as4", "as6") and check_dictionary("equal", "ls5", "ls8") == False:
        add_to_dictionary("equal", "ls5", "ls8");
        add_to_dictionary("equal", "ar5", "ar6");
        add_to_dictionary("congruent", "ar5", "ar6");
        know_ls5();
        know_ls8();
        know_a5();
        know_a6();
    return

def know_as5():
    return

def know_as6():
    if check_dictionary("equal", "as4", "as6") and check_dictionary("equal", "ls5", "ls8") == False:
        add_to_dictionary("equal", "ls5", "ls8");
        add_to_dictionary("equal", "ar5", "ar6");
        add_to_dictionary("congruent", "ar5", "ar6");
        know_ls5();
        know_ls8();
        know_a5();
        know_a6();
    if check_dictionary("equal", "as2", "as6") and check_dictionary("equal", "ls2", "ls8") == False:
        add_to_dictionary("equal", "ls2", "ls8");
        add_to_dictionary("equal", "ar4", "ar6");
        add_to_dictionary("congruent", "ar4", "ar6");
        know_ls2();
        know_ls8();
        know_a4();
        know_a6();
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
    return

def know_ar5():
    return

def know_ar6():
    return

def know_ar7():
    return

def know_ar8():
    return

def know_ar9():
    return

#output

def get_all():
    dictionary = {'equal':[['ls1','ls2'],['ls1','ls3']]}
    return dictionary
