import pymysql
import base64
from flask import Flask, render_template, request, redirect, url_for
from sql_dbt import host,user,password,db_name

try:
    connection = pymysql.connect(
        host=host,
        port=3306,
        user=user,
        password=password,
        database=db_name,
        cursorclass=pymysql.cursors.DictCursor)
    print("Successfully connected...")
    # try:
    #     with connection.cursor() as cursor:
    #         sql_qt = "SELECT * FROM Aston_Martin"
    #         cursor.execute(sql_qt)
    #
    #         column_names = [column[0] for column in cursor.description]
    #         print(column_names)
    #
    #         result = cursor.fetchall()
    #
    #         for row in result:
    #             print(row)
    # finally:
    #     print("")

except Exception as ex:
    print("Connection refused...")
    print(ex)
app = Flask(__name__)

# Маршрут по умолчанию для английской версии
@app.route('/')
def en():
    return render_template('AM.html')

# Маршрут по умолчанию для русской версии
@app.route('/ru')
def ru():

    return render_template('rAM.html')


@app.route('/button', methods=['POST'])
def button():
    if request.method == 'POST':
        model = request.form['model']
        if model == 'DB5':
            return redirect(url_for('DB5'))
        if model == 'DBS Superleggera':
            return redirect(url_for('DBS'))
        if model == 'DB7':
            return redirect(url_for('DB7'))
        if model == 'DB9':
            return redirect(url_for('DB9'))
        if model == 'DB11':
            return redirect(url_for('DB11'))
        if model == 'rDB5':
            return redirect(url_for('rDB5'))
        if model == 'rDBS Superleggera':
            return redirect(url_for('rDBS'))
        if model == 'rDB7':
            return redirect(url_for('rDB7'))
        if model == 'rDB9':
            return redirect(url_for('rDB9'))
        if model == 'rDB11':
            return redirect(url_for('rDB11'))
        if model == 'ru':
            return redirect(url_for(("ru")))
        if model == 'en':
            return redirect(url_for(("en")))



    return render_template('AM.html')







@app.route('/rDB5')
def rDB5():
    try:
        with connection.cursor() as cursor:
            sql_qt = "SELECT DB5 FROM ruAston_Martin WHERE DB5 IS NOT NULL"
            cursor.execute(sql_qt)

            result = cursor.fetchall()

            db5_values = [value['DB5'] for value in result if value['DB5'] is not None]
        with connection.cursor() as cursor:
            sql_qt = "SELECT DB5 FROM Aston_Martin_img WHERE DB5 IS NOT NULL"
            cursor.execute(sql_qt)

            result = cursor.fetchone()

            if result:
                image_data = result['DB5']

                # Кодирование данных изображения в base64
                encoded_image = base64.b64encode(image_data).decode('utf-8')

                # Передача закодированного изображения в шаблон HTML
                return render_template('rDB5.html', db5_values=db5_values, encoded_image=encoded_image)
            else:
                return "No image found in the database."
    except Exception as ex:
        print("Error executing SQL query...")
        print(ex)
        return "An error occurred while processing your request."


@app.route('/rDBS')
def rDBS():
    try:
        with connection.cursor() as cursor:
            sql_qt = "SELECT DBS FROM ruAston_Martin WHERE DBS IS NOT NULL"
            cursor.execute(sql_qt)

            result = cursor.fetchall()

            dbs_values = [value['DBS'] for value in result if value['DBS'] is not None]

        with connection.cursor() as cursor:
            sql_qt = "SELECT DBS FROM Aston_Martin_img WHERE DBS IS NOT NULL"
            cursor.execute(sql_qt)

            result = cursor.fetchone()

            if result:
                image_data = result['DBS']

                # Кодирование данных изображения в base64
                encoded_image = base64.b64encode(image_data).decode('utf-8')

                # Передача закодированного изображения в шаблон HTML
                return render_template('rDBS.html', dbs_values=dbs_values, encoded_image=encoded_image)
            else:
                return "No image found in the database."
    except Exception as ex:
        print("Error executing SQL query...")
        print(ex)
        return "An error occurred while processing your request."

@app.route('/rDB7')
def rDB7():
    try:
        with connection.cursor() as cursor:
            sql_qt = "SELECT DB7 FROM ruAston_Martin WHERE DB7 IS NOT NULL"
            cursor.execute(sql_qt)

            result = cursor.fetchall()

            db7_values = [value['DB7'] for value in result if value['DB7'] is not None]

        with connection.cursor() as cursor:
            sql_qt = "SELECT DB7 FROM Aston_Martin_img WHERE DB7 IS NOT NULL"
            cursor.execute(sql_qt)

            result = cursor.fetchone()

            if result:
                image_data = result['DB7']

                # Кодирование данных изображения в base64
                encoded_image = base64.b64encode(image_data).decode('utf-8')

                # Передача закодированного изображения в шаблон HTML
                return render_template('rDB7.html', db7_values=db7_values, encoded_image=encoded_image)
            else:
                return "No image found in the database."
    except Exception as ex:
        print("Error executing SQL query...")
        print(ex)
        return "An error occurred while processing your request."

@app.route('/rDB9')
def rDB9():
    try:
        with connection.cursor() as cursor:
            sql_qt = "SELECT DB9 FROM ruAston_Martin WHERE DB9 IS NOT NULL"
            cursor.execute(sql_qt)

            result = cursor.fetchall()

            db9_values = [value['DB9'] for value in result if value['DB9'] is not None]

        with connection.cursor() as cursor:
            sql_qt = "SELECT DB9 FROM Aston_Martin_img WHERE DB9 IS NOT NULL"
            cursor.execute(sql_qt)

            result = cursor.fetchone()

            if result:
                image_data = result['DB9']

                # Кодирование данных изображения в base64
                encoded_image = base64.b64encode(image_data).decode('utf-8')

                # Передача закодированного изображения в шаблон HTML
                return render_template('rDB9.html', db9_values=db9_values, encoded_image=encoded_image)
            else:
                return "No image found in the database."
    except Exception as ex:
        print("Error executing SQL query...")
        print(ex)
        return "An error occurred while processing your request."

@app.route('/rDB11')
def rDB11():
    try:
        with connection.cursor() as cursor:
            sql_qt = "SELECT DB11 FROM ruAston_Martin WHERE DB11 IS NOT NULL"
            cursor.execute(sql_qt)

            result = cursor.fetchall()

            db11_values = [value['DB11'] for value in result if value['DB11'] is not None]

        with connection.cursor() as cursor:
            sql_qt = "SELECT DB11 FROM Aston_Martin_img WHERE DB11 IS NOT NULL"
            cursor.execute(sql_qt)

            result = cursor.fetchone()

            if result:
                image_data = result['DB11']

                # Кодирование данных изображения в base64
                encoded_image = base64.b64encode(image_data).decode('utf-8')

                # Передача закодированного изображения в шаблон HTML
                return render_template('rDB11.html', db11_values=db11_values, encoded_image=encoded_image)
            else:
                return "No image found in the database."
    except Exception as ex:
        print("Error executing SQL query...")
        print(ex)
        return "An error occurred while processing your request."


@app.route('/DB5')
def DB5():
    try:
        with connection.cursor() as cursor:
            sql_qt = "SELECT DB5 FROM Aston_Martin WHERE DB5 IS NOT NULL"
            cursor.execute(sql_qt)

            result = cursor.fetchall()

            db5_values = [value['DB5'] for value in result if value['DB5'] is not None]
        with connection.cursor() as cursor:
            sql_qt = "SELECT DB5 FROM Aston_Martin_img WHERE DB5 IS NOT NULL"
            cursor.execute(sql_qt)

            result = cursor.fetchone()

            if result:
                image_data = result['DB5']

                # Кодирование данных изображения в base64
                encoded_image = base64.b64encode(image_data).decode('utf-8')

                # Передача закодированного изображения в шаблон HTML
                return render_template('DB5.html', db5_values=db5_values, encoded_image=encoded_image)
            else:
                return "No image found in the database."
    except Exception as ex:
        print("Error executing SQL query...")
        print(ex)
        return "An error occurred while processing your request."


@app.route('/DBS')
def DBS():
    try:
        with connection.cursor() as cursor:
            sql_qt = "SELECT DBS FROM Aston_Martin WHERE DBS IS NOT NULL"
            cursor.execute(sql_qt)

            result = cursor.fetchall()

            dbs_values = [value['DBS'] for value in result if value['DBS'] is not None]

        with connection.cursor() as cursor:
            sql_qt = "SELECT DBS FROM Aston_Martin_img WHERE DBS IS NOT NULL"
            cursor.execute(sql_qt)

            result = cursor.fetchone()

            if result:
                image_data = result['DBS']

                # Кодирование данных изображения в base64
                encoded_image = base64.b64encode(image_data).decode('utf-8')

                # Передача закодированного изображения в шаблон HTML
                return render_template('DBS.html', dbs_values=dbs_values, encoded_image=encoded_image)
            else:
                return "No image found in the database."
    except Exception as ex:
        print("Error executing SQL query...")
        print(ex)
        return "An error occurred while processing your request."

@app.route('/DB7')
def DB7():
    try:
        with connection.cursor() as cursor:
            sql_qt = "SELECT DB7 FROM Aston_Martin WHERE DB7 IS NOT NULL"
            cursor.execute(sql_qt)

            result = cursor.fetchall()

            db7_values = [value['DB7'] for value in result if value['DB7'] is not None]

        with connection.cursor() as cursor:
            sql_qt = "SELECT DB7 FROM Aston_Martin_img WHERE DB7 IS NOT NULL"
            cursor.execute(sql_qt)

            result = cursor.fetchone()

            if result:
                image_data = result['DB7']

                # Кодирование данных изображения в base64
                encoded_image = base64.b64encode(image_data).decode('utf-8')

                # Передача закодированного изображения в шаблон HTML
                return render_template('DB7.html', db7_values=db7_values, encoded_image=encoded_image)
            else:
                return "No image found in the database."
    except Exception as ex:
        print("Error executing SQL query...")
        print(ex)
        return "An error occurred while processing your request."

@app.route('/DB9')
def DB9():
    try:
        with connection.cursor() as cursor:
            sql_qt = "SELECT DB9 FROM Aston_Martin WHERE DB9 IS NOT NULL"
            cursor.execute(sql_qt)

            result = cursor.fetchall()

            db9_values = [value['DB9'] for value in result if value['DB9'] is not None]

        with connection.cursor() as cursor:
            sql_qt = "SELECT DB9 FROM Aston_Martin_img WHERE DB9 IS NOT NULL"
            cursor.execute(sql_qt)

            result = cursor.fetchone()

            if result:
                image_data = result['DB9']

                # Кодирование данных изображения в base64
                encoded_image = base64.b64encode(image_data).decode('utf-8')

                # Передача закодированного изображения в шаблон HTML
                return render_template('DB9.html', db9_values=db9_values, encoded_image=encoded_image)
            else:
                return "No image found in the database."
    except Exception as ex:
        print("Error executing SQL query...")
        print(ex)
        return "An error occurred while processing your request."

@app.route('/DB11')
def DB11():
    try:
        with connection.cursor() as cursor:
            sql_qt = "SELECT DB11 FROM Aston_Martin WHERE DB11 IS NOT NULL"
            cursor.execute(sql_qt)

            result = cursor.fetchall()

            db11_values = [value['DB11'] for value in result if value['DB11'] is not None]

        with connection.cursor() as cursor:
            sql_qt = "SELECT DB11 FROM Aston_Martin_img WHERE DB11 IS NOT NULL"
            cursor.execute(sql_qt)

            result = cursor.fetchone()

            if result:
                image_data = result['DB11']

                # Кодирование данных изображения в base64
                encoded_image = base64.b64encode(image_data).decode('utf-8')

                # Передача закодированного изображения в шаблон HTML
                return render_template('DB11.html', db11_values=db11_values, encoded_image=encoded_image)
            else:
                return "No image found in the database."
    except Exception as ex:
        print("Error executing SQL query...")
        print(ex)
        return "An error occurred while processing your request."

if __name__ == '__main__':
    a=app.run(debug=True)


