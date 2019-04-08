import sqlite3


def jsonize(request_id):
    conn = sqlite3.connect("db.sqlite3")  # connexion bd
    cursor = conn.cursor()
    get_date = "SELECT request_date FROM images_request WHERE id=?"  # on cherche la date de la requete
    cursor.execute(get_date, (request_id,))
    user_request = cursor.fetchone()
    date = user_request[0]

    get_client = "SELECT client FROM images_request WHERE id=?"  # on cherche le client de la requete
    cursor.execute(get_client, (request_id,))
    client_request = cursor.fetchone()
    client = client_request[0]

    get_urls = "SELECT * FROM url_responses WHERE request_id=?"  # on cherche les urls resultantes de la requete
    cursor.execute(get_urls, (request_id,))
    user_corresponding_result = cursor.fetchall()
    data = {}  # on initialise l'objet json qu'on va renvoyer pour le GET
    data['date'] = date  # attribut date
    data['client'] = client  # attribut client
    data['request_id'] = request_id

    urls_list = []  # liste d'urls et score
    for i in range(0, len(user_corresponding_result)):
        url_element = {}  # un url_element est une url + un score dans un dictionnaire
        url_element['image_url'] = user_corresponding_result[i][2]
        url_element['score'] = user_corresponding_result[i][3]
        urls_list.append(url_element)

    data['results'] = urls_list  # on stocke la liste

    return data  # resultat
