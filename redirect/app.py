from flask import Flask

appname = "app"

app = Flask(appname)
app.config.from_object(appname)

app.config.update(dict(
    DEBUG=True
))

@app.route('/')
def test():
    return "Hello 301 in a Box!\n"

@app.route('/api/records', methods=['GET'])
def get_records():
    """Get ALIAS records"""
    return "This will retrieve ALIAS records\n"

@app.route('/api/records', methods=['POST'])
def post_record():
    """Add ALIAS record to database"""
    return "This will add an ALIAS record to the database\n"

@app.route('/api/records/<record_id>', methods=['PUT'])
def put_record(record_id):
    """Update ALIAS record"""
    return "This will update an ALIAS record\n"

@app.route('/api/records/<record_id>', methods=['DELETE'])
def delete_record(record_id):
    """Delete ALIAS record from the database"""
    return "This will delete an ALIAS record from the database\n"

if __name__ == '__main__':
    app.run()