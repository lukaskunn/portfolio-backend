from django.http import JsonResponse
from content.models import Content, Landing, SectSubtitle

# Create your views here.
def getContent(request):
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

    response = JsonResponse(language, safe=False, json_dumps_params={'ensure_ascii': False})
    
    response["Access-Control-Allow-Origin"] = "*"
    response["Access-Control-Allow-Methods"] = "GET, OPTIONS"
    response["Access-Control-Max-Age"] = "1000"
    response["Access-Control-Allow-Headers"] = "X-Requested-With, Content-Type"
    
    return response

def saveNewContent(request):
    content = Content.objects.create(lang_code="en")
    landing = Landing.objects.create(content=content, sect_title="Lucas Oliveira")
    subtitle1 = SectSubtitle.objects.create(value="daora 1", landing=landing)
    subtitle2 = SectSubtitle.objects.create(value="daora 2", landing=landing)
    subtitle3 = SectSubtitle.objects.create(value="daora 3", landing=landing)
    
    subtitle1.save()
    subtitle2.save()
    subtitle3.save()