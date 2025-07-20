from django.shortcuts import render, HttpResponse
from .models import TodoItem, EducationItem, AchievementItem
# Create your views here.

def home(request):
    return render(request, "home.html")

def education(request):
    educationItems = EducationItem.objects.all()
    achievementItems = AchievementItem.objects.all()

    return render(request, "education.html", {"educationItems": educationItems, "achievementItems": achievementItems})

def skill(request):
    skills_data = [
                {
                    "section": "Data Science",
                    "categories": [
                        {
                            "name": "Programming",
                            "skills": [
                                {"name": "Python", "icon": "python.png"},
                                {"name": "R", "icon": "r.png"}
                            ]
                        },
                        {
                            "name": "Framework",
                            "skills": [
                                {"name": "PyTorch", "icon": "pytorch.png"},
                                {"name": "TensorFlow", "icon": "tensorflow.png"},
                                {"name": "SciKit-Learn", "icon": "scikit-learn.png"},
                                {"name": "Numpy", "icon": "numpy.png"},
                                {"name": "Pandas", "icon": "pandas.png"},
                                {"name": "Matplotlib", "icon": "matplotlib.png"},
                                {"name": "Seaborn", "icon": "seaborn.png"}
                            ]
                        },
                        {
                            "name": "Tools",
                            "skills": [
                                {"name": "Google Colab", "icon": "google-colab.png"},
                                {"name": "Jupyter Notebook", "icon": "jupyter.png"},
                                {"name": "OpenCV", "icon": "opencv.png"},
                                {"name": "SQLAlchemy", "icon": "sqlalchemy.png"},
                                {"name": "Power BI", "icon": "powerbi.png"},
                                {"name": "Tableau", "icon": "tableau.png"},
                                {"name": "PyODBC", "icon": "pyodbc.png"},
                                {"name": "psycopg2", "icon": "psycopg2.png"}
                            ]
                        }
                    ]
                },
                {
                    "section": "App Development",
                    "categories": [
                        {
                            "name": "Programming",
                            "skills": [
                                {"name": "Swift", "icon": "swift.png"},
                                {"name": "Dart", "icon": "dart.png"},
                                {"name": "Java", "icon": "java.png"},
                                {"name": "Objective C", "icon": "objc.png"}
                            ]
                        },
                        {
                            "name": "Frameworks",
                            "skills": [
                                {"name": "SwiftUI", "icon": "swiftui.png"},
                                {"name": "UIKit", "icon": "uikit.png"},
                                {"name": "iOS Core Frameworks", "icon": "ios.png"},
                                {"name": "Flutter", "icon": "flutter.png"},
                                {"name": "Android Development", "icon": "android-development.png"}
                            ]
                        },
                        {
                            "name": "Tools",
                            "skills": [
                                {"name": "Xcode", "icon": "xcode.png"},
                                {"name": "SceneBuilder", "icon": "scenebuilder.png"},
                                {"name": "Android Studio", "icon": "android-studio.png"},
                                {"name": "Jira", "icon": "jira.png"},
                                {"name": "Jenkins", "icon": "jenkins.png"}
                            ]
                        }
                    ]
                },
                {
                    "section": "Web Development",
                    "categories": [
                        {
                            "name": "Programming / Markup Languages",
                            "skills": [
                                {"name": "JavaScript", "icon": "javascript.png"},
                                {"name": "Python", "icon": "python.png"},
                                {"name": "C#", "icon": "csharp.png"},
                                {"name": "HTML", "icon": "html.png"},
                                {"name": "CSS", "icon": "css.png"},
                                {"name": "SCSS", "icon": "scss.png"}
                            ]
                        },
                        {
                            "name": "Frameworks",
                            "skills": [
                                {"name": "ReactJS", "icon": "reactjs.png"},
                                {"name": "TypeScript", "icon": "typescript.png"},
                                {"name": "NextJS", "icon": "nextjs.png"},
                                {"name": "Django", "icon": "django.png"},
                                {"name": "ASP .NET", "icon": "aspnet.png"},
                                {"name": "Bootstrap", "icon": "bootstrap.png"},
                                {"name": "Beautiful Soup", "icon": "beautifulsoup.png"},
                                {"name": "Selenium", "icon": "selenium.png"}
                            ]
                        },
                        {
                            "name": "Tools",
                            "skills": [
                                {"name": "VSCode", "icon": "vscode.png"},
                                {"name": "Intellij", "icon": "intellij.png"},
                                {"name": "Figma", "icon": "figma.png"},
                                {"name": "Docker", "icon": "docker.png"},
                                {"name": "Material-UI", "icon": "materialui.png"}
                            ]
                        }
                    ]
                },
                {
                    "section": "Desktop Application Development",
                    "categories": [
                        {
                            "name": "Programming",
                            "skills": [
                                {"name": "Java", "icon": "java.png"}
                            ]
                        },
                        {
                            "name": "Frameworks",
                            "skills": [
                                {"name": "JavaFX", "icon": "javafx.png"},
                                {"name": "Javaswing", "icon": "javaswing.png"}
                            ]
                        },
                        {
                            "name": "Tools",
                            "skills": [
                                {"name": "SceneBuilder", "icon": "scenebuilder.png"}
                            ]
                        }
                    ]
                }
            ]
    return render(request, "skill.html", {'skills_data': skills_data})

def achievement(request):
    return render(request, "achievement.html")

def job_experience(request):

    positions = [   
        {
            'title': 'Software Engineer',
            'company': 'Tech Company',
            'company_link': 'https://www.techcompany.com',
            'department': 'Engineering',
            'duration': 'Jan 2020 - Present',
            'description': 'Developed and maintained web applications using Django and React.'
        },
        {
            'title': 'Data Analyst',
            'company': 'Data Company',
            'location': 'City, Country',
            'duration': 'Jan 2019 - Dec 2019',
            'description': 'Analyzed data using Python and SQL to provide insights for business decisions.'
        },
        {
            'title': 'Intern',
            'company': 'Internship Company',
            'location': 'City, Country',
            'duration': 'Jun 2018 - Aug 2018',
            'description': 'Assisted in software development projects and learned about Agile methodologies.'
        }

    ]
    return render(request, "job_experience.html", {'positions': positions})

def project(request):
    return render(request, "project.html")

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



