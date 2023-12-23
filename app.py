from flask import Flask, render_template

app = Flask(__name__, static_url_path='/static')

@app.route('/')
def index():
    
    designers_data = [
        {
            'name': 'Epic Designs',
            'rating': 4,
            'description': 'Passionate team of 4 designers working out <br> of Bangalore with an experience of 8 years.',
            'projects': 57,
            'experience': 8,
            'price': '$$$',
            'tel1': '+91 - 984532853',
            'tel2': '+91 - 984532854'
        },
        {
            'name': 'Studio - D3',
            'rating': 3,
            'description': 'Passionate team of 4 designers working out <br> of Bangalore with an experience of 6 years.',
            'projects': '43',
            'experience': 6,
            'price': '$$',
            'tel1': '+91 - 984532874',
            'tel2': '+91 - 984532876'
        },
        {
            'name': 'House of designs',
            'rating': 3.5,
            'description': 'Passionate team of 4 designers working out <br> of Bangalore with an experience of 3 years.',
            'projects': 40,
            'experience': 3,
            'price': '$$$',
            'tel1': '+91 - 984532812',
            'tel2': '+91 - 984532821'
        },
        {
            'name': 'Royal Designs',
            'rating': 4,
            'description': 'Passionate team of 4 designers working out <br> of Bangalore with an experience of 2 years.',
            'projects': 20,
            'experience': 2,
            'price': '$$$$',
            'tel1': '+91 - 984532832',
            'tel2': '+91 - 984532898'
        },
        {
            'name': 'Luxe Interiors',
            'rating': 3,
            'description': 'Passionate team of 4 designers working out <br> of Bangalore with an experience of 4 years.',
            'projects': 60,
            'experience': 4,
            'price': '$$$',
            'tel1': '+91 - 984532809',
            'tel2': '+91 - 984532818'
        }
    ]
    num_rectangles = len(designers_data)
    colors = ['#FFFCF2' if i % 2 == 0 else '#FFF' for i in range(num_rectangles)]
    return render_template('index.html', num_rectangles=num_rectangles, colors=colors,
                           designers_data=designers_data)

if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True)
