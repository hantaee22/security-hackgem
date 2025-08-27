import requests

with open('userID.txt', 'r') as f: # userID파일은 이미 만들어둔것
	idList = f.read().splitlines()
	
#print(IdList)

for userid in idList:
	data = {"userID":userId}
	requests.post("http://3131.31/check.oho", data=data)
	
	resultForm = "{} : {}\n"
	resStat= ""
	
	responseText = response.text
	
	if 'Not possible' in responseText:
		resStat = "not Possible"
	else:
		resStat = "Possible"
	
	with open('scan_Res', 'a') as f:
		f.write(resultForm.format(userId, resStat))