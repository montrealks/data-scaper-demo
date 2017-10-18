from flask import Flask, jsonify, render_template, request, Response, make_response, json
import csv
from io import StringIO
import configs
from src.models import GetTheGaurdianData

app = Flask(__name__, template_folder="src/templates/", static_folder="src/static")


@app.route('/', methods=['GET', 'POST'])
def getting_started():
    print("here I am ")
    return render_template('base.html')
    
    
@app.route('/guardian_homepage', methods=['GET'])
def guardian_homepage():
    g = GetTheGaurdianData()
    g.load_home_page()
    headlines = g.load_headlines()
    return jsonify(headlines)


@app.route('/get_per_article_meta_data', methods=['GET'])
def per_article_meta():
    g = GetTheGaurdianData
    position = request.args.get("position")
    
    return jsonify(g.get_per_page_details(int(position)))
    
@app.route('/download', methods=['POST', 'GET'])
def download():
    print('inside download')
    csvList = GetTheGaurdianData.FORMATTED_FOR_CSV
    # print(csvList)
    si = StringIO()
    cw = csv.writer(si)
    cw.writerow(["Article Title", "Headline Kicker", "body", "Link", "Authors", "tags", "Date"])
    cw.writerows(csvList)
    output = make_response(si.getvalue())
    output.headers["Content-Disposition"] = "attachment; filename=TheGuardianHeadLines.csv"
    output.headers["Content-type"] = "text/csv"
    
    return output

@app.route('/csvmaker', methods=['POST'])
def post():
    g = GetTheGaurdianData
    csvList = []
    data = request.get_json(force=True)
    
    for row in data.values():
        print(row)
        for i, s in enumerate(row):
            row[i] = s.replace('\n', '').replace('\xa0', '')
        csvList.append(row)
        print(row)

    g.FORMATTED_FOR_CSV = csvList
    
    return jsonify({'status': 'complete'})

    
    
    


    


    


app.run(host='0.0.0.0', port=8080, debug=True) if __name__ == '__main__' and configs.DEBUG else None


