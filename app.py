from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def dashboard():
    data = {
        'today_sales': {'total_sales': '$5k', 'total_order': 500, 'product_sold': 9, 'new_customer': 12},
        'top_products': [
            {'name': 'Home Decor Range', 'popularity': '72%', 'sales': '82k'},
            {'name': 'Disney Princess Dress', 'popularity': '62%', 'sales': '41k'},
            {'name': 'Bathroom Essentials', 'popularity': '51%', 'sales': '31k'},
            {'name': 'Apple Smartwatch', 'popularity': '29%', 'sales': '29k'}
        ],
        'earnings': {'total_expense': '$6078.76', 'profit_increase': '48%', 'profit_percentage': '80%'},
        'visitor_insights': 'Graph data here',
        'customer_fulfillment': {'this_month': '$4765', 'last_month': '$4029'},
        'trending_now': [
            {'name': 'Home Decor Range', 'popularity': '78%'},
            {'name': 'Disney Princess Dress', 'popularity': '62%'}
        ],
        'customers': [
            {'name': 'John Doe', 'email': 'john@example.com', 'phone': '123-456-7890',
                'billing_address': '123 Main St', 'total_spent': '$500'},
            {'name': 'Jane Smith', 'email': 'jane@example.com', 'phone': '987-654-3210',
                'billing_address': '456 Elm St', 'total_spent': '$300'}
        ]
    }
    return render_template('dashboard.html', data=data)


if __name__ == '__main__':
    app.run(debug=True)
