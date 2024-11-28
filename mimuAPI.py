import psycopg2
import json
from flask import Flask, jsonify
app = Flask(__name__)

def load_config():
    with open('config.json', 'r') as file:
        return json.load(file)
    
def getConn():
    try:
        config = load_config()
        db_config = config['database']
        pgdb = f"dbname={db_config['database']} host={db_config['host']} port=5432 user={db_config['user']} password={db_config['password']}"
        conn = psycopg2.connect (pgdb)
        return conn
    except Exception as e:
        print(e) 

@app.route('/village/', methods=['GET'])
def getVillage():
    try:
        conn = getConn()
        cursor = conn.cursor()
        stmt = """
        SELECT village,villagetract,
        township,district,states
        FROM tbl_mimu_villages;
        """
        cursor.execute(stmt)
        rows = cursor.fetchall()
        if rows:
            return jsonify(rows)
        else:
            return jsonify({"message": "No villages found!!!."}), 404
    except Exception as e:
        return jsonify({"error": str(e)})

@app.route('/village/states/<states>', methods=['GET'])
def get_villages_by_states(states):
    try:
        connection = getConn()
        cursor = connection.cursor()
        stmt = """
        SELECT village,villagetract,township, 
            district, states
        FROM tbl_mimu_villages WHERE states = %s;
        """     
        cursor.execute(stmt, (states,))
        rows = cursor.fetchall()
        if rows:
            return jsonify(rows)
        else:
            return jsonify({"message": f"No villages found for State '{states}'."}), 404
    except Exception as e:
        return jsonify({"error": str(e)})
if __name__ == '__main__':
    app.run(host='0.0.0.0',port=8000)
