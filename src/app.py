from flask import Flask, redirect, render_template, request
import psycopg2

app = Flask(__name__)
conn = psycopg2.connect(database='expense_management', user='pallisingh')
cursor = conn.cursor()

@app.route("/")
def add():
    return render_template('add.html')

@app.route('/expenses')
def expenses():
    cursor.execute('select * from expenses;')
    expenses = cursor.fetchall()
    return render_template('expenses.html', expenses=expenses)

@app.route("/addexpense",methods =['POST'])
def addexpense():
    date = request.form['expense_date']
    expensename = request.form['expense_name']
    amount = request.form['amount']
    category = request.form['category']
    cursor.execute('INSERT INTO expenses(expense_date,expense_name,amount,categories)'
    'VALUES (%s, %s, %s, %s)',
    (date, expensename,amount,category)
   )
    conn.commit()
    return redirect("/expenses")

@app.route("/delete/<id>")
def delete(id):
    cursor.execute('DELETE FROM expenses where id = %s', id)
    conn.commit()
    return redirect("/expenses")

@app.route("/edit/<id>")
def edit(id):
    cursor.execute('select * from expenses where id = %s', id)
    expense = cursor.fetchone()
    return render_template('update.html', expense=expense)

@app.route("/edit", methods=['POST'])
def update():
    new_date = request.form['expense_date']
    new_expensename = request.form['expense_name']
    new_amount = request.form['amount']
    new_category = request.form['category']
    # cursor.execute("""UPDATE expenses SET expense_date = new_date
    # """)
    return redirect("/expenses")
   # cursor.execute(""" UPDATE expense set expense_date = new_date)
#     # cursor.execute('UPDATE expenses SET expense_date=%s,expense_name,amount,categories'
#     #                 expense_date=date,
#     #                 expense_name=expensename,
    #                 amount=amount,
    #                 categories=category
    #                 where id = id""")
    # cursor.execute('UPDATE expenses SET expense_date='%s',expense_name='%s',amount='%s',categories='%s'
    # (new_date, new_expensename, new_amount, new_category) )
    # conn.commit()
    # return redirect("/expenses")
    




app.run(debug=True)
