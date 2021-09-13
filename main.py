#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Script for test for alternance
"""

# Format json.
import json

# Make request.
import requests

#Verify python version > 3.7 
import sys
print(sys.version)


class API:
    """Class for calling api"""

    def __init__(self, path_url):
        """Constructor of the class"""

        # Path of th url to call.
        self.path_url = path_url 

        # Content of the request.
        self.content = None


    def calling_url(self):
        """Function for make a HTTP request."""

        # Make a request.
        response = requests.get(self.path_url)
        # Recuperate the content under json form decode in utf-8.
        self.content = json.loads(response.content.decode('utf-8'))


    def getter_os(self, data_dict) -> dict:
        """On the dictionnary return, search to find the os on the user agent label"""

        # List of all os avaibles.
        os_possible = ["windows", "linux", "macos", "mac os", "iOS", "android"]
        # Lower the string for the scrap.
        os_user = data_dict["user_agent"].lower()

        # Make a matching. -1 <= we did not find os.
        wrap = [os for os in os_possible if os_user.find(os) >= 0]

        # Return the os or no found.
        return "No found" if not wrap else wrap[0]


    def replace_labels(self, data_dict) -> dict:
        """Replace old label to new label. old label: label of the response."""

        label = {"username": "username", "email": "adresse email", "user_agent": "os emoji"}
        return {new_value: data_dict[old_value] for old_value, new_value in label.items()}


    def working_on_the_response(self):
        """Displaying the content of the get request"""

        # Recuperate label interest of the response.
        data = ["username", "email", "user_agent"]
        labels_of_the_request = {label: self.content[label] if label in self.content else None for label in data}

        # Update the os.
        labels_of_the_request["user_agent"] = self.getter_os(labels_of_the_request)

        # Update labels.
        data = self.replace_labels(labels_of_the_request)

        return data


    def response_display(self, response_of_the_request):
        """Replace the os to an emoji & display the response"""

        dico_emoji = {
            "windows": "🪟", 
            "linux": "🐧", 
            "mac os":"🍎",
            "ios": "🍎",
            "android": "🤖",
        }


        # Get the data of the response
        username = response_of_the_request["username"]
        email = response_of_the_request["adresse email"]
        emoji = dico_emoji[response_of_the_request["os emoji"]] if response_of_the_request["os emoji"] in dico_emoji else None

        # Display the response.
        response = f"L'adresse email de l'utilisateur {username} est {email}. Iel utilise le système d'exploitation {emoji}."

        print(response)
        return response

    def main(self):
        
        # Send a request to the url.
        self.calling_url()
        # Recuperate data, update dictionnary with label ask.
        response_of_the_request = self.working_on_the_response()
        # Display response.
        self.response_display(response_of_the_request)



    def test_url(self, path):
        """Verify response (code status) of the request"""
        res = requests.get(path)
        assert res.status_code == 200

    def test_response(self):
        """Verify the final sentence to display"""

        # With windows
        response_of_the_request = {
            "username": "jbaw",
            "adresse email": "jb26400@hotmail.fr",
            "os emoji": "windows"
        }

        response = self.response_display(response_of_the_request)
        assert response == "L'adresse email de l'utilisateur jbaw est jb26400@hotmail.fr. Iel utilise le système d'exploitation 🪟."


        # With android
        response_of_the_request = {
            "username": "jbaw",
            "adresse email": "jb26400@hotmail.fr",
            "os emoji": "android"
        }

        response = self.response_display(response_of_the_request)
        assert response == "L'adresse email de l'utilisateur jbaw est jb26400@hotmail.fr. Iel utilise le système d'exploitation 🤖."

        # With empty data.
        response_of_the_request = {
            "username": "",
            "adresse email": "",
            "os emoji": "aaa"
        }

        response = self.response_display(response_of_the_request)
        assert response == "L'adresse email de l'utilisateur  est . Iel utilise le système d'exploitation None."


    def test_replace_labels(self):
        """Test for verify the replacement of the label as the exercice"""

        data_dict = {'username': 'xavier', 'email': 'ezra_johns@example.org', 'user_agent': 'linux'}
        verification = {'username': 'xavier', 'adresse email': 'ezra_johns@example.org', 'os emoji': 'linux'}

        new_dict = self.replace_labels(data_dict)
        assert new_dict == verification
        
    
    def test_os(self):
        """Test of the scrap of the os"""

        sentence = {"user_agent": "okokok windows okok"}
        false_sentence = {"user_agent": "no os"}

        #With os.
        response1 = self.getter_os(sentence)
        assert response1 == "windows"

        # Without os.
        reponse2 = self.getter_os(false_sentence)
        assert reponse2 == "No found"





if __name__ == "__main__":

    path_url = "https://random-data-api.com/api/internet_stuff/random_internet_stuff"

    api = API(path_url)
    api.main()

    api.test_url(path_url)
    api.test_response()
    api.test_replace_labels()
    api.test_os()




"""
Les 3 questions

La première donnée que je choisirai serait des photos de la rue ou du bien immobilier. 
En effet l'utilisateur aura directement un aperçu de ce qu'il pourrait 
s'acheter et pourrait ainsi se projeter plus facilement.

La deuxième donnée serait les commerces et les accès routiers. Que ce soit 
les petits commerces alimentaires aux grandes surfaces. Ainsi la personne 
pourra également se projeter et ainsi combler son instinct primaire qui est de survivre.
Les espaces routiers que ce soit des voies rapides ou des bus/métro etc.

Enfin la dernière donnée pourrait tout ce qui ya en rapport avec le bien-être comme 
le climat car certaines personnes peuvent y être sensibles, les espaces 
verts ou les associations pour jeunes.


Le télétravail:

Étant de nature réservée l'alternance en télétravail serait un plus pour moi. En effet, en suivant la formation data science chez openclassrooms
je pourrai rester chez moi tout en suivant des cours et en gagnant en expérience professionnelle.


De plus, je pourrai m'organiser. Ayant déjà suivi une formation (non en alternance) chez openclassrooms
je pense combler vos désirs car je suis très travailleur et j'aime l'informatique, la programmation et la data science.

J'espère montrer ma motivation et mets en avant ma formation de développeur web python (bac+3) afin de monter mon profil à vos yeux.

Je vous remercie.

"""




