import psycopg2
from urllib.parse import urlparse
from flask import request, render_template, redirect, abort
from app import app, edCoder, database

host = app.config['HOST']

@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        original_url = request.form.get('url')
        if urlparse(original_url).scheme == '':
            original_url = 'http://' + original_url
        conn = database.MyDatabase()
        insert_row = """
                INSERT INTO tiny(url) VALUES('%s') RETURNING id;
                """ % (original_url)
        cur = conn.cursor()
        cur.execute(insert_row)
        conn.commit()
        result_cursor = cur.fetchone()[0]
        encoded_string = edCoder.toBase62(result_cursor)
        return render_template('home.html', short_url=host + encoded_string)
    return render_template('home.html')


@app.route('/api-create')
def api_create():
    url = request.args.get('url')
    if url is None or url == '':
        abort(500)
    if urlparse(url).scheme == '':
        url = 'http://' + url
    conn = psycopg2.connect(host=app.config['DBHOST'], port=app.config['DBPORT'],
                        database=app.config['DBDB'],
                        user=app.config['DBUSER'], password=app.config['DBPASS'])
    insert_row = """
            INSERT INTO tiny(url) VALUES('%s') RETURNING id;
            """ % (url)
    cur = conn.cursor()
    cur.execute(insert_row)
    conn.commit()
    result_cursor = cur.fetchone()[0]
    encoded_string = edCoder.toBase62(result_cursor)
    short_url = host + encoded_string
    return short_url


@app.route('/<short_url>')
def redirect_short_url(short_url):
    decoded_string = edCoder.toBase10(short_url)
    redirect_url = host
    conn = psycopg2.connect(host=app.config['DBHOST'], port=app.config['DBPORT'],
                        database=app.config['DBDB'],
                        user=app.config['DBUSER'], password=app.config['DBPASS'])
    select_row = """
            SELECT url FROM tiny WHERE ID=%s;
            """ % (decoded_string)
    cur = conn.cursor()
    cur.execute(select_row)
    try:
        redirect_url = cur.fetchone()[0]
    except Exception as error:
        print(error)
    return redirect(redirect_url)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
