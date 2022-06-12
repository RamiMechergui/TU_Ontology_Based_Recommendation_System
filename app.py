from flask import Flask,render_template,redirect,request
import rdflib
app = Flask(__name__)
g = rdflib.Graph()
g.parse("My_Ontology.owl")

@app.route('/subscriber',methods=['POST'])
def Subsriber():
    First_Name = request.form.get('First_Name')
    Last_Name = request.form.get('Last_Name')
    Email = request.form.get('Email')
    Password = request.form.get('Password')
    Place_of_Birth = request.form.get('Place_of_Birth')
    Chosen_University = request.form.get('Chosen_University')
    q = """
        PREFIX ab: <https://tuapirecommendationsystem.herokuapp.com/My_Ontology#>
        SELECT  ?x ?name_of_university ?city ?Data_Endpoint
        WHERE {
               FILTER regex(?city, \"""" + Place_of_Birth + """\")
               ?x ab:University_Name ?name_of_university  .
               ?x ab:Corresponding_City ?city .
               ?x ab:Data_Endpoint ?Data_Endpoint
               }"""
    q2 = """PREFIX ab: <https://tuapirecommendationsystem.herokuapp.com/My_Ontology#>
            SELECT  ?x ?name_of_university ?city ?Data_Endpoint
            WHERE {
                FILTER regex(?name_of_university,\""""+Chosen_University+"""\")
                ?x ab:University_Name ?name_of_university  .
                ?x ab:Corresponding_City ?city .
                ?x ab:Data_Endpoint ?Data_Endpoint
                 }"""
    Chosen_Topic = request.form.get('Chosen_Topic')
    for r in g.query(q):
        Endpoint_1 = r['Data_Endpoint']

    for M in g.query(q2):
        Endpoint_2 = M['Data_Endpoint']

    return render_template('subscriber.html',Endpoint_1=Endpoint_1,First_Name=First_Name,Last_Name=Last_Name,Endpoint_2=Endpoint_2,Email=Email,Password=Password,Place_of_Birth=Place_of_Birth,Chosen_University=Chosen_University,Chosen_Topic=Chosen_Topic)

@app.route('/index')
def hello_world():  # put application's code here
    return render_template('index.html')

@app.route('/')
def Main_Redirection():
    return redirect('/index')

@app.route('/<string:url>')
def Routes_Redirection(url):
    return redirect('/index')

if __name__ == '__main__':
    app.run()
