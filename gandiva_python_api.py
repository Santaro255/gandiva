import requests
import json

#params
gandiva_user = "domain\\user" #changeme
gandiva_pass = "password" #changeme
gandiva_api_url = "https://api-address/" #changeme

#get token
def gandiva_get_token():
    headers = { 'Content-Type': 'x-www-form-urlencoded' }
    data = {
        'grant_type': 'password',
        'username': gandiva_user,
        'password': gandiva_pass
        }
    response = requests.post(gandiva_api_url + "Token", data=data, headers=headers)
    return response.json()['access_token']

#assign token
gandiva_api_key = gandiva_get_token()
#token header for API requests #requests.*(, headers=token)
token = {
    'Content-Type': 'application/json',
    'Authorization': 'Bearer '+ gandiva_api_key
    }

#get all departments
def gandiva_get_departments():
    response = requests.get(gandiva_api_url + "api/workNormative/departments", headers=token)
    return response.json()

#get all catigories for department by id
def gandiva_get_categories(department_id):
    response = requests.get(gandiva_api_url + "api/workNormative/departments/" + str(department_id) + "/categories", headers=token)
    return response.json()

#get all types for category by id
def gandiva_get_types(category_id):
    response = requests.get(gandiva_api_url + "api/workNormative/categories/" + str(category_id) + "/requestTypes", headers=token)
    return response.json()

#get all job types for type by id
def gandiva_get_job_types(type_id):
    response = requests.get(gandiva_api_url + "api/workNormative/requestTypes/" + str(type_id) + "/jobTypes", headers=token)
    return response.json()

#get request by id
def gandiva_get_request_by_id(request_id):
    response = requests.get(gandiva_api_url + "api/Requests/" + str(request_id), headers = token)
    return response.json()

#print all unclosed requests for gandiva_user
def gandiva_print_my_unclosed_requests():
    request_status_list = {
        '0': 'Отсутствует',
        '1': 'Новый',
        '2': 'На рассмотрении',
        '3': 'На согласовании',
        '4': 'На уточнении',
        '5': 'Отклонена',
        '6': 'В работе',
        '7': 'Отменено',
        '8': 'Проверка выполнения',
        '9': 'Закрыта',
        '10': 'Ожидает',
        '11': 'Ожидает предшественника',
        '12': 'Ожидает публикации плана',
        '13': 'На уточнении у исполнителя'
        }
    response = requests.get(gandiva_api_url + "api/Requests?type=my&page=1&size=100&sort=id", headers=token)#, verify=False)
    print('Total: ' + str(response.json()['Total']) + "\n")
    for i in response.json()['Requests']:
        if i['Status'] != 9:
            req_id = i['Id']
            req_status = request_status_list[str(i['Status'])]
            initiator_first_name = i['Initiator']['FirstName']
            initiator_last_name = i['Initiator']['LastName']
            req_create_date = i['CreateDate']
            contractor_first_name = i['Contractor']['FirstName']
            contractor_last_name = i['Contractor']['LastName']
            req_department = i['Department']['Name']
            req_category = i['Category']['Name']
            req_type = i['RequestType']['Name']
            req_job_type = i['JobType']['Name']
            req_desc = i['Description']   
            print('Id: ' + str(req_id))
            print('Статус заявки: ' + str(req_status))
            print('Инициатор: ' + initiator_last_name + " " + initiator_first_name)
            print('Дата: ' + req_create_date)
            print('Испольнитель: ' + contractor_last_name + " " + contractor_first_name)
            print('Отдел: ' + req_department)
            print('Категория: ' + req_category)
            print('Тип: ' + req_type)
            print('Вид: ' + req_job_type)
            print('Описание: ' + req_desc)
            print("###")

#print all requests for gandiva_user
def gandiva_print_all_my_requests():
    request_status_list = {
        '0': 'Отсутствует',
        '1': 'Новый',
        '2': 'На рассмотрении',
        '3': 'На согласовании',
        '4': 'На уточнении',
        '5': 'Отклонена',
        '6': 'В работе',
        '7': 'Отменено',
        '8': 'Проверка выполнения',
        '9': 'Закрыта',
        '10': 'Ожидает',
        '11': 'Ожидает предшественника',
        '12': 'Ожидает публикации плана',
        '13': 'На уточнении у исполнителя'
        }
    response = requests.get(gandiva_api_url + "api/Requests?type=my&page=1&size=100&sort=id", headers=token)#, verify=False)
    print('Total: ' + str(response.json()['Total']) + "\n")
    for i in response.json()['Requests']:
        req_id = i['Id']
        req_status = request_status_list[str(i['Status'])]
        initiator_first_name = i['Initiator']['FirstName']
        initiator_last_name = i['Initiator']['LastName']
        req_create_date = i['CreateDate']
        contractor_first_name = i['Contractor']['FirstName']
        contractor_last_name = i['Contractor']['LastName']
        req_department = i['Department']['Name']
        req_category = i['Category']['Name']
        req_type = i['RequestType']['Name']
        req_job_type = i['JobType']['Name']
        req_desc = i['Description']   
        print('Id: ' + str(req_id))
        print('Статус заявки: ' + str(req_status))
        print('Инициатор: ' + initiator_last_name + " " + initiator_first_name)
        print('Дата: ' + req_create_date)
        print('Испольнитель: ' + contractor_last_name + " " + contractor_first_name)
        print('Отдел: ' + req_department)
        print('Категория: ' + req_category)
        print('Тип: ' + req_type)
        print('Вид: ' + req_job_type)
        print('Описание: ' + req_desc)
        print("###")
