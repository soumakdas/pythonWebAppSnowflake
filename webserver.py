#import packages
from flask import Flask, render_template, request
from pandas import DataFrame

from snowflakeConnection import sfconnect
import pandas as pd

#Flask Web Application
app = Flask("my website")

@app.route('/')
def homepage():
    cur = cnx.cursor().execute("select color_name, count(*) from colors group by color_name having count(*) > 50 order by count(*) desc;")
    rows = pd.DataFrame(cur.fetchall(), columns=['Color UID', 'Votes'])
    dfhtml = rows.to_html(index=False)
    return render_template('index.html', dfhtml=dfhtml)


@app.route('/submit')
def submitpage():
    return render_template('submit.html')

@app.route('/thanks4submit', methods=["POST"])
def thanks4submit():
    colorname = request.form.get("cname")
    username = request.form.get("uname")
    cnx.cursor().execute("INSERT INTO COLORS(COLOR_UID, COLOR_NAME) " +"SELECT COLOR_UID_SEQ.nextval, '" + colorname+ "'")
    return render_template("thanks4submit.html",
                           colorname=colorname,
                           username=username
                           )

@app.route("/coolcharts")
def coolcharts():
    cur = cnx.cursor().execute("Select Color_name, count(*) from colors group by color_name order by count(*) desc;")
    data4charts=pd.DataFrame(cur.fetchall(), columns=['color','vote'])
    data4chartsJSON = data4charts.to_json(orient='records')
    return render_template("coolcharts.html", data4chartsJSON=data4chartsJSON)

# Snowflake
cnx = sfconnect()


#print(rows)

#test dataframe


app.run()