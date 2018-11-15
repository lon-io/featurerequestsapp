from flask import Flask, render_template, url_for, request, redirect

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html', title="Home")

@app.route('/request/create', methods=('POST', 'GET'))
def create_feature_request():
    if request.method == "POST":
        title = request.form['title']
        description = request.form['description']
        client = request.form['client']
        client_priority = request.form['client_priority']
        target_date = request.form['target_date']
        product_area = request.form['product_area']

        return redirect(url_for('feature_request',
            title=title,
            description=description,
            client=client,
            client_priority=client_priority,
            target_date=target_date,
            product_area=product_area
            ))

@app.route('/request', methods=["GET"])
def feature_request():
    title = request.args.get('title')
    description = request.args.get('description')
    client = request.args.get('client')
    client_priority = request.args.get('client_priority')
    target_date = request.args.get('target_date')
    product_area = request.args.get('product_area')

    return render_template('feature_request.html',
        title=title,
        description=description,
        client=client,
        client_priority=client_priority,
        target_date=target_date,
        product_area=product_area
        )

if __name__ == "__main__":
    app.run(debug=True, port=8080)
