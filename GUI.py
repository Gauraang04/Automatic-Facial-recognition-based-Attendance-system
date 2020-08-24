from tkinter import *
from Training import *
import cv2
import os
from imutils.video import VideoStream
import face_recognition
import imutils
import pickle
import time
import xlwt
import numpy as np
import pandas as pd
import openpyxl 
import datetime

root= Tk()
root.geometry("758x511")
root.iconbitmap('icon.ico')
root.title("Attendance System")
root.configure(background="grey22")


def second_win():
    l=[]
    def take_img():          
        cam = cv2.VideoCapture(0)
        detector = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
        Roll_no = txt2.get()
        Name = txt.get()
        co=['Name']
        att=pd.DataFrame(columns=co)
        N=Name+'('+Roll_no+')'
        l.append(N)
        att.loc[len(att)]=l
        print(att)
        if not os.path.exists('Record'):
            os.mkdir('Record')
        path1='Record/Student_record.xlsx'
        m= 'a' if os.path.exists(path1) else 'w'
        with pd.ExcelWriter(path1,mode= m) as w:
            att.to_excel(w)
        i=0
        if not os.path.exists('dataset'):
            os.mkdir('dataset')
        path='dataset/'+Name+'('+Roll_no+')'+'/'
        if not os.path.exists(path):
            os.mkdir(path)
        while True:
            ret, img = cam.read()
            gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
            faces = detector.detectMultiScale(gray, 1.3, 5)
            for (x, y, w, h) in faces:
                cv2.rectangle(img, (x, y), (x + w, y + h), (255, 0, 0), 2)
                # incrementing sample Roll_nober
                i=i+1
                # saving the captured face in the dataset folder
                cv2.imwrite(path+Roll_no+'-'+'{}.jpg'.format(i),gray[y:y + h, x:x + w])
                cv2.imshow('Frame', img)
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break
            elif i>100:
                break
        cam.release()
        cv2.destroyAllWindows()
    window= Tk()
    window.iconbitmap('icon.ico')
    window.title("Update Database")
    window.geometry('758x511')

    label_00= Label(window, text="Enter Student Details", font=("ubantu", 40), fg="black", bg="grey30",
      height=2, width=23).grid(row=0, rowspan=2, columnspan=2, sticky=N+E+W+S, padx=20, pady=15)

    lbl = Label(window, text="Enter Name :", width=10, height=2 , fg="grey30", font=('ubuntu', 18) )# .grid(row= 3, sticky=E)
    lbl.place(x=202, y=157)

    txt = Entry(window, validate="key", width=20, bg="grey30", fg="grey90", font=('ubuntu', 15, ' bold '))#.grid(row=3, column=1, sticky= W)
    #txt['validatecommand'] = (txt.register(testVal),'%P','%d')
    txt.place(x=352, y=174)

    #txt = Entry(window,width=20  ,bg="grey30" ,fg="grey90",font=('ubuntu', 15, ' bold ')).grid(row=3, column=1, sticky= W)
    #txt.place(x=700, y=215)

    lbl2 = Label(window, text="Enter Roll.No :",width=11  ,fg="grey30" ,height=2 ,font=('ubuntu', 18)) #.grid(row= 5, sticky=E, padx=5) 
    lbl2.place(x=185, y=227)

    txt2 = Entry(window, width=20,validate="key" ,bg="grey30"  ,fg="grey90",font=('ubuntu', 15, ' bold ')) #.grid(row=5, column=1, sticky= W)
    txt2.place(x=352, y=244)

    Notification = Label(window, text="All things good", bg="Green", fg="white", width=15,
                      height=2, font=('times', 17, 'bold'))

    but_01= Button(window, text="Train Images", font=("ubantu", 18), bg="grey30",
       fg='grey90', command= train)#.grid(row=7, column=1, sticky=S, pady=15)
    but_01.place(x=395, y=312)

    but_02= Button(window, text="Take Images", font=("ubantu", 18), bg="grey30",
       fg='grey90', command= take_img)#.grid(row=7,column=1, columnspan=2, sticky=W, pady=15)
    but_02.place(x=220, y=312)
    
    but_BK= Button(window, text="⬅ BACK", font=("ubantu", 18), bg="grey30",
       fg='grey90',height=1, width=3, command= window.destroy).grid(row=9, columnspan=2, sticky=N+E+W+S, padx=305, pady=230)

########## Name = txt.get()
########## Roll_no = txt2.get()


def third_win():
    def fun():
        data = pickle.loads(open("encodings.pickle", "rb").read())
        l=[]
        sub=txt3.get()
        while True:
                data = pickle.loads(open("encodings.pickle", "rb").read())
                vs = cv2.VideoCapture(0) #cv2.VideoCapture('http://192.168.43.88:8080/shot.jpg')#VideoStream(src=0).start()
                ret,frame = vs.read()
                rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)         
                #rgb = imutils.resize(frame, width=750)      
                r = frame.shape[1] / float(rgb.shape[1])

                boxes = face_recognition.face_locations(rgb,
                        model='hog')
                encodings = face_recognition.face_encodings(rgb, boxes)
                names = []
                for encoding in encodings:
                        matches = face_recognition.api.compare_faces(data["encodings"],
                                                         encoding, tolerance=0.479)
                        name = "Unknown"
                        if True in matches:
                                matchedIdxs = [i for (i, b) in enumerate(matches) if b]
                                counts = {}
                                for i in matchedIdxs:
                                        name = data["names"][i]
                                        counts[name] = counts.get(name, 0) + 1
                                name = max(counts, key=counts.get)
                        names.append(name)
                for ((top, right, bottom, left), name) in zip(boxes, names):
                        top = int(top * r)
                        right = int(right * r)
                        bottom = int(bottom * r)
                        left = int(left * r)
                        cv2.rectangle(frame, (left, top), (right, bottom),
                                (0, 255, 0), 2)
                        y = top - 15 if top - 15 > 15 else top + 15
                        cv2.putText(frame, name, (left, y), cv2.FONT_HERSHEY_SIMPLEX,
                                0.75, (0, 255, 0), 2)
                        l.append(name)
                cv2.imshow("Frame", frame)
                key = cv2.waitKey(1)
                if key == ord("q"):
                    cv2.destroyAllWindows()
                    break
        lis = list(dict.fromkeys(l))
        try:
            lis.remove('Unknown')
            print(lis)
        except ValueError:
            print(lis)
        co=['Name']
        att=pd.DataFrame(columns=co)
        print(len(lis))
        for i in range (0,len(lis)):
            att.loc[len(att)]=lis[i]
        #att.drop_duplicates(['name'],keep='first')
        print(att)
        ts = time.time() 
        date = datetime.datetime.fromtimestamp(ts).strftime('%d-%m-%y')
        sheet=date
        path = 'Attendence/'+sub+'.xlsx'
        if not os.path.exists('Attendence'):
            os.mkdir('Attendence')
       # path='dataset/'+Name+'('+Roll_no+')'+'/'
        m= 'a' if os.path.exists(path) else 'w'
        with pd.ExcelWriter(path,mode= m) as w:
            att.to_excel(w,sheet_name=sheet)
    window= Tk()
    window.iconbitmap('icon.ico')
    window.title("Mark Attendence")
    window.geometry('758x511')

    label_01= Label(window, text="Enter Subject Details", font=("ubantu", 40), fg="black", bg="grey30",
      height=2, width=23).grid(row=0, rowspan=2, columnspan=2, sticky=N+E+W+S, padx=25, pady=15)

    lb3 = Label(window, text="Enter Subject :", width=12, height=2 , fg="grey30", font=('ubuntu', 18) ) #.grid(row= 3, sticky=E)
    lb3.place(x=150, y=165)

    #txt3 = Entry(window,width=20,validate="key"  ,bg="grey30" ,fg="grey90",font=('ubuntu', 15)).grid(row=3, column=1, sticky= W)
    txt3 = Entry(window, validate="key", width=20, bg="grey30", fg="grey90", font=('ubuntu', 15, ' bold '))#.grid(row=3, column=1, sticky= W)
    #txt['validatecommand'] = (txt.register(testVal),'%P','%d')
    txt3.place(x=352, y=182)

    #lb4 = Label(window, text="Enter Subject :", width=12, height=2 , fg="grey30", font=('ubuntu', 18) ) .grid(row= 5, sticky=E)
    #lbl.place(x=130, y=165)

    but_03= Button(window, text="Start Attendence", font=("ubantu", 18), bg="grey30",
       fg='grey90',width=16, command= fun)#.grid(row=7, columnspan=2, sticky=W+E+N+S, padx=275, pady=55)
    but_03.place(x=260,y=250)
    
    but_BK2= Button(window, text="⬅ BACK", font=("ubantu", 18), bg="grey30",
       fg='grey90',height=1, width=10, command= window.destroy)#.grid(row=9, columnspan=2, sticky=N+E+W+S, padx=305, pady=5)
    but_BK2.place(x=300,y=325)



label_01= Label(text="Attendence System", font=("ubantu", 40), fg="grey90", bg="grey30",
      height=2, width=23).grid(row=0, rowspan=2, columnspan=2, sticky=N+E+W+S, padx=20, pady=15)


but_UD= Button(text="UPDATE DATABASE", font=("ubantu", 18), bg="white",
       fg='black',height=1, width=0, command= second_win, relief=FLAT).grid(row=3, columnspan=2, sticky=W+E+N+S, padx=200, pady=15)

but_MA= Button(text="MARK ATTENDANCE", font=("ubantu", 18), bg="white",
       fg='black',height=1, width=3, command= third_win).grid(row=4, columnspan=2, sticky=N+E+W+S, padx=200, pady=15)

but_QT= Button(text="⬅ QUIT", font=("ubantu", 18), bg="white",
       fg='black',height=1, width=3, command= root.destroy).grid(row=5, columnspan=2, sticky=N+E+W+S, padx=275, pady=15)


root.mainloop




