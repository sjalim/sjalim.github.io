from django.shortcuts import render, HttpResponse
from .models import ProjectSection, TodoItem, EducationItem, AchievementItem, Section, Categories, Skills, JobExperienceItem, Project
# Create your views here.
import logging
import json
logger = logging.getLogger(__name__)

def home(request):
    return render(request, "home.html")

def education(request):
    educationItems = EducationItem.objects.all()
    achievementItems = AchievementItem.objects.all()

    return render(request, "education.html", {"educationItems": educationItems, "achievementItems": achievementItems})

def skill(request):
    sections = Section.objects.all()
    categories = Categories.objects.all()

    skills_data = []
    logger.debug('Something happened')
    for section in sections:
        section_dict = {
            'section': section.name,
            'categories': []
        }

        for category in section.categories.all():
            category_dict = {
                'name': category.name,
                'skills': []
            }

            for skill in category.skills.all():
                skill_dict = {
                    'name': skill.name,
                    'icon': skill.icon.url if skill.icon else None,
                    'active': skill.active
                }
                category_dict['skills'].append(skill_dict)

            section_dict['categories'].append(category_dict)

        skills_data.append(section_dict)

    return render(request, "skill.html", {'skills_data': skills_data})

def achievement(request):
    return render(request, "achievement.html")

def job_experience(request):

    positions = JobExperienceItem.objects.all()

    # print(positions)
    

    # positions = [   
    #     {
    #         'title': 'Software Engineer',
    #         'company': 'Tech Company',
    #         'company_link': 'https://www.techcompany.com',
    #         'department': 'Engineering',
    #         'duration': 'Jan 2020 - Present',
    #         'description': 'Developed and maintained web applications using Django and React.'
    #     },
    #     {
    #         'title': 'Data Analyst',
    #         'company': 'Data Company',
    #         'location': 'City, Country',
    #         'duration': 'Jan 2019 - Dec 2019',
    #         'description': 'Analyzed data using Python and SQL to provide insights for business decisions.'
    #     },
    #     {
    #         'title': 'Intern',
    #         'company': 'Internship Company',
    #         'location': 'City, Country',
    #         'duration': 'Jun 2018 - Aug 2018',
    #         'description': 'Assisted in software development projects and learned about Agile methodologies.'
    #     }

    # ]
    return render(request, "job_experience.html", {'positions': positions})

def project(request):

    grouped_projects = []

    sections = ProjectSection.objects.filter(active=True)

    for section in sections:
        projects = Project.objects.filter(section=section)
        if projects.exists():
            grouped_projects.append({
                'section': section,
                'projects': projects
            })

    return render(request, "project.html", {'projectItems': grouped_projects})
  
 
  
    # projectItems = [
    #     {
    #         "section": "Data Science",
    #         "projects": [
    #             {
    #                 "name": "check",
    #                 "image": "saruar.jpg",
    #                 "description": "check check check check check check check check",
    #                 "tags": [
    #                     "Swift", "SwiftUI", "iOS Deveploment"
    #                 ],
    #                 "link": "https://placehold.co/600x400"
    #             },
               
    #         ]
    #     },
    #     {
    #         "section": "App Development",
    #         "projects": [
    #             {
    #                 "name": "check",
    #                 "image": "saruar.jpg",
    #                 "description": "check check",
    #                 "tags": [
    #                     "Swift", "SwiftUI", "iOS Deveploment"
    #                 ],
    #                 "link": "https://github.com/sjalim/CricInfo"
    #             },
    #             {
    #                 "name": "check",
    #                 "image": "saruar.jpg",                    
    #                 "description": "check check",
    #                 "tags": [
    #                     "Swift", "SwiftUI", "iOS Deveploment"
    #                 ],
    #                 "link": "https://github.com/sjalim/CricInfo"
    #             },
    #              {
    #                 "name": "check",
    #                 "image": "saruar.jpg",
    #                 "description":  "check check",
    #                 "tags": [
    #                     "Swift", "SwiftUI", "iOS Deveploment"
    #                 ],
    #                 "link": "https://github.com/sjalim/CricInfo"
    #             },              
    #                   {
    #                 "name": "check",
    #                 "image": "saruar.jpg",
    #                 "description": "check check",
    #                 "tags": [
    #                     "Swift", "SwiftUI", "iOS Deveploment"
    #                 ],
    #                 "link": "https://github.com/sjalim/CricInfo"
    #             },  
    #         ]
    #     }
    # ]


def research(request):
    return render(request, "research.html")

def publication(request):
    return render(request, "publication.html")

def resume(request):
    return render(request, "resume.html")

def contact(request):
    return render(request, "contact.html")

def todos(request):
    items = TodoItem.objects.all()
    sections = [
        {
            'id': 'section1',
            'headline': 'Introduction',
            'content': 'Lorem ipsum dolor sit amet, consectetur adipiscing elit. Nullam auctor, nisl eget ultricies tincidunt, nisl nisl aliquam nisl, eget ultricies nisl nisl eget nisl. Nullam auctor, nisl eget ultricies tincidunt, nisl nisl aliquam nisl, eget ultricies nisl nisl eget nisl. Lorem ipsum dolor sit amet, consectetur adipiscing elit. Nullam auctor, nisl eget ultricies tincidunt, nisl nisl aliquam nisl, eget ultricies nisl nisl eget nisl. Nullam auctor, nisl eget ultricies tincidunt, nisl nisl aliquam nisl, eget ultricies nisl nisl eget nisl.'
        },
        {
            'id': 'section2',
            'headline': 'Key Features',
            'content': 'Sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum. Sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur.'
        },
        {
            'id': 'section3',
            'headline': 'Technical Specifications',
            'content': 'Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum. Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum. Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat.'
        },
        {
            'id': 'section4',
            'headline': 'How It Works',
            'content': 'Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum. Lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum. Lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.'
        },
        {
            'id': 'section5',
            'headline': 'Conclusion',
            'content': 'Sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum. Lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum. Lorem ipsum dolor sit amet, consectetur adipiscing elit.'
        },
    ]
    return render(request, "todos.html", {'sections': sections})



