import requests

with open('userID.txt', 'r') as f:
	idList = f.read().splitlines()

for userId in idList:
	data = {"userID":userId}
	response = requests.post("http://123.45.67.123/check.php", data=data)
	
	resultForm = "[Scan] {} : {}\n"
	resStat = ""
	
	responseText = response.text
	
	if 'Not Possible' in responseText:
		resStat= "Not Possible"
	else:
		resStat = "Possible"
		
	with open('idscan_res.txt', 'a') as f: # 파일 만들고 데이터 삽입
		f.write(resultForm.format(userId, resStat))