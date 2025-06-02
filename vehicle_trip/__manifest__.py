{
    "name": "Vehicle Trip",
    "version": "1.0",
    "depends": ["base","fleet"],
    "author": "silesh",
    "category": "Transport",
    "description": "Vehicle Trip Management",
    "data": [
        "security/ir.model.access.csv",
        "views/vehicle_trip_views.xml",
        "views/vehicle_trip_passout_view.xml",
        # "report/report_action.xml",
        "report/passout_print_action.xml",
        # "report/vehicle_trip_template.xml",
        "report/vehicle_trip_passout_template.xml",
    ],
    "installable": True,
    "application": True,
}
