from portfolio.models import Section


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
                            "name": "Framework",
                            " ": [
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


for section in skills_data:
    Section.objects.create(**section)