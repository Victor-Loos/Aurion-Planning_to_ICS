from datetime import datetime
import email
import locale
locale.setlocale(locale.LC_ALL, 'fr_FR.utf-8')
import getplanning, validelogs, parse
     

#@app.route('/log', methods=['GET', 'POST'])
def log(email,password):
    # handle the POST request
    #session["email"] = urllib.parse.quote(session["email"])
    return (validelogs.main(0, email, password) != True)
        

#@app.route('/ics', methods=['GET', 'POST'])
def return_cal(email,password,month):
    # Exporte les 6 prochains mois 
    ajd=datetime.now()
    start = datetime.strftime(ajd, '%Y-%m')
    start = start+"-01"

    end = datetime.strptime(str(start),'%Y-%m-%d')
    end = int(end.timestamp())
    end += month*30*24*60*60
    end = datetime.fromtimestamp(end)
    end = datetime.strftime(end, '%Y-%m-%d')

    #Semaine : 2022-03-21T13:30:00+0100
    #Mois : 2022-09-11
    cal=getplanning.main(start,end,email,password)
    # Retour à améliorer ...
    return parse.main(cal)


# Main code
email=str(input("Entrez votre prenom.nom : "))
email=email+"@student.junia.com"
password=str(input("Mots de passe : "))
month=int(input("Combien de mois voulez vous ? : ") or 6)

log(email,password)

return_cal(email,password,month)