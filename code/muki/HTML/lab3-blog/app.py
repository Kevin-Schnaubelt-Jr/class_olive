from flask import Flask, render_template

app = Flask(__name__)

x=9

blog_posts = [
    {
        'title': 'something',
        'author': 'A. Named Dude',
        'date': 'September 19, 2022',
        'content': 'Soufflé bonbon cheesecake I love candy I love bonbon. Croissant topping croissant I love powder I love. Sesame snaps dragée chupa chups cake apple pie cake marzipan.'
    },
    {
        'title': 'something else',
        'author': 'A. Named Dude',
        'date': 'September 18, 2022',
        'content': 'Lemon drops I love gummi bears danish cotton candy I love. Wafer carrot cake gummi bears sweet roll cheesecake wafer cheesecake tiramisu. Fruitcake jelly-o tootsie roll I love cupcake gingerbread soufflé marzipan. Oat cake jelly beans lemon drops lemon drops sugar plum sweet gummies.'
    },
    {
        'title': 'something previous',
        'author': 'A. Named Dude',
        'date': 'September 17, 2022',
        'content': 'Tootsie roll I love pie apple pie I love soufflé macaroon tart tart. Chocolate cake danish powder biscuit muffin. Icing biscuit candy halvah gummi bears dessert tart wafer shortbread.'
    },
    {
        'title': 'things that are named',
        'author': 'A. Named Dude',
        'date': 'September 16, 2022',
        'content': 'Cookie toffee I love croissant carrot cake I love cake cupcake. Croissant croissant jujubes bonbon chupa chups wafer cookie dessert sweet. Macaroon I love oat cake chupa chups icing candy.'
    },
]


@app.route('/')
def index():
    return render_template('lab3blog.html', x=x, blog_posts=blog_posts)

app.run(debug=True)
