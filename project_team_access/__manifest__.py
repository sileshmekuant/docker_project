{
    "name": "Project Team Access",
    "version": "17.0.1.0.0",
    "category": "Project",
    "summary": "Team-based access control for projects",
    "author": "sss",
    "depends": ["project"],
    "data": [
        "security/project_team_security.xml",
        "security/ir.model.access.csv",
        "views/project_team_view.xml",
    ],
    "installable": True,
    "application": False,
    "auto_install": False,
}