from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def root():
   return render_template('cwTemplates/cwbase.html'), 200

@app.route('/Nations')
def nations():
   return render_template('cwTemplates/cwnations.html')

@app.route('/Nations/Africa')
def africa():
   return render_template('cwTemplates/cwafrica.html')

@app.route('/Nations/Americas')
def americas():
   return render_template('cwTemplates/cwamericas.html')

@app.route('/Nations/Asia')
def asia():
   return render_template('cwTemplates/cwasia.html')

@app.route('/Nations/Europe')
def europe():
   return render_template('cwTemplates/cweurope.html')

@app.route('/Nations/Oceania')
def oceania():
   return render_template('cwTemplates/cwoceania.html')

@app.route('/Nations/Formable')
def formable():
   return render_template('cwTemplates/cwformable.html')

@app.route('/Events')
def events():
   return render_template('cwTemplates/cwevents.html')

@app.route('/Events/CountryList')
def countrylist():
   return render_template('cwTemplates/cwnationlist.html')

@app.route('/Events/General')
def general():
   return render_template('cwTemplates/cwgeneral.html')

@app.route('/Developer')
def Developer():
   return render_template('cwTemplates/cwdeveloper.html')

@app.route('/Strategy')
def Strategy():
   return render_template('cwTemplates/cwstrategy.html')

if __name__ == "__main__":
   app.run(host='0.0.0.0', debug=True)
