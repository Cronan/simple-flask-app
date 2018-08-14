from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
@app.route('/index')
def index():
    return render_template('clean_blog_basic.html', heading='Home',
    title='Keenan Product - Offical Home Page',
    subheading='This page will essentially just be an opt in page, so it would have to capture email which would then be sent to some sort of email management site like Mailchimp.')


@app.route('/blog')
def blog():
    return render_template('clean_blog_blog.html', heading='Blog',
    title='Keenan Product | Blog',
    subheading='This will be somewhere to host and post blogs. No option for commenting. Will also have an email capture.')


@app.route('/contact')
def contact():
    return render_template('clean_blog_basic.html', heading='Contact',
    title='Keenan Product | Contact Keenan',
    subheading='This will just hold text, but would also have an email capture same as before')


@app.route('/buy')
def buy():
    return render_template('clean_blog_basic.html', heading='Buy Product',
    title='Keenan Product | Buy the Product',
    subheading='This will also just be text with an email capture, will explain what the product is, but no way to order it like a retail site. They will get a bribe to opt in, such as the first chapter of the book I’ll be selling, and would then have the option to buy it once they’re in the funnel')