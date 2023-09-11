from django.db import models
import uuid
# Create your models here.

class Content(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    lang_code = models.CharField(max_length=2, null=True, blank=True)
    def __str__(self):
        return self.lang_code.upper()
    
class Landing(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    content = models.OneToOneField(to=Content, on_delete=models.SET_NULL, null=True, related_name="landing")
    sect_title = models.CharField(max_length=100, null=False, blank=False)
    
    def __str__(self):
        return f"{self.content.lang_code.upper()} - {self.sect_title}"

class SectSubtitle(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    landing = models.ForeignKey(to=Landing, on_delete=models.SET_NULL, related_name="sect_subtitle", null=True)
    value = models.CharField(max_length=50, null=False, blank=False)
    
    def __str__(self):
        return f"{self.landing.content.lang_code.upper()} - {self.value}"
    
    
class About(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    content = models.OneToOneField(to=Content, on_delete=models.SET_NULL, null=True, related_name="about")
    header_title = models.CharField(max_length=100, null=False, blank=False)
    sect_title = models.CharField(max_length=100, null=False, blank=False)
    
    def __str__(self):
        return f"{self.content.lang_code.upper()} - {f'{self.sect_title[0:25]}...' if len(self.sect_title) > 20 else self.sect_title}"

class AboutContent(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    about_sect = models.ForeignKey(to=About, on_delete=models.SET_NULL, related_name="about_sect", null=True)
    text = models.CharField(max_length=500, null=False, blank=False)
    def __str__(self):
        return f"{self.about_sect.content.lang_code.upper()} - {f'{self.text[0:25]}...' if len(self.text) > 20 else self.text}"


class AboutContentTexts(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    about_content_texts = models.ForeignKey(to=AboutContent, on_delete=models.SET_NULL, related_name="about_content_texts", null=True)
    text = models.CharField(max_length=1000,null=False, blank=False)
    def __str__(self):
        return f"{self.about_content_texts.about_sect.content.lang_code.upper()} - {f'{self.text[0:25]}...' if len(self.text) > 20 else self.text}"

class Resume(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    content = models.OneToOneField(to=Content, on_delete=models.SET_NULL, null=True, related_name="resume")
    sect_title = models.CharField(max_length=100,null=False, blank=False)
    header_title = models.CharField(max_length=20, null=False, blank=False)
    def __str__(self):
        return f"{self.content.lang_code.upper()} - {self.sect_title}"

class ResumeCard(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    resume = models.ForeignKey(to=Resume, on_delete=models.SET_NULL, related_name="resume_cards", null=True)
    job_title = models.CharField(max_length=100, null=False, blank=False)     
    company = models.CharField(max_length=100, null=False, blank=False)
    description = models.CharField(max_length=1000, null=False, blank=False)
    start_date = models.CharField(max_length=20, null=False, blank=False)
    end_date = models.CharField(max_length=20, null=False, blank=False)
    def __str__(self):
        return f"{self.resume.content.lang_code.upper()} - {f'{self.job_title[0:25]}...' if len(self.job_title) > 20 else self.job_title}"

class Services(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    content = models.OneToOneField(to=Content, on_delete=models.SET_NULL, null=True, related_name="services")
    sect_title = models.CharField(max_length=100,null=False, blank=False)
    header_title = models.CharField(max_length=20, null=False, blank=False)
    def __str__(self):
        return f"{self.content.lang_code.upper()} - {self.sect_title}"

class ServicesSkills(models.Model):
    OPTIONS_TYPE = [
        ("Desktop", "Desktop"),
        ("Mobile", "Mobile")
    ]
    OPTIONS_TYPE_SOFT_HARD = [
        ("Soft", "Soft"),
        ("Hard", "Hard")
    ]
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    service = models.ForeignKey(to=Services, on_delete=models.SET_NULL, related_name="service_skills", null=True)
    title = models.CharField(max_length=50, null=False, blank=False, default="_")
    subtitle = models.CharField(max_length=100, null=True, blank=True)
    type = models.CharField(max_length=7,null=False, blank=False, default="Desktop", choices=OPTIONS_TYPE)
    typeSoftHard = models.CharField(max_length=7,null=False, blank=False, default="Soft", choices=OPTIONS_TYPE_SOFT_HARD)
    
    def __str__(self):
        return f"{self.service.content.lang_code.upper()} - {f'{self.title[0:25]}...' if len(self.title) > 20 else self.title}"
    
class Works(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    content = models.OneToOneField(to=Content, on_delete=models.SET_NULL, null=True, related_name="works")
    sect_title = models.CharField(max_length=100,null=False, blank=False)
    header_title = models.CharField(max_length=20, null=False, blank=False)
    see_more_text = models.CharField(max_length=20, null=False, blank=False)
    personal_project_title = models.CharField(max_length=100,null=False, blank=False, default="Personal Projects.")
    background_project_title = models.CharField(max_length=100,null=False, blank=False, default="Background Projects.")
    def __str__(self):
        return f"{self.content.lang_code.upper()} - {self.sect_title}"

class Project(models.Model):
    OPTION_TYPE = [
        ("Personal", "Personal"),
        ("Background", "Background")
    ]
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    projects = models.ForeignKey(to=Works, on_delete=models.SET_NULL, related_name="projects", null=True)
    project_title = models.CharField(max_length=100,null=False, blank=False)
    description = models.CharField(max_length=1000,null=False, blank=False)    
    background_image = models.CharField(max_length=100,null=False, blank=False)
    url_to_project = models.CharField(max_length=100,null=False, blank=False)
    type = models.CharField(max_length=10,null=False, blank=False, default="Background", choices=OPTION_TYPE)
    def __str__(self):
        return f"{self.projects.content.lang_code.upper()} - {f'{self.project_title[0:25]}...' if len(self.project_title) > 20 else self.project_title}"
    
class Contact(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    content = models.OneToOneField(to=Content, on_delete=models.SET_NULL, null=True, related_name="contact")
    title = models.CharField(max_length=100,null=False, blank=False)
    header_title = models.CharField(max_length=20, null=False, blank=False)
    def __str__(self):
        return f"{self.content.lang_code.upper()} - {self.title}"
    
class ContactCard(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    contact = models.ForeignKey(to=Contact, on_delete=models.SET_NULL, related_name="contacts", null=True)
    type = models.CharField(max_length=20,null=False, blank=False)
    link_text = models.CharField(max_length=100,null=False, blank=False)
    url_link = models.CharField(max_length=200, null=False, blank=False)
    def __str__(self):
        return f"{self.contact.content.lang_code.upper()} - {f'{self.link_text[0:25]}...' if len(self.link_text) > 20 else self.link_text}"

    
