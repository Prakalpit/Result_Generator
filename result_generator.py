from tkinter import *

root=Tk()
root.title("DEBHIS School Result Generator")
root.geometry("590x500")


#functions here

#clear all function


def All_clear():
    eng_entry.delete(0, END)
    nep_entry.delete(0, END)
    sci_entry.delete(0, END)
    soc_entry.delete(0, END)
    math_entry.delete(0, END)
    hp_entry.delete(0, END)
    opt_1_entry.delete(0, END)
    opt_2_entry.delete(0, END)
    output2.delete(0, END)
    output1.delete(0, END)
    total_entry.delete(0, END)
    Eng_entry.delete(0, END)
    Nep_entry.delete(0, END)
    Sci_entry.delete(0, END)
    Soc_entry.delete(0, END)
    eph_entry.delete(0, END)
    Opt_1_entry.delete(0, END)
    Opt_2_entry.delete(0, END)
    Math_entry.delete(0, END)


#result gererator button


def result():
    eng_sc = float(eng_entry.get())
    nep_sc = float(nep_entry.get())
    sci_sc = float(sci_entry.get())
    soc_sc = float(soc_entry.get())
    mat_sc = float(math_entry.get())
    hp_sc = float(hp_entry.get())
    opt_1_sc = float(opt_1_entry.get())
    opt_2_sc = float(opt_2_entry.get())
    total = float(total_entry.get())

    eng_dp = eng_sc / total
    nep_dp = nep_sc / total
    sci_dp = sci_sc / total
    soc_dp = soc_sc / total
    mat_dp = mat_sc / total
    hp_dp = hp_sc / total
    opt_1_dp = opt_1_sc / total
    opt_2_dp = opt_2_sc / total

    # case of english

    if (eng_dp >= 0.9):  # it will be lie it is 90% which is A+
        eng_pg = '4.0'
        eng_lg = 'A+'

    elif (eng_dp < 0.9) and (eng_dp >= 0.8):   # its like from 80-89  % and it goes on as such
        eng_pg = '3.6'
        eng_lg = 'A'

    elif (eng_dp < 0.8) and (eng_dp >= 0.7):
        eng_pg = '3.2'  # it is point grade
        eng_lg = 'B+'  # it is letter grade

    elif (eng_dp < 0.7) and (eng_dp >= 0.6):
        eng_pg = '2.8'
        eng_lg = 'B'

    elif (eng_dp < 0.6) and (eng_dp >= 0.5):
        eng_pg = '2.4'
        eng_lg = 'C+'

    elif (eng_dp < 0.5) and (eng_dp >= 0.4):
        eng_pg = '2.0'
        eng_lg = 'C'

    elif (eng_dp < 0.4) and (eng_dp >= 0.3):
        eng_pg = '1.6'
        eng_lg = 'D+'

    elif(eng_dp < 0.3) and (eng_dp >= 0.2):
        eng_pg = '1.2'
        eng_lg = 'D'

    else:
        eng_pg = '0.8'
        eng_lg = 'E'


    # case of nepali

    if nep_dp >= 0.9:
        nep_pg = '4.0'
        nep_lg = 'A+'

    elif (nep_dp < 0.9) and (nep_dp >= 0.8):
        nep_pg = '3.6'
        nep_lg = 'A'

    elif (nep_dp < 0.8) and (nep_dp >= 0.7):
        nep_pg = '3.2'
        nep_lg = 'B+'

    elif (nep_dp < 0.7) and (nep_dp >= 0.6):
        nep_pg = '2.8'
        nep_lg = 'B'

    elif (nep_dp < 0.6) and (nep_dp >= 0.5):
        nep_pg = '2.4'
        nep_lg = 'C+'

    elif (nep_dp < 0.5) and (nep_dp >= 0.4):
        nep_pg = '2.0'
        nep_lg = 'C'
    elif (nep_dp < 0.4) and (nep_dp >= 0.3):
        nep_pg = '1.6'
        nep_lg = 'D+'


    elif (nep_dp < 0.3) and (nep_dp >= 0.2):
        nep_pg = '1.2'
        nep_lg = 'D'

    else:
        nep_pg = '0.8'
        nep_lg = 'E'


    # social now
    if soc_dp >= 0.9:
        soc_pg = '4.0'
        soc_lg = 'A+'

    elif (soc_dp < 0.9) and (soc_dp >= 0.8):
        soc_pg = '3.6'
        soc_lg = 'A'

    elif (soc_dp < 0.8) and (soc_dp >= 0.7):
        soc_pg = '3.2'
        soc_lg = 'B+'

    elif (soc_dp < 0.7) and (soc_dp >= 0.6):
        soc_pg = '2.8'
        soc_lg = 'B'

    elif (soc_dp < 0.6) and (soc_dp >= 0.5):
        soc_pg = '2.4'
        soc_lg = 'C+'

    elif (soc_dp < 0.5) and (soc_dp >= 0.4):
        soc_pg = '2.0'
        soc_lg = 'C'
    elif (soc_dp < 0.4) and (soc_dp >= 0.3):
        soc_pg = '1.6'
        soc_lg = 'D'

    elif (soc_dp < 0.3) and (soc_dp >= 0.2):
        soc_pg = '1.2'
        soc_lg = 'D'

    else:
        soc_pg = '0.8'
        soc_lg = 'E'


    # science now
    if sci_dp >= 0.9:
        sci_pg = '4.0'
        sci_lg = 'A+'

    elif (sci_dp < 0.9) and (sci_dp >= 0.8):
        sci_pg = '3.6'
        sci_lg = 'A'

    elif (sci_dp < 0.8) and (sci_dp >= 0.7):
        sci_pg = '3.2'
        sci_lg = 'B+'

    elif (sci_dp < 0.7) and (sci_dp >= 0.6):
        sci_pg = '2.8'
        sci_lg = 'B'

    elif (sci_dp < 0.6) and (sci_dp >= 0.5):
        sci_pg = '2.4'
        sci_lg = 'C+'

    elif (sci_dp < 0.5) and (sci_dp >= 0.4):
        sci_pg = '2.0'
        sci_lg = 'C'
    elif (sci_dp < 0.4) and (sci_dp >= 0.3):
        sci_pg = '1.6'
        sci_lg = 'D'

    elif (sci_dp < 0.3) and (sci_dp >= 0.2):
        sci_pg = '1.2'
        sci_lg = 'D'

    else:
        sci_pg = '0.8'
        sci_lg = 'E'


    # mathematics now

    if mat_dp >= 0.9:
        mat_pg = '4.0'
        mat_lg = 'A+'

    elif (mat_dp < 0.9) and (mat_dp >= 0.8):
        mat_pg = '3.6'
        mat_lg = 'A'

    elif (mat_dp < 0.8) and (mat_dp >= 0.7):
        mat_pg = '3.2'
        mat_lg = 'B+'

    elif (mat_dp < 0.7) and (mat_dp >= 0.6):
        mat_pg = '2.8'
        mat_lg = 'B'

    elif (mat_dp < 0.6) and (mat_dp >= 0.5):
        mat_pg = '2.4'
        mat_lg = 'C+'

    elif (mat_dp < 0.5) and (mat_dp >= 0.4):
        mat_pg = '2.0'
        mat_lg = 'C'
    elif (mat_dp < 0.4) and (mat_dp >= 0.3):
        mat_pg = '1.6'
        mat_lg = 'D'

    elif (mat_dp < 0.3) and (mat_dp >= 0.2):
        mat_pg = '1.2'
        mat_lg = 'D'

    else:
        mat_pg = '0.8'
        mat_lg = 'E'


    #Ehp case
    if (hp_dp >= 0.9):  # it will be lie it is 90% which is A+
        hp_pg = '4.0'
        hp_lg = 'A+'

    elif (hp_dp < 0.9) and (hp_dp >= 0.8):  # its like from 80-89  % and it goes on as such
        hp_pg = '3.6'
        hp_lg = 'A'

    elif (hp_dp < 0.8) and (hp_dp >= 0.7):
        hp_pg = '3.2'  # it is point grade
        hp_lg = 'B+'  # it is letter grade

    elif (hp_dp < 0.7) and (hp_dp >= 0.6):
        hp_pg = '2.8'
        hp_lg = 'B'

    elif (hp_dp < 0.6) and (hp_dp >= 0.5):
        hp_pg = '2.4'
        hp_lg = 'C+'

    elif (hp_dp < 0.5) and (hp_dp >= 0.4):
        hp_pg = '2.0'
        hp_lg = 'C'
    elif (hp_dp < 0.4) and (hp_dp >= 0.3):
        hp_pg = '1.6'
        hp_lg = 'D'

    elif (hp_dp < 0.3) and (hp_dp >= 0.2):
        hp_pg = '1.2'
        hp_lg = 'D'

    else:
        hp_pg = '0.8'
        hp_lg = 'E'

    # OPT II case
    if (opt_2_dp >= 0.9):  # it will be lie it is 90% which is A+
        opt_2_pg = '4.0'
        opt_2_lg = 'A+'

    elif (opt_2_dp < 0.9) and (opt_2_dp >= 0.8):  # its like from 80-89  % and it goes on as such
        opt_2_pg = '3.6'
        opt_2_lg = 'A'

    elif (opt_2_dp < 0.8) and (opt_2_dp >= 0.7):
        opt_2_pg = '3.2'  # it is point grade
        opt_2_lg = 'B+'  # it is letter grade

    elif (opt_2_dp < 0.7) and (opt_2_dp >= 0.6):
        opt_2_pg = '2.8'
        opt_2_lg = 'B'

    elif (opt_2_dp < 0.6) and (opt_2_dp >= 0.5):
        opt_2_pg = '2.4'
        opt_2_lg = 'C+'

    elif (opt_2_dp < 0.5) and (opt_2_dp >= 0.4):
        opt_2_pg = '2.0'
        opt_2_lg = 'C'
    elif (opt_2_dp < 0.4) and (opt_2_dp >= 0.3):
        opt_2_pg = '1.6'
        opt_2_lg = 'D'

    elif (opt_1_dp < 0.3) and (opt_1_dp >= 0.2):
        opt_2_pg = '1.2'
        opt_1_lg = 'D'

    else:
        opt_1_pg = '0.8'
        opt_1_lg = 'E'

    #OPT II case
    if (opt_1_dp >= 0.9):  # it will be lie it is 90% which is A+
        opt_1_pg = '4.0'
        opt_lg = 'A+'

    elif (opt_1_dp < 0.9) and (opt_1_dp >= 0.8):  # its like from 80-89  % and it goes on as such
        opt_1_pg = '3.6'
        opt_lg = 'A'

    elif (opt_1_dp < 0.8) and (opt_1_dp >= 0.7):
        opt_1_pg = '3.2'  # it is point grade
        opt_lg  = 'B+'  # it is letter grade

    elif (opt_1_dp < 0.7) and (opt_1_dp >= 0.6):
        opt_1_pg = '2.8'
        opt_lg  = 'B'

    elif (opt_1_dp < 0.6) and (opt_1_dp >= 0.5):
        opt_1_pg = '2.4'
        opt_lg  = 'C+'

    elif (opt_1_dp < 0.5) and (opt_1_dp >= 0.4):
        opt_1_pg = '2.0'
        opt_lg  = 'C'
    elif (opt_1_dp < 0.4) and (opt_1_dp >= 0.3):
        opt_1_pg = '1.6'
        opt_lg  = 'D'

    elif (opt_1_dp < 0.3) and (opt_1_dp >= 0.2):
        opt_1_pg = '1.2'
        opt_lg = 'D'

    else:
        opt_1_pg = '0.8'
        opt_lg = 'E'

    grade_point_raw = (float(opt_1_pg) + float(opt_2_pg) + float(hp_pg) + float(mat_pg) + float(sci_pg) + float(soc_pg) + float(eng_pg) + float(nep_pg)) / 6
    grade_pointRaw = round(float(grade_point_raw), 2)
    global grade_point
    grade_point = grade_pointRaw
    output1.insert(0, grade_point)
    global ELG, NLG, MLG, SLG, SoLG, HLG, O1LG, O2LG
    ELG= eng_lg
    NLG= nep_lg
    MLG= mat_lg
    SLG= sci_lg
    SoLG= soc_lg
    HLG= hp_lg
    O1LG= opt_lg
    O2LG=opt_2_lg
    #inserting
    Eng_entry.insert(0, ELG)

    Nep_entry.insert(0, NLG)


    Math_entry.insert(0, MLG)


    Sci_entry.insert(0, SLG)


    Soc_entry.insert(0, SoLG)


    eph_entry.insert(0, HLG)


    Opt_1_entry.insert(0, O1LG)

    Opt_2_entry.insert(0, O2LG)


    if (grade_point<=4.0) and (grade_point >3.6):
        output2.insert(0, "A+")

    elif (grade_point<=3.6) and (grade_point >3.2):
        output2.insert(0, "A")

    elif (grade_point<=3.2) and (grade_point >2.8):
        output2.insert(0, "B+")

    elif (grade_point<=2.8) and (grade_point >2.4):
        output2.insert(0, "B")

    elif (grade_point<=2.4) and (grade_point >2.0):
        output2.insert(0, "C+")

    elif (grade_point<=2.0) and (grade_point >1.6):
        output2.insert(0, "C")

    elif (grade_point<=1.6) and (grade_point >1.2):
        output2.insert(0, "D+")

    elif (grade_point<=1.2) and (grade_point >0.8):
        output2.insert(0, "D+")

    else:
        output2.insert(0, "E")


#Name Entry mode

name=Label(root, text="Enter the Individual: ")
name.grid(row=0, column=0)

score = Label(root, text="Score")
score.grid(row=0, column=1)

Letter_Grade = Label(root, text="Generated Letter Grade")
Letter_Grade.grid(row=0, column=2)
#subject entries

#English
eng=Label(root, text="English:")
eng.grid(row=1, column=0)

eng_entry=Entry(root)
eng_entry.grid(row=1, column=1)



#nepali
nep=Label(root, text="Nepali:")
nep.grid(row=2, column=0)

nep_entry=Entry(root)
nep_entry.grid(row=2, column=1)

Nep_entry=Entry(root)
Nep_entry.grid(row=2, column=2)

#mathematics
math=Label(root, text="Mathematics:")
math.grid(row=3, column=0)

math_entry=Entry(root)
math_entry.grid(row=3, column=1)



#Science
sci=Label(root, text="science:")
sci.grid(row=4, column=0)

sci_entry=Entry(root)
sci_entry.grid(row=4, column=1)


#Social
soc=Label(root, text="Social:")
soc.grid(row=5, column=0)

soc_entry=Entry(root)
soc_entry.grid(row=5, column=1)


#hp
hp=Label(root, text="HP:")
hp.grid(row=6, column=0)

hp_entry=Entry(root)
hp_entry.grid(row=6, column=1)



#OPT1
opt_1=Label(root, text="OPT I:")
opt_1.grid(row=7, column=0)

opt_1_entry=Entry(root)
opt_1_entry.grid(row=7, column=1)


#OPT2
opt_2=Label(root, text="OPT II:")
opt_2.grid(row=8, column=0)

opt_2_entry=Entry(root)
opt_2_entry.grid(row=8, column=1)

#total

total=Label(root, text="Total:")
total.grid(row=9, column=0)

total_entry=Entry(root)
total_entry.grid(row=9, column=1)
#generate Result Button
result=Button(root, text="Generate Result", command=result)
result.grid(row=10, column=1)

#text to say the result is done
done=Label(root, text="Get the result here")
done.grid(row=11, column=0)
#GPA output
gpa=Label(root, text="GPA")
gpa.grid(row=12, column=0)

output1=Entry(root)
output1.grid(row=12, column=1)

grade=Label(root, text="Grade")
grade.grid(row=13, column=0)

output2=Entry(root)
output2.grid(row=13, column=1)

#clear all button
clear_all=Button(root, text="DO NEXT", command=All_clear)
clear_all.grid(row=14, column=1)

def exit():
    quit()

Exit=Button(root, text="EXIT", command=exit)
Exit.grid(row=15, column=1)

#returns
Eng_entry=Entry(root)
Eng_entry.grid(row=1, column=2)

Nep_entry=Entry(root)
Nep_entry.grid(row=2, column=2)

Math_entry=Entry(root)
Math_entry.grid(row=3, column=2)

Sci_entry=Entry(root)
Sci_entry.grid(row=4, column=2)

Soc_entry=Entry(root)
Soc_entry.grid(row=5, column=2)

eph_entry=Entry(root)
eph_entry.grid(row=6, column=2)

Opt_1_entry=Entry(root)
Opt_1_entry.grid(row=7, column=2)

Opt_2_entry=Entry(root)
Opt_2_entry.grid(row=8, column=2)

#focus
eng_entry.focus()
#programme Ends here
root.mainloop()
