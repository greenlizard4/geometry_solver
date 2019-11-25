#
#   Geometry Solver
#

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
    return

def know_a2():
    return

def know_a3():
    return

def know_a4():
    return

def know_a5():
    return

def know_a6():
    return

def know_a7():
    return

def know_a8():
    return

def know_a9():
    return

def know_b1():
    return

def know_b2():
    return

def know_b3():
    return

def know_b4():
    return

def know_b5():
    return

def know_b6():
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
    return

def know_ls2():
    return

def know_ls3():
    return

def know_ls4():
    return

def know_ls5():
    return

def know_ls6():
    return

def know_ls7():
    return

def know_ls8():
    return

def know_ls9():
    return

def know_ls10():
    return

def know_ls11():
    return

def know_ls12():
    return

#ARC SEGMENTS

def know_as1():
    return

def know_as2():
    return

def know_as3():
    return

def know_as4():
    return

def know_as5():
    return

def know_as6():
    return

#def know_as7():
#    circle circumference
#    return

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
    return
