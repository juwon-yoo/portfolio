from flask import Flask, render_template, request, url_for
from flask_restx import Api, Resource, reqparse
from sqlalchemy import create_engine
from sqlalchemy import text

app = Flask(__name__)
api = Api(app)

# DB 연결
test_config=None

if test_config is None:      
    app.config.from_pyfile("config.py")
else:
    app.config.update(test_config)

database = create_engine(app.config['DB_URL'], encoding = 'utf-8', max_overflow = 0)   
app.database = database

parser = reqparse.RequestParser()
parser.add_argument('id', help='프로젝트ID', type=int, required=True)

@app.route('/main')
def main():
    return render_template('main.html')

@app.route('/detail/<id>', methods=['GET'])
def contact():
    if request.method=='GET':

        sql = 'SELECT * FROM project'
        query = {
            'id': id
        }      
        rows = app.database.execute(text(sql)).fetchall()
        retVal = []
        for row in rows:
            r = {  
                    'p_name'     : row['p_name'],
                    'team'   : row['team'],
                    'stack'     : row['stack'],
                    'd'     : row['detail'],
                    'id'   : row['id']                                 
                }
            retVal.append(r)
        return render_template('detail.html', label=retVal)



if __name__ == "__main__":
    #서버 시작
    app.run(debug=True, host='0.0.0.0', port=80)