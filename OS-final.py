import os
import requests
from hashlib import md5
import uuid


photoName = []
photoHash = []

def hshCode(photo):
	with open(photo, "rb") as p:
		 photoHash = md5(p.read()).hexdigest()
	return photoHash
	

def dltDuplicates():
	duplicates = []
	index = 0
	
	for i in photoHash:
		if i not in duplicates:
			duplicates.append(i)
		else:
			name = photoName[index]
			path = os.path.join(os.getcwd(), name)
			os.remove(path)
		index = index +1
	print("Duplicates are deleted...")
		
def childProcess():
	child = os.fork()
	if(child>0):
		print("Parent process is ", os.getpid())
		os.wait()
	
	else:
		print("Child process is ", os.getpid())

def downloadFile(url, file_name = None):
	r = requests.get(url, allow_redirects= True)
	file = file_name if file_name else str(uuid.uuid4())
	open(file, 'wb').write(r.content)
	
	photoName.append(file)
	photoHash.append(hshCode(file))

	
	
		
def downloadUrl():
	child = os.fork()
	if(child>0):
		print("Parent process is ", os.getpid())
		os.wait()
	
	elif(child==0):
		print("Child process is ", os.getpid())

		url = ["http://wiki.netseclab.mu.edu.tr/images/thumb/f/f7/MSKU-BlockchainResearchGroup.jpeg/300px-MSKU-BlockchainResearchGroup.jpeg", "https://upload.wikimedia.org/wikipedia/tr/9/98/Mu%C4%9Fla_S%C4%B1tk%C4%B1_Ko%C3%A7man_%C3%9Cniversitesi_logo.png", "https://upload.wikimedia.org/wikipedia/commons/thumb/c/c3/Hawai%27i.jpg/1024px-Hawai%27i.jpg", "http://wiki.netseclab.mu.edu.tr/images/thumb/f/f7/MSKU-BlockchainResearchGroup.jpeg/300px-MSKU-BlockchainResearchGroup.jpeg", "https://upload.wikimedia.org/wikipedia/commons/thumb/c/c3/Hawai%27i.jpg/1024px-Hawai%27i.jpg" ]
		
		

		for i in url:
			downloadFile(i) 
			
		print("All files are downloaded...")
		print(photoName)
		dltDuplicates()
	

		


if __name__ == "__main__":
	
	downloadUrl()
	
		



	





	


