import requests

url = "https://iautismo-442024368398.southamerica-east1.run.app/analyze-image"
files = {'image': open('C:\\Users\\dunin\\Desktop\\teste.jpg', 'rb')}
response = requests.post(url, files=files)
print("Status code:", response.status_code)
print("Conteúdo bruto da resposta:")
print(response.text)
