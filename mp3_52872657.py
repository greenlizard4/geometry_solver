import pymysql
import cgi
import datetime

#made a change


db = pymysql.connect(host='localhost',
user='gallery',
passwd='eecs118',
db= 'gallery')
cur = db.cursor()
hashlink = 'https://i.ytimg.com/vi/juoJ9G9MNHA/maxresdefault.jpg'

# mini project 3
# Galleries page
print("Content-Type: text/html")
print()
print("<H1>The Galleries Page</H1>")
x = datetime.datetime.now()
if int(x.strftime("%I")) < 12:
    print("<H3>Good Morning!</H3>")
if int(x.strftime("%I")) >= 12 and int(x.strftime("%I")) <= 17:
    print("<H3>Good Afternoon!</H3>")
if int(x.strftime("%I")) >= 17:
    print("<H3>Good Evening!</H3>")

print("<head><style>")
#style of page
print("div.gallery {margin: 5px; border: 1px solid #ccc; float: left; width: 180px; background-color: blue;}")
print("div.gallery:hover {border: 1px solid #777;}")
print("div.galleryName {padding: 5px; text-align: center;}")
print("div.desc {padding: 5px; text-align: center;}")
print("body {background-color: lightblue;}")
print("select {width:7%; border-radius: 4px; background-color: #f1f1f1;}")
print("</style></head>")

print("<body>")
#search bar
print("<form action = 'searchPage.py'>")
print("<label for='search_option'>Search Image by:</label>" )
print("<select id='search_option' name='search_option'>")
print("<option value='type'>Image Type</option>")
print("<option value='year'>Image Year</option>")
print("<option value='artist_name'>Artist Name</option>")
print("<option value='location'>Location</option>")
print("<input type='text' id='search_query' name='search_query'>")
print("<input type = 'submit' value = 'Search Image' />")
print("</form>")
print("<form action = 'searchPage.py'>")
print("<label for='search_option'>OR Search Artist by:</label>" )
print("<select id='search_option' name='search_option'>")
print("<option value='country'>Artist Country</option>")
print("<option value='birth_year'>Birth Year</option>")
print("<input type='text' id='search_query' name='search_query'>")
print("<input type = 'submit' value = 'Search Artist' />")
print("</form>")
#list of galleries
sql="SELECT * FROM gallery.gallery;"
cur.execute(sql)
for row in cur.fetchall():
    gallery_id = row[0]
    name = row[1]
    description = row[2]
    print("<div class='gallery'>")
    print("""<div class='galleryName'>%s</div>""" %name)
    print("""<div class='desc'>%s</div>""" %description)
    print("<form id = 'gallery_items' action = 'imagePage.py' method = 'get'>")
    print("""<input type = 'hidden' name='gallery_id' value=%s />"""%gallery_id)
    print("<input type = 'submit' value = 'Go to gallery' />")
    print("</form>")
    print("</div>")


#adding a new gallery
print("<div class='gallery'>")
print("<div class='name'>Add a new gallery</div>")
print("<form action='addNewGallery.py'>")
print("<label for='galleryName'>Gallery Name</label><br />" )
print("<input type='text' id='galleryName' name='galleryName'>")
print("<label for='desc'>Gallery description</label><br />" )
print("<input type='text' id='desc' name='desc'>")
print("<input type = 'submit' value = 'Submit' />")
print("</form>")
print("</div>")

#adding a new artist
print("<div class='gallery'>")
print("<div class='name'>Add a new artist</div>")
print("<form action='addNewArtist.py'>")
print("<label for='artist_name'>Artist Name</label><br />" )
print("<input type='text' id='artist_name' name='artist_name'>")
print("<label for='birth_year'>Birth Year</label><br />" )
print("<input type='text' id='birth_year' name='birth_year'>")
print("<label for='country'>Country</label><br />" )
print("<input type='text' id='country' name='country'>")
print("<label for='desc'>Artist Description</label><br />" )
print("<input type='text' id='desc' name='desc'>")
print("<input type = 'submit' value = 'Submit' />")
print("</form>")
print("</div>")


print("</body> </html>")
