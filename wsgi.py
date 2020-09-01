from main import create_app

app = create_app()

""" for development purpose only... should be commented for deployment """
app.run(debug=True)
