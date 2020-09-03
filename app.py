#!env/bin/python

#https://apify.com/covid-19
from flask import Flask, jsonify, abort, make_response, request

#base_url = "https://api.apify.com/v2/key-value-stores/tVaYRsPHLjNdNBu7S/records/LATEST?disableRedirect=true"

app = Flask(__name__)

destination = [
        { 'id' : 1 ,
          'Country' : 'India' ,
          'Status' : [] ,
          'Description' : 'Best known for its diverse culture' ,
          'Expense' : 'INR 20,000 - 30,000' ,
          'Attractions' : 'Taj Mahal, Amber Palace, Hawa Mahal'
        } ,

        { 'id' : 2 ,
          'Country' : 'Switzerland',
          'Status' : [] ,
          'Description' : 'Known for its astounding scenery' ,
          'Expense' : 'INR 1,00,000 - 2,00,000' ,
          'Attractions' : 'Zurich, Geneva, Lucerne'
        }
    ]

@app.errorhandler(404)
def not_found(error):
    return make_response(jsonify({'error': 'Not Found'}), 404)


@app.route('/travel/api/destination', methods = ['POST'])
def create_dest():
    if not request.json or not 'Country' in request.json:
        abort(400)
    dest = {
          'id' :destination[-1]['id'] +1  ,
          'Country' : request.json['Country'] ,
          'Status' : [] ,
          'Description' : request.json.get('Description',"") ,
          'Expense' : request.json.get('Expense',""),
          'Attractions' : request.json.get('Attractions',"")
        }
    destination.append(dest)
    return jsonify({'dest':dest}),201

@app.route('/travel/api/destination', methods = ['GET'])
def get_destis():
    return jsonify({'destination':destination})


@app.route('/travel/api/destination/<int:dest_id>', methods = ['GET'])
def get_dest(dest_id):

#    data = {}
#   req = requests.get(base_url)

#   if req.status_code == 200:
#        data = json.loads(req.text)

#    new_data = {}
#    for item in data:
#        country = item.pop('country')
#        new_data[country] = item['infected']

#    for i in range(len(destination)):
#        if destination[i]['Country'] in new_data:
#            if new_data[destination[i]['country']] < 10000:
#                destination[i]['status'] = "Safe"
#            elif new_data[destination[i]['country']] >= 10000 or new_data[destination[i]['country']] < 300000:
#                destination[i]['status'] = "Moderately Safe"
#            else:
#                destination[i]['status'] = "Extremely Unsafe"


    dest = [dest for dest in destination if dest['id'] == dest_id]
    if len(dest) == 0:
        abort(404)
    return jsonify({'destination' : dest[0]})

if __name__ == '__main__':
    app.run(debug=True)
