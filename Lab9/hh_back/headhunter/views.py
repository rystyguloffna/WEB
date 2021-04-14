from django.shortcuts import render

# Create your views here.
from .models import Company,Vacancy
from django.http import JsonResponse,HttpResponse

# Create your views here

def show_companies(request):
    companies = list(Company.objects.values())
    return JsonResponse(companies,safe=False)

def show_company(request,company_id):
    try:
        company = list(Company.objects.filter(id=company_id).values())
        return JsonResponse(company,safe=False)
    except:
        return HttpResponse("NOT FOUND")

def show_vacancies(request):
    vacancies = list(Vacancy.objects.values())
    return JsonResponse(vacancies,safe=False)

def show_vacancy(request,vacancy_id):
    try:
        vacancy = list(Vacancy.objects.filter(id=vacancy_id).values())
        return JsonResponse(vacancy,safe=False)
    except:
        return HttpResponse("NOT FOUND")

def show_topten(request):
    vacancies = Vacancy.objects.order_by('-salary')[:10]
    vacancies_json = [vacancy.to_json() for vacancy in vacancies]
    return JsonResponse(vacancies_json, safe=False)

def companies_vacancies(request, company_id):
    vacancies = Vacancy.objects.filter(company=company_id)
    vacancies_json = [vacancy.to_json() for vacancy in vacancies]
    return JsonResponse(vacancies_json, safe=False)