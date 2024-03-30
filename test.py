import requests

cookies = {
    'ci_session': 'cmo6t4an0atmi1f37u2o213jpgqk9ojs',
    'csrf_cookie_cmsdatagoe': '18b92352f789f706319f15f191a9e268',
}

headers = {
    'Accept': 'application/json, text/javascript, */*; q=0.01',
    'Accept-Language': 'en-US,en;q=0.9,id-ID;q=0.8,id;q=0.7',
    'Connection': 'keep-alive',
    'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
    # 'Cookie': 'ci_session=cmo6t4an0atmi1f37u2o213jpgqk9ojs; csrf_cookie_cmsdatagoe=18b92352f789f706319f15f191a9e268',
    'Origin': 'https://new-portal.serdangbedagaikab.go.id',
    'Referer': 'https://new-portal.serdangbedagaikab.go.id/',
    'Sec-Fetch-Dest': 'empty',
    'Sec-Fetch-Mode': 'cors',
    'Sec-Fetch-Site': 'same-origin',
    'User-Agent': 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Mobile Safari/537.36',
    'X-Requested-With': 'XMLHttpRequest',
    'sec-ch-ua': '"Google Chrome";v="123", "Not:A-Brand";v="8", "Chromium";v="123"',
    'sec-ch-ua-mobile': '?1',
    'sec-ch-ua-platform': '"Android"',
}

data = {
    'csrf_tokencmsdatagoe': '18b92352f789f706319f15f191a9e268',
    'nama': 'test',
    'nohp': 'test',
    'jawaban_id[1]': '1',
    'jawaban_id[2]': '2',
    'jawaban_id[3]': '5',
    'jawaban_id[4]': '1',
    'jawaban_id[5]': '1',
    'jawaban_id[6]': '5',
    'jawaban_id[7]': '1',
    'jawaban_id[8]': '1',
    'jawaban_id[9]': '5',
    'totalnil': '12',
    'survey_id': '1',
    'saran': 'test',
}

response = requests.post(
    'https://new-portal.serdangbedagaikab.go.id/survey/isisurvei',
    cookies=cookies,
    headers=headers,
    data=data,
)

print(response.text)