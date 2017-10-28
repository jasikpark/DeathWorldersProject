import requests

# implement input arguments later. for now, i'll just hardcode the file.

f = open('deathworlders-url-list-2.csv','r')

urls = f.readlines()

fixed_urls = [x.strip('\r\n') for x in urls]

first_url = """http://markdownplease.com/?url="""

for i,x in enumerate(fixed_urls):
    r = requests.get(first_url + x)
    print r.url + "\n"
    name = x.rsplit('/', 1)[-1].strip()
    filename = str(i+100) + "_" + name + ".md"
    print "writing to " + filename + "\n"
    f = open(filename,'w')
    f.write(r.content)

print "All webpages have been downloaded and stored as markdown files!"
