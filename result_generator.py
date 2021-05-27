from tkinter import *

root=Tk()
root.title("DEBHIS School Result Generator")
root.geometry("400x400")


#functions here

#clear all function


def All_clear():
    eng_entry.delete(0, END)
    nep_entry.delete(0, END)
    sci_entry.delete(0, END)
    soc_entry.delete(0, END)
    math_entry.delete(0, END)
    hp_entry.delete(0, END)
    moral_entry.delete(0, END)
    output2.delete(0, END)
    output1.delete(0, END)
    total_entry.delete(0, END)

#result gererator button


def result():
    eng_sc = float(eng_entry.get())
    nep_sc = float(nep_entry.get())
    sci_sc = float(sci_entry.get())
    soc_sc = float(soc_entry.get())
    mat_sc = float(math_entry.get())
    hp_sc = float(hp_entry.get())
    moral_sc = float(moral_entry.get())
    total = float(total_entry.get())

    eng_dp = eng_sc / total
    nep_dp = nep_sc / total
    sci_dp = sci_sc / total
    soc_dp = soc_sc / total
    mat_dp = mat_sc / total
    hp_dp = hp_sc / total
    moral_dp = moral_sc / total

    # case of english

    if eng_dp >= 0.9:  # it will be lie it is 90% which is A+
        eng_pg = '4.0'
        eng_lg = 'A+'

    elif eng_dp < 0.9 and (eng_dp >= 0.8):  # its like from 80-89  % and it goes on as such
        eng_pg = '3.6'
        eng_lg = 'A'

    elif eng_dp < 0.8 and (eng_dp >= 0.7):
        eng_pg = '3.2'  # it is point grade
        eng_lg = 'B+'  # it is letter grade

    elif eng_dp < 0.7 and (eng_dp >= 0.6):
        eng_pg = '2.8'
        eng_lg = 'B'

    elif eng_dp < 0.6 and (eng_dp >= 0.5):
        eng_pg = '2.4'
        eng_lg = 'C+'

    elif eng_dp < 0.5 and (eng_dp >= 0.4):
        eng_pg = '2.0'
        eng_lg = 'C'
    elif eng_dp < 0.4 and (eng_dp >= 0.3):
        eng_pg = '1.6'
        eng_lg = 'D'
    else:
        eng_pg = '1.2'
        eng_lg = 'E'

    # case of nepali

    if nep_dp >= 0.9:
        nep_pg = '4.0'
        nep_lg = 'A+'

    elif nep_dp < 0.9 and (nep_dp >= 0.8):
        nep_pg = '3.6'
        nep_lg = 'A'

    elif nep_dp < 0.8 and (nep_dp >= 0.7):
        nep_pg = '3.2'
        nep_lg = 'B+'

    elif nep_dp < 0.7 and (nep_dp >= 0.6):
        nep_pg = '2.8'
        nep_lg = 'B'

    elif nep_dp < 0.6 and (nep_dp >= 0.5):
        nep_pg = '2.4'
        nep_lg = 'C+'

    elif nep_dp < 0.5 and (nep_dp >= 0.4):
        nep_pg = '2.0'
        nep_lg = 'C'
    elif nep_dp < 0.4 and (nep_dp >= 0.3):
        nep_pg = '1.6'
        nep_lg = 'D'
    else:
        nep_pg = '1.2'
        soc_lg = 'E'

    # social now
    if soc_dp >= 0.9:
        soc_pg = '4.0'
        soc_lg = 'A+'

    elif soc_dp < 0.9 and (soc_dp >= 0.8):
        soc_pg = '3.6'
        soc_lg = 'A'

    elif soc_dp < 0.8 and (soc_dp >= 0.7):
        soc_pg = '3.2'
        soc_lg = 'B+'

    elif soc_dp < 0.7 and (soc_dp >= 0.6):
        soc_pg = '2.8'
        soc_lg = 'B'

    elif soc_dp < 0.6 and (soc_dp >= 0.5):
        soc_pg = '2.4'
        soc_lg = 'C+'

    elif soc_dp < 0.5 and (soc_dp >= 0.4):
        soc_pg = '2.0'
        soc_lg = 'C'
    elif soc_dp < 0.4 and (soc_dp >= 0.3):
        soc_pg = '1.6'
        soc_lg = 'D'
    else:
        soc_pg = '1.2'
        soc_lg = 'E'

    # science now
    if sci_dp >= 0.9:
        sci_pg = '4.0'
        sci_lg = 'A+'

    elif sci_dp < 0.9 and (sci_dp >= 0.8):
        sci_pg = '3.6'
        sci_lg = 'A'

    elif sci_dp < 0.8 and (sci_dp >= 0.7):
        sci_pg = '3.2'
        sci_lg = 'B+'

    elif sci_dp < 0.7 and (sci_dp >= 0.6):
        sci_pg = '2.8'
        sci_lg = 'B'

    elif sci_dp < 0.6 and (sci_dp >= 0.5):
        sci_pg = '2.4'
        sci_lg = 'C+'

    elif sci_dp < 0.5 and (sci_dp >= 0.4):
        sci_pg = '2.0'
        sci_lg = 'C'
    elif sci_dp < 0.4 and (sci_dp >= 0.3):
        sci_pg = '1.6'
        sci_lg = 'D'
    else:
        sci_pg = '1.2'
        sci_lg = 'E'

    # mathematics now

    if mat_dp >= 0.9:
        mat_pg = '4.0'
        mat_lg = 'A+'

    elif mat_dp < 0.9 and (mat_dp >= 0.8):
        mat_pg = '3.6'
        mat_lg = 'A'

    elif mat_dp < 0.8 and (mat_dp >= 0.7):
        mat_pg = '3.2'
        mat_lg = 'B+'

    elif mat_dp < 0.7 and (mat_dp >= 0.6):
        mat_pg = '2.8'
        mat_lg = 'B'

    elif mat_dp < 0.6 and (mat_dp >= 0.5):
        mat_pg = '2.4'
        mat_lg = 'C+'

    elif mat_dp < 0.5 and (mat_dp >= 0.4):
        mat_pg = '2.0'
        mat_lg = 'C'
    elif mat_dp < 0.4 and (mat_dp >= 0.3):
        mat_pg = '1.6'
        mat_lg = 'D'
    else:
        mat_pg = '1.2'
        mat_lg = 'E'

    # hp case
    if hp_dp >= 0.9:
        hp_pg = '4.0'
        hp_lg = 'A+'

    elif hp_dp < 0.9 and (mat_dp >= 0.8):
        hp_pg = '3.6'
        hp_lg = 'A'

    elif hp_dp < 0.8 and (mat_dp >= 0.7):
        hp_pg = '3.2'
        hp_lg = 'B+'

    elif hp_dp < 0.7 and (mat_dp >= 0.6):
        hp_pg = '2.8'
        hp_lg = 'B'

    elif hp_dp < 0.6 and (mat_dp >= 0.5):
        hp_pg = '2.4'
        hp_lg = 'C+'

    elif hp_dp < 0.5 and (mat_dp >= 0.4):
        hp_pg = '2.0'
        hp_lg = 'C'

    elif hp_dp < 0.4 and (mat_dp >= 0.3):
        hp_pg = '1.6'
        hp_lg = 'D'
    else:
        hp_pg = '1.2'
        hp_lg = 'E'

    # moral case

    if moral_dp >= 0.9:
        moral_pg = '4.0'
        moral_lg = 'A+'

    elif moral_dp < 0.9 and (mat_dp >= 0.8):
        moral_pg = '3.6'
        moral_lg = 'A'

    elif moral_dp < 0.8 and (mat_dp >= 0.7):
        moral_pg = '3.2'
        moral_lg = 'B+'

    elif moral_dp < 0.7 and (mat_dp >= 0.6):
        moral_pg = '2.8'
        moral_lg = 'B'

    elif moral_dp < 0.6 and (mat_dp >= 0.5):
        moral_pg = '2.4'
        moral_lg = 'C+'

    elif moral_dp < 0.5 and (mat_dp >= 0.4):
        moral_pg = '2.0'
        moral_lg = 'C'

    elif mat_dp < 0.4 and (mat_dp >= 0.3):
        moral_pg = '1.6'
        moral_lg = 'D'
    else:
        moral_pg = '1.2'
        moral_lg = 'E'

    grade_point_raw = (float(mat_pg) + float(eng_pg) + float(soc_pg) + float(sci_pg) + float(nep_pg) + float(hp_pg)+float(moral_pg)) / 7
    grade_pointRaw = round(grade_point_raw, 2)

    global grade_point
    grade_point=grade_pointRaw
    output1.insert(0, grade_point)
    if (grade_point >3.6) and (grade_point<=4.0):
        output2.insert(0, "A+")

    elif (grade_point >3.2) and (grade_point<=3.6):
        output2.insert(0, "A")

    elif (grade_point >2.8) and (grade_point<=3.2):
        output2.insert(0, "B+")

    elif (grade_point > 2.4) and (grade_point<=2.8):
        output2.insert(0, "B")

    elif (grade_point >2.0) and (grade_point<=2.4):
        output2.insert(0, "C+")

    elif (grade_point >1.6) and (grade_point<=2.0):
        output2.insert(0, "D")

    else:
        output2.insert(0, "E")





#Name Entry mode

name=Label(root, text="Enter the Individual: ")
name.grid(row=0, column=0)

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

#Science
sci=Label(root, text="science:")
sci.grid(row=3, column=0)

sci_entry=Entry(root)
sci_entry.grid(row=3, column=1)
#Social
soc=Label(root, text="Social:")
soc.grid(row=4, column=0)

soc_entry=Entry(root)
soc_entry.grid(row=4, column=1)

#mathematics
math=Label(root, text="Mathematics:")
math.grid(row=5, column=0)

math_entry=Entry(root)
math_entry.grid(row=5, column=1)
#hp
hp=Label(root, text="HP:")
hp.grid(row=6, column=0)

hp_entry=Entry(root)
hp_entry.grid(row=6, column=1)


#moral
moral=Label(root, text="Moral:")
moral.grid(row=7, column=0)

moral_entry=Entry(root)
moral_entry.grid(row=7, column=1)

total=Label(root, text="Total:")
total.grid(row=8, column=0)

total_entry=Entry(root)
total_entry.grid(row=8, column=1)
#generate Result Button
result=Button(root, text="Generate Result", command=result)
result.grid(row=9, column=1)

#text to say the result is done
done=Label(root, text="Get the result here")
done.grid(row=10, column=0)
#GPA output
gpa=Label(root, text="GPA")
gpa.grid(row=11, column=0)

output1=Entry(root)
output1.grid(row=11, column=1)

grade=Label(root, text="Grade")
grade.grid(row=12, column=0)
output2=Entry(root)
output2.grid(row=12, column=1)

#clear all button
clear_all=Button(root, text="Clear all", command=All_clear)
clear_all.grid(row=13, column=1)

#programme Ends here
root.mainloop()