import csv
import matplotlib.pyplot as plt

with open('data.csv', 'r') as file:
    reader = csv.reader(file)
    next(reader)
    rows = list(reader)
# taking input from user
str, sid = input().split()
# sid = input()

# Generate the HTML table
if(str == "-s"):
    sum = 0
    table_html = '<table border=2px solid black>'
    table_html += '<tr>'
    table_html += '<th>Student id</th>'
    table_html += '<th>Course id</th>'
    table_html += '<th>Marks</th>'
    table_html += '</tr>'

    for row in rows:
        if(sid == row[0]):
            sum += int(row[2])
            for cell in row:
                table_html += '<td>{}</td>'.format(cell)
            table_html += '</tr>'
    table_html += '<tr>'
    table_html += '<td colspan = 2 align=center>Total Marks</td>'
    table_html += '<td>{}</td>'.format(sum)
    table_html += '</tr>'
    table_html += '</table>'

    # Save the HTML table to a file
    with open('student.html', 'w') as file:
        file.write("<title>" + "Students Details" + "</title>")
        file.write("<h1>" + "Students Details"  + "</h1>")
        file.write(table_html)

# Course id section
elif(str == "-c"):
    table_html = '<table border=2px solid black>'
    table_html += '<tr>'
    table_html += '<th>Average Marks</th>'
    table_html += '<th>Maximum max</th>'
    table_html += '</tr>'

    sum = 0
    max = 0
    count = 0
    sid = " "+ sid   # According to given csv file ,course id containd extra space at starting of each value .
    for row in rows:
        if(sid == row[1]):
            count += 1
            sum += int(row[2])
            if(int(row[2]) > int(max)):
                max = row[2]
    if(count > 0):
        avg = float(sum/count)
    else: avg = sum
    table_html += '<tr>'
    table_html += '<td>{}</td>'.format(avg)
    table_html += '<td>{}</td>'.format(max)
    table_html += '</tr>'
    table_html += '</table>'
    data = []
    for row in rows:
        data.append(int(row[2]))
    
    # Create a histogram of the data using matplotlib
    plt.hist(data, bins=100 )
    plt.xlabel("Marks")
    plt.ylabel("Frequency")

    # Save the histogram as a PNG image
    plt.savefig('histogram.png')

    # Save the HTML table to a file
    with open('course.html', 'w') as file:
        file.write("<title>" + "Course Details" + "</title>")
        file.write("<h1>" + "Students Details" + "</h1>")
        file.write(table_html)
        file.write("<img src='histogram.png' alt='Histogram'>")

# Worng inputs
else:
    with open('Worng.html', 'w') as file:
        file.write("<title>" + "Something went worng" + "</title>")
        file.write("<h1>" + "Wrong Inputs" + "</h1>")
        file.write("<p>" + "Something went worng" + "</p>")