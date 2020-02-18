from bs4 import BeautifulSoup

def findFileTitleDict(path):
	not_filename = ['FARNON', 'SRE']
	file_title_dict = {}
	f = open(path, "r")
	for lines in f:
		#print(lines)
		if lines.startswith("<TR VALIGN=TOP>"):
			soup = BeautifulSoup(lines,'lxml')
			filename = soup.find('a')			
			title = soup.find_all('td')
			if filename.attrs['href'] not in not_filename:
				file_title_dict[filename.attrs['href']] = (title[2].text).strip()
	return file_title_dict

#path = 'C:/Users/PrateekAgarwal/Desktop/Second Semester/Information Retrieval/Assignment 2/stories/stories/SRE/index.html'
'''path = 'C:/Users/PrateekAgarwal/Desktop/Second Semester/Information Retrieval/Assignment 2/stories/stories/index.html'
file_title_dict = findFileTitleDict(path)
print("file_title_dict:",file_title_dict)'''