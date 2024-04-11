# run.py
from app import app
from app.routes.add_routes import add
from app.routes.minute_route import minute


@app.route("/")
def main():
    return "Sefl learning python with Flask!"

app.register_blueprint(add)
app.register_blueprint(minute)

if __name__ == '__main__':
    print("chạy run")
    app.run(host='0.0.0.0', port=8080,debug=True)
