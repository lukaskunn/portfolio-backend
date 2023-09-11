from django.contrib import admin
from content.models import Content, Landing, SectSubtitle, About, AboutContent, AboutContentTexts, Services, ServicesSkills, Works, Project, Contact, ContactCard, ResumeCard, Resume


class SectSubtitleAdmin(admin.ModelAdmin):
    fields = ["landing", "value"]
    
class LandingAdmin(admin.ModelAdmin):
    fields = ["content", "sect_title"]

class ContentAdmin(admin.ModelAdmin):
    fields = ["lang_code"] 

class AboutAdmin(admin.ModelAdmin):
    fields = ["content", "header_title", "sect_title"]

class AboutContentAdmin(admin.ModelAdmin):
    fields = ["about_sect", "text"]
    
class AboutContentTextsAdmin(admin.ModelAdmin):
    fields = ["about_content_texts", "text"]
    
class ResumeAdmin(admin.ModelAdmin):
    fields = ["content", "sect_title", "header_title"]
    
class ResumeCardAdmin(admin.ModelAdmin):
    fields = ["resume", "job_title", "company", "description", "start_date", "end_date"]
    
class ServicesAdmin(admin.ModelAdmin):
    fields = ["content", "sect_title", "header_title"]
class ServicesSkillsAdmin(admin.ModelAdmin):
    fields = ["service", "title", "subtitle", "type", "typeSoftHard"]
    
class WorksAdmin(admin.ModelAdmin):
    fields = ["content", "sect_title", "header_title", "see_more_text", "personal_project_title", "background_project_title"]
    
class ProjectAdmin(admin.ModelAdmin):
    fields = ["projects", "project_title", "description", "background_image", "url_to_project", 'type']

class ContactAdmin(admin.ModelAdmin):
    fields = ["content", "title", "header_title"]
class ContactCardAdmin(admin.ModelAdmin):
    fields = ["contact", "type", "link_text", "url_link"]
    
admin.site.register(Content, ContentAdmin)
admin.site.register(Landing, LandingAdmin)
admin.site.register(SectSubtitle, SectSubtitleAdmin)
admin.site.register(About, AboutAdmin)
admin.site.register(AboutContent, AboutContentAdmin)
admin.site.register(AboutContentTexts, AboutContentTextsAdmin)
admin.site.register(Resume, ResumeAdmin)
admin.site.register(ResumeCard, ResumeCardAdmin)
admin.site.register(Services, ServicesAdmin)
admin.site.register(ServicesSkills, ServicesSkillsAdmin)
admin.site.register(Works, WorksAdmin)
admin.site.register(Project, ProjectAdmin)
admin.site.register(ContactCard, ContactCardAdmin)
admin.site.register(Contact, ContactAdmin)
