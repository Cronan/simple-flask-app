from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
@app.route('/index')
def index():
    return render_template('clean_blog_basic.html', heading='Home',
        title='New Product - Offical Home Page',
        subheading='This page will essentially just be an opt in page.')


@app.route('/blog')
def blog():
    return render_template('clean_blog_blog.html', heading='Blog',
        title='New Product | Blog',
        subheading='This will be somewhere to host and post blogs.')


@app.route('/contact')
def contact():
    return render_template('clean_blog_basic.html', heading='Contact',
        title='New Product | Contact Us',
        subheading='This will just hold text.')


@app.route('/buy')
def buy():
    return render_template('clean_blog_basic.html', heading='Buy Product',
        title='New Product | Buy the Product',
        subheading='This will explain what the product is, but no way to order it like a retail site.')