from app import app, Config
from flask import Flask, request, render_template, redirect, abort
from app import edCoder
import sqlite3
from urllib.parse import urlparse

host = app.config['HOST']


@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        original_url = request.form.get('url')
        if urlparse(original_url).scheme == '':
            original_url = 'http://' + original_url
        with sqlite3.connect(app.config['SQLITE']) as conn:
            cursor = conn.cursor()
            insert_row = """
                INSERT INTO TINY (URL)
                    VALUES ('%s')
                """ % (original_url)
            result_cursor = cursor.execute(insert_row)
            encoded_string = edCoder.toBase62(result_cursor.lastrowid)
        return render_template('home.html', short_url=host + encoded_string)
    return render_template('home.html')


@app.route('/api-create')
def apiCreate():
    url = request.args.get('url')
    if url is None or url == '':
        abort(500)
    if urlparse(url).scheme == '':
        url = 'http://' + url
    with sqlite3.connect(app.config['SQLITE']) as conn:
        cursor = conn.cursor()
        insert_row = """
            INSERT INTO TINY (URL)
                VALUES ('%s')
            """ % (url)
        result_cursor = cursor.execute(insert_row)
        encoded_string = edCoder.toBase62(result_cursor.lastrowid)
        short_url = host + encoded_string
    return short_url


@app.route('/<short_url>')
def redirect_short_url(short_url):
    decoded_string = edCoder.toBase10(short_url)
    redirect_url = host
    with sqlite3.connect(app.config['SQLITE']) as conn:
        cursor = conn.cursor()
        select_row = """
                SELECT URL FROM TINY
                    WHERE ID=%s
                """ % (decoded_string)
        result_cursor = cursor.execute(select_row)
        try:
            redirect_url = result_cursor.fetchone()[0]
        except Exception as e:
            print(e)
    return redirect(redirect_url)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
