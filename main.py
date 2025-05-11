import requests

name = "Tiya Joshi"
regNo = "REG1325"
email = "tiyajoshi220840@acropolis.in"

generate_url = "https://bfhldevapigw.healthrx.co.in/hiring/generateWebhook/PYTHON"
payload = {
    "name": name,
    "regNo": regNo,
    "email": email
}
response = requests.post(generate_url, json=payload)

res_json = response.json()
access_token = res_json["accessToken"]
webhook_url = res_json["webhook"]

print("Access Token:", access_token)
print("Webhook URL:", webhook_url)

final_sql_query = """
SELECT 
    p.AMOUNT AS SALARY,
    CONCAT(e.FIRST_NAME, ' ', e.LAST_NAME) AS NAME,
    FLOOR(DATEDIFF(CURRENT_DATE, e.DOB) / 365) AS AGE,
    d.DEPARTMENT_NAME
FROM PAYMENTS p
JOIN EMPLOYEE e ON p.EMP_ID = e.EMP_ID
JOIN DEPARTMENT d ON e.DEPARTMENT = d.DEPARTMENT_ID
WHERE DAY(p.PAYMENT_TIME) != 1
ORDER BY p.AMOUNT DESC
LIMIT 1;
"""

headers = {
    "Authorization": access_token,
    "Content-Type": "application/json"
}

submit_payload = {
    "finalQuery": final_sql_query.strip()
}

submit_response = requests.post(webhook_url, headers=headers, json=submit_payload)

print("Submission Status:", submit_response.status_code)
print("Response:", submit_response.text)
