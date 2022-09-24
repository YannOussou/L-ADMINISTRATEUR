from cProfile import label
from cgitb import text
from html.entities import name2codepoint
from pickle import APPEND
from tkinter import *
from tkinter import font
from tkinter import messagebox
#Pour la page d'enregstrement des etudiants

def ENREGISTREMENT():
    enregistrement= Tk()
    enregistrement.title("@Enregistrements@")
    enregistrement.configure(background="#ffffff")
    enregistrement.geometry("400x500")
    enregistrement.minsize(400,500)
    enregistrement.maxsize(400,500)
    
    name=Label(enregistrement,text="Nom :", font="Raleway",fg="black",bg="#ffffff")
    name.place (x=20,y=100)
    name2nd=Label(enregistrement,text="Prénom :", font="Raleway",fg="black",bg="#ffffff")
    name2nd.place(x=20,y=130)
    classe =Label(enregistrement, text="Classe :",font="Raleway",fg="black",bg="#ffffff")
    classe.place(x=20,y=160)
    date=Label(enregistrement, text="Date:",font="Raleway", fg= "black",bg="#ffffff")
    date.place(x=20,y=190)
    
    entré1=Entry(enregistrement,)
    entré1.place(x=102,y=105)
    entré2=Entry(enregistrement,)
    entré2.place(x=102,y=135)
    entréC= Entry(enregistrement, )
    entréC.place(x=102,y=165)
    entryI= Entry(enregistrement,)
    entryI.place(x=102,y=195)
    #debut de la def INSCRIPTION: programme d'enregistrement dans la base de donnée
    def INSCRIPTION():
        nom=entré1.get()
        prenom=entré2.get()
        classe=entréC.get()
        date=entryI.get()
        if nom=="" or prenom=="" or classe=="" or date=="":
            enregistrement.destroy()
            messagebox.showwarning("ATTENTION/!\ ","Veuillez recommencer l'enregistrementent en remplissant tous les champs d'entrés")
            
        else:
             
             separation=["---------------------------------------------- \n"]
             l=["NOM ; PRENOM ; CLASSE ;DATE  \n"]
             liste=[nom +"; ", prenom+"; ",classe+"; ",date+"\n"]
             with open("INSCRIPTION.txt","a")as yann:
                for tiret in separation:
                    yann.write(tiret)
                for presentation in l:
                    yann.write(presentation)
                for eleve in liste :
                    yann.write(eleve)
                messagebox.showinfo("Enregistrement","Inscription effectuée avec succès")      

        return       
    #fin de la def INSCRIPTION: programme d'enregistrement dans la base de donnée


    def clear():#def pour supprimé les entry
        entré1.delete(0,END)
        entré2.delete(0,END)
        entréC.delete(0,END)
        entryI.delete(0,END)
        return
    #Bouton pour effacer les entrées
    cls=Button(enregistrement, text="EFFACER", fg ="white", bg="red",font="Raleway",command= clear)
    cls.place(x=127,y=290)

    #Bouton d'enregistrement(inscription)
    a=Button(enregistrement,text="INSCRIPTION",fg="white",bg="green",font="Raleway",command=INSCRIPTION)
    a.place(x=107,y=240)
            
    enregistrement.mainloop()
    return
#fin de la def ENREGISTREMENT

#Pour la page des saisi des notes 
def NOTES():
    #debut du programme pour la saisie des notes
    def SAISI():
        nom=entré1.get()
        prenom=entré2.get()
        classe=entréC.get()
        math=maths.get()
        fran=fr.get()
        ang=anglais.get()
        phy=pc.get()
        if math==""or phy==""or ang==""or fran=="":
            notes.destroy()
            messagebox.showerror("ATTENTION","Erreur, cases vides")
            messagebox.showinfo("ATTENTION","Recommencez en remplissant les cases vides")
        #conversion notes str en str
        M=float(math)
        F=float(fran)
        A=float(ang)
        PC=float(phy)
        
        my=(M+F+A+PC)/4
        print(my)
        #Conversion de la moyenne my Float en str
        my=str(my)
        my=my[0:5]
        
        if nom=="" or prenom=="" or classe==""or math=="" or phy=="" or fran=="" or ang=="":
            messagebox.showwarning("ATTENTION","Veuillez reprendre en remplissant tous les champs d'entrés")
        else :
             sepa=["-------------------------------------------------------------- \n"]
             exam=["NOM ; PRENOM ; CLASSE   MATH ; PHY-CHI ; FRAN ; ANG \n"]
             moy =[nom+" ; "+prenom+" ; "+classe+" ; "+math+" ; "+phy+" ; "+fran+" ; "+ang+"\n"]
             my=["MOYENNES:"+my+"\n"]
             with open ("MOYENNES.txt","a") as Moyenne:
                 
                 for tirêt in sepa :
                     Moyenne.write(tirêt)
                 for points in exam :
                     Moyenne.write(points)

                 for m in moy :
                     Moyenne.write (m)

                 for a in my :
                     Moyenne.write(a)
                 messagebox.showinfo("Saisi", "La saisi a été effectuée avec succès")    
        return
     #findu programme pour la saisie des notes
    
    #fonction qui efface
    def cls():
        entré1.delete(0,END)
        entré2.delete(0,END)
        entréC.delete(0,END)
        maths.delete(0,END)
        fr.delete(0,END)
        anglais.delete(0,END)
        pc.delete(0,END)
        return
    
    notes= Tk()
    notes.title("@Saisie des notes@")
    notes.configure(background="#ffffff")
    notes.geometry("400x500")
    notes.minsize(400,500)
    notes.minsize(400,500)
    
    saisir=Label(notes, text="VEUILLEZ SAISIR LES MOYENNES",font=("Bahnschrift",16),bg="#ffffff",fg="Green")
    saisir.place(x=20,y=20)
    
    maths=Label(notes, text="Maths ", font="Bahnschrift",fg="Black",bg="#ffffff")
    maths.place(x=260,y=80)
    fr=Label(notes, text="Français", font="Bahnschrift",fg="Black",bg="#ffffff")
    fr.place(x=260,y=105)
    anglais=Label(notes, text="Anglais", font="Bahnschrift",fg="Black",bg="#ffffff")
    anglais.place(x=260,y=130)
    pc=Label(notes, text="Physique", font="Bahnschrift",fg="Black",bg="#ffffff")
    pc.place(x=260,y=155)
    name=Label(notes,text="Nom :", font="Raleway",fg="black",bg="#ffffff")
    name.place (x=20,y=92.5)
    name2nd=Label(notes,text="Prénom :", font="Raleway",fg="black",bg="#ffffff")
    name2nd.place(x=20,y=117.5)
    classe =Label(notes, text="Classe :",font="Raleway",fg="black",bg="#ffffff")
    classe.place(x=20,y=142.5)
    
    maths=Entry(notes, font="Bahnschrift",fg="red",bg="#ffffff")
    maths.place(x=349,y=80 ,width=45)
    fr=Entry(notes, font="Bahnschrift",fg="red",bg="#ffffff")
    fr.place(x=349,y=105,width=45)
    anglais=Entry(notes, font="Bahnschrift",fg="red",bg="#ffffff")
    anglais.place(x=349,y=130,width=45)
    pc=Entry(notes, font="Bahnschrift ",bg="#ffffff",fg="red")
    pc.place(x=349,y=155,width=45)
    entré1=Entry(notes,font="Bahnschrift ",bg="#ffffff")
    entré1.place(x=102,y=97.5,width=150)
    entré2=Entry(notes,font="Bahnschrift ",bg="#ffffff")
    entré2.place(x=102,y=122.5,width=150)
    entréC= Entry(notes,font="Bahnschrift ",bg="#ffffff" )
    entréC.place(x=102,y=147.5,width=150)

    #Bouton pour calculer pour calculer la moyenne
    a=Button(notes,text="CALCULER",font ="Bahnschrift",fg="white",bg="green",command=SAISI)
    a.place(x=115,y=220)
    #Bouton pour effacer les entré
    cls=Button(notes,text="EFFACER",font="Bahnschrift", fg="white",bg="red",command=cls)
    cls.place(x=115,y=270)
    
    notes.mainloop()
    return
#fin de la def NOTES


#Pour la page de calcul des moyennes
def MOYENNES():
    fin=StringVar()
    #debut du programme pour les MoyG
    def MoyG():
        with open ("MOYENNES.txt",'rt') as Moyenne:
             texte=Moyenne.read()
             #Création de mon canvas pour l'affichge des moyennes
             MonCanvas= Canvas(moyenne,bg="white")
             MonCanvas.place(x=80,y=50,width=450,height=150)
             #ascenceur est la variable qui va scroller MonCanvas,Il ne faut pas oublier de configurer la scrollar
             ascenceur=Scrollbar(MonCanvas)
             ascenceur.pack(side=RIGHT,fill=Y)
             ascenceur.config(command=MonCanvas.yview) #configuration de la scrollbar

             #resultat est la variable qui va mettre les infos dans MonCanvas 
             resultats=MonCanvas.create_text(225,100,text=texte)
             
        return
             
    #fin du programme pour les MoyG
    moyenne= Tk()
    moyenne.title("@Moyennes Generales@")
    moyenne.configure(background="#a9a9a9")
    moyenne.geometry("600x400")
    moyenne.minsize(600,400)
    
    btn=Button(moyenne, text="VOIR LES MOYENNES",font="Bahnschrift",fg="white",bg="blue",command=MoyG)
    btn.place(x=165,y=300)
    
    moyenne.mainloop()

    return

app= Tk()
app.title("@ L'administration Scolaire @")
app.configure(background="#FFFFFF")
app.minsize(350,300)
app.maxsize(350,300)
#bouton de la page principale(generateur de nouvelle page )
ENREGISTREMENT=Button(app,font=("Raleway",10), text="ENREGISTREMENTS",fg="blue" ,command=ENREGISTREMENT)
ENREGISTREMENT.place(x=80 ,y=90)
menu=Label(app,text="@MENU ADMININSTRATEUR@",fg="blue",bg="#FFFFFF", font=("Raleway",16))
menu.place(x=25,y=20)
NOTES=Button(app,font=("Raleway",10) , text="NOTES" , fg="blue", command= NOTES)
NOTES.place(x=80 ,y=150)
MOYENNE=Button(app,font=("Raleway",10) , text="MOYENNES", fg="blue", command= MOYENNES)
MOYENNE.place(x=80 ,y=200)
        
app.mainloop()



    

