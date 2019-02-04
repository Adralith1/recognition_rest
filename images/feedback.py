import sqlite3

def changeDataFromFeedback(feedback,request_id):



    try:
        conn = sqlite3.connect("db.sqlite3")  # connexion bd
        cursor = conn.cursor()
        get_list = "SELECT * FROM url_responses WHERE request_id=?"  # on cherche toutes les urls lies a la requete du client
        cursor.execute(get_list, (request_id,))
        list = cursor.fetchall()

        for i in range(0,len(list)):
            if feedback[i]['feedback']==0 :#Pas la peine de mettre a zero des valeurs deja a zero, economie de requetes
                change_feedback="UPDATE url_responses SET feedback=? WHERE request_id=? and image_url=?" #on met a 1 ou 0 des que le feedback est donne (sinon la valeur est 0 par defaut)
                cursor.execute(change_feedback,(feedback[i]['feedback'],request_id,list[i][2],))
        conn.commit()
        change_score = "UPDATE url_responses SET score=score/2 WHERE feedback=1 and request_id=?" #on divise par 2 le score sur le "mauvais feedback"
        cursor.execute(change_score, (request_id,))
        conn.commit()
        return 0 #tout s'est bien passe
    except:
        return 1 #une erreur est survenue


