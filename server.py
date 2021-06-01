from flask import *
import csv
from werkzeug.utils import secure_filename
import os
import datetime
app = Flask(__name__)


@app.route('/')
def my_home():
	return render_template('index.html')


@app.route('/<string:page_name>')
def html_page(page_name):
	return render_template(page_name)

def write_to_file(data):
	with open("C:\\Users\\Qadeer Rizvi\\Desktop\\portfolio\\database.txt", mode = 'a') as database:
		email = data["email"]
		subject = data["subject"]
		message = data["message"]
		file = database.write(f'\n{email}, {subject}, {message}')


def write_to_csv(data):
	with open("C:\\Users\\Qadeer Rizvi\\Desktop\\portfolio\\database.csv", mode = 'a', newline='') as database2:
		email = data["email"]
		subject = data["subject"]
		message = data["message"]
		date_time = datetime.datetime.now()
		headers = ['Email', 'Subject', 'Message', 'Date & Time']
		csv_writer = csv.writer(database2, delimiter = ',', quotechar='"',quoting=csv.QUOTE_MINIMAL)
		csv_writer.writerow([email, subject, message, date_time])

@app.route('/submit_data', methods=['POST', 'GET'])
def submit_form():
	if request.method== 'POST':
		try:
			data = request.form.to_dict()
			write_to_csv(data)
			return redirect("/thankyou.html")
		except:
			return 'did not save to database.'
	else:
		return 'something went wrong. Try again!'


@app.route('/work.html')
def work1():
	return render_template('work.html')

@app.route('/work.html/download', methods = ['GET', 'POST'])
def work1_download():
	file_path = './downloads/work1.rar'
	if request.method=='GET':
		return send_file(file_path, as_attachment=True)
@app.route('/work2.html')
def work2():
	return render_template('work2.html')

@app.route('/work2.html/download', methods = ['GET', 'POST'])
def work2_download():
	file_path = './downloads/work2.rar'
	if request.method=='GET':
		return send_file(file_path, as_attachment=True)

@app.route('/work3.html')
def work3():
	return render_template('work3.html')

@app.route('/work3.html/download', methods = ['GET', 'POST'])
def work3_download():
	file_path = './downloads/work3.rar'
	if request.method=='GET':
		return send_file(file_path, as_attachment=True)


@app.route('/work4.html')
def work4():
	return render_template('work4.html')

@app.route('/work4.html/download', methods = ['GET', 'POST'])
def work4_download():
	file_path = './downloads/work4.rar'
	if request.method=='GET':
		return send_file(file_path, as_attachment=True)


@app.route('/work5.html')
def work5():
	return render_template('work5.html')

@app.route('/work5.html/download', methods = ['GET', 'POST'])
def work5_download():
	file_path = './downloads/work5.rar'
	if request.method=='GET':
		return send_file(file_path, as_attachment=True)





