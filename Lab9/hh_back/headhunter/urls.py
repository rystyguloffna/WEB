from django.contrib import admin
from django.urls import path
from headhunter import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('companies',views.show_companies),
    path('company/<int:company_id>',views.show_company),
    path('vacancies',views.show_vacancies),
    path('vacancy/<int:vacancy_id>',views.show_vacancy),
    path('vacanies/top_ten',views.show_topten),
    path('company/<int:company_id>/vacancies',views.companies_vacancies),
]
