#First run this command: ssh -L 9999:<IP of your instance>:80 username@remote-ip
#This will tunnel localhost:9999 through the remote machine to <IP of you instance>
#Create another terminal and run the python script below locally

import requests
import json
import pandas as pd
from pandasql import sqldf

BASE_URL = "http://localhost:9999/query"
JWT = "<JWT>"  # replace this with your actual JWT
HEADERS = {
    "Authorization": JWT,
    "Content-type": "application/json"
}

#Run Query through PrivateSQL instance
def run_query(sql_query):
    payload = {
        "database_name": "postgres",
        "project": "project-psql",
        "query": sql_query
    }

    response = requests.get(BASE_URL, headers=HEADERS, data=json.dumps(payload))

    print("Status Code:", response.status_code)
    try:
        print("Response JSON:", response.json())
    except Exception as e:
        print("Non-JSON Response:", response.text)

#Ground Truth
medical_insurance = pd.read_csv('insurance.csv')
pysql = lambda q: sqldf(q, globals())

def run_queries(queries):
  for query in queries:
    print("##Private SQL##")
    run_query(query)
    print("##Ground Truth##")
    print(pysql(query))



if __name__ == "__main__":
    # print("----Safe Aggregates----")
    # safe_aggregates = ["SELECT sex, COUNT(*) FROM medical_insurance GROUP BY sex",
    #                    "SELECT smoker, COUNT(*) FROM medical_insurance GROUP BY smoker",
    #                    "SELECT region, COUNT(*) FROM medical_insurance GROUP BY region"]
    # run_queries(safe_aggregates)
    # print("----Safe Averages----")
    # safe_averages = ["SELECT AVG(age) FROM medical_insurance",
    #                  "SELECT region, AVG(charges) FROM medical_insurance GROUP BY region",
    #                  "SELECT smoker, AVG(bmi) FROM medical_insurance GROUP BY smoker"]
    # run_queries(safe_averages)
    # print("----Self Enforcement ----")
    # self_enforcement = ["SELECT charges FROM medical_insurance WHERE sex = 'female' AND age = 64 AND bmi > 40",
    #                     "SELECT * FROM medical_insurance WHERE age = 19 AND sex = 'female' AND bmi = 27.9 AND children = 0 AND smoker = 'yes' AND region = 'southwest'"]
    # run_queries(self_enforcement)
    # print("----Complex Aggregates----")
    # complex_aggregates = ["SELECT age, COUNT(*) FROM medical_insurance GROUP BY age",
    #                       "SELECT bmi, COUNT(*) FROM medical_insurance GROUP BY bmi"]
    # run_queries(complex_aggregates)
    # print("----Difference Attack----")
    # difference_attack = ["SELECT COUNT(*) FROM medical_insurance WHERE smoker = 'yes'",
    #                      "SELECT COUNT(*) FROM medical_insurance WHERE smoker = 'yes' AND sex = 'female'"]
    # run_queries(difference_attack)
    print("----Single Out Query----")
    single_out = ["SELECT charges FROM medical_insurance ORDER BY charges DESC LIMIT 1"]
    run_queries(single_out)
    # noise_check = ["SELECT COUNT(*) FROM medical_insurance WHERE smoker='yes'"]
    #Consistency Tests
    # for _ in range(10):
    #   run_queries(noise_check)
