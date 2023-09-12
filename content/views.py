from django.http import JsonResponse
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from content.models import Content
from users.models import CustomUser



# Create your views here.
class GetContent(APIView):
    def get(self, request):
        api_key = request.headers.get("api-key")
        api_secret = request.headers.get("api-secret")
        
        print(api_key)
        print(api_secret)

        try:
            user = CustomUser.objects.get(api_key=api_key)
            print(user.api_key)
            print(user.has_valid_api_secret(api_secret))
        except:
            print("nao")
            return Response(status=status.HTTP_404_NOT_FOUND)

        if user:
            if user.api_key == api_key and user.has_valid_api_secret(api_secret):
                
                allContent = Content.objects.all()
                language = {}
                
                for index, content in enumerate(allContent):
                    language[content.lang_code] = {}
                    language[content.lang_code]["landing"] = {"sectionTitle": content.landing.sect_title, "subtitle": []}
                    
                    language[content.lang_code]["aboutMe"] = {"sectionTitle": content.about.sect_title, "headerTitle": content.about.header_title, "content": []}
                    
                    language[content.lang_code]["resume"] = {"sectionTitle": content.resume.sect_title,"headerTitle": content.resume.header_title, "cards": []}
                    
                    language[content.lang_code]["services"] = {"sectionTitle": content.services.sect_title,"headerTitle": content.services.header_title, "skills": {"soft": {"desktop": [], "mobile": []}, "hard": {"desktop": [], "mobile": []}}}
                    
                    language[content.lang_code]["works"] = {"sectionTitle": content.works.sect_title,"headerTitle": content.works.header_title, "seeMoreText": content.works.see_more_text, "personalProjects": {"title": content.works.personal_project_title, "projects": []}, "backgroundProjects": {"title": content.works.background_project_title, "projects": []}}
                    
                    language[content.lang_code]["contact"] = {"sectionTitle": content.contact.title,"headerTitle": content.contact.header_title, "contacts": []}
                    
                    for subtitles in content.landing.sect_subtitle.all():
                        language[content.lang_code]["landing"]["subtitle"].append(subtitles.value)
                    
                    for about_contents in content.about.about_sect.all():
                        texts = []
                        for about_content_texts in about_contents.about_content_texts.all():
                            texts.append(about_content_texts.text)
                        language[content.lang_code]["aboutMe"]["content"].append({"title": about_contents.text, "text": texts})
                        
                    for card in content.resume.resume_cards.all():
                        language[content.lang_code]["resume"]["cards"].append({"jobTitle": card.job_title, "company": card.company, "startDate": card.start_date, "endDate": card.end_date, "description": card.description})
                    
                    for skillsSoftDesktop in content.services.service_skills.filter(type="Desktop", typeSoftHard="Soft"):
                        language[content.lang_code]["services"]["skills"]["soft"]["desktop"].append({"title": skillsSoftDesktop.title, "subtitle": skillsSoftDesktop.subtitle})
                        
                    for skillsSoftMobile in content.services.service_skills.filter(type="Mobile", typeSoftHard="Soft"):
                        language[content.lang_code]["services"]["skills"]["soft"]["mobile"].append({"title": skillsSoftMobile.title})
                        
                        
                    for skillsHardDesktop in content.services.service_skills.filter(type="Desktop", typeSoftHard="Hard"):
                        language[content.lang_code]["services"]["skills"]["hard"]["desktop"].append({"title": skillsHardDesktop.title, "subtitle": skillsHardDesktop.subtitle})
                        
                        
                    for skillsHardMobile in content.services.service_skills.filter(type="Mobile", typeSoftHard="Hard"):
                        language[content.lang_code]["services"]["skills"]["hard"]["mobile"].append({"title": skillsHardMobile.title})
                    
                    for personalProjects in content.works.projects.filter(type="Personal"):
                        language[content.lang_code]["works"]["personalProjects"]["projects"].append({"projectTitle": personalProjects.project_title, "description": personalProjects.description,"background":  personalProjects.background_image, "urlToProject": personalProjects.url_to_project, "tags": []})
                        
                    for backgroundProjects in content.works.projects.filter(type="Background"):
                        language[content.lang_code]["works"]["backgroundProjects"]["projects"].append({"projectTitle": backgroundProjects.project_title, "description": backgroundProjects.description,"background":  backgroundProjects.background_image, "urlToProject": backgroundProjects.url_to_project, "tags": []})
                        
                    for contact in content.contact.contacts.all():
                        language[content.lang_code]["contact"]["contacts"].append({"type": contact.type, "linkText": contact.link_text, "urlLink": contact.url_link})
                print("entra aqui")

                data_response = JsonResponse(language, safe=False, json_dumps_params={'ensure_ascii': False})
                
                data_response["Access-Control-Allow-Origin"] = "*"
                data_response["Access-Control-Allow-Methods"] = "GET, OPTIONS"
                data_response["Access-Control-Max-Age"] = "1000"
                data_response["Access-Control-Allow-Headers"] = "api-secret"
                
                print(data_response)
                
                return data_response
                # return Response(data=language, status=status.HTTP_200_OK)
            return Response(data={"valid": False}, status=status.HTTP_200_OK)
