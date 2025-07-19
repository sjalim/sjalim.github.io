from portfolio.models import EducationItem

educationItems = [
    {
        "schoolNameText": "Ahsanullah University of Science and Technology",
        "schoolWebsiteLink": "https://aust.edu/",
        "degreeNameText": "Bachelor of Science in Computer Science & Engineering",
        "departmentNameText": "Department of Computer Science & Engineering",
        "certificateLink": "https://shorturl.at/nYcPZ",
        "durationText": "2018 - 2023",
        "gradeText": "GPA: 3.285/4.0",
        "transcriptLink": "https://shorturl.at/AjS4n"
    },
    {
        "schoolNameText": "Mirpur Cantonment Public School & College",
        "schoolWebsiteLink": "https://mcpsc.edu.bd/",
        "degreeNameText": "Secondary School Certificate",
        "departmentNameText": "Science",
        "certificateLink": "https://shorturl.at/6Tkzq",
        "durationText": "2015 - 2017",
        "gradeText": "GPA: 5.00/5.00",
        "transcriptLink": "https://shorturl.at/i7Ui4"
    },
]

for item in educationItems:
    EducationItem.objects.create(**item)