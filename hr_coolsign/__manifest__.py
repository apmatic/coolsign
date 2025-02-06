{
    'name': 'Coolsign',
    'summary': 'Smart mobile attendance',
    'description': """
        Coolsign is a free solution for employee attendance. Using it,
        an employee can easily check in and out using his or her smartphone.
        The detected location will be saved in the attendance record.
        Coolsign consists of a backend part, this module, and a frontend one,
        the Android app.
        The employee must have a corresponding user; the Android app
        requires login and password of this user to gain access to Odoo.
        A new field in the employee can be used by the HR Manager to enable or
        disable the use of the smartphone app by that employee.  
    """,
    'author': 'Apmatic',
    'website': 'https://github.com/apmatic/coolsign',
    'category': 'Human Resources',
    'version': '17.0.1.0.0',
    'depends': ['hr'],
    'data': ['views/hr_employee.xml'],
    'demo': [],
    'images': ['static/description/banner.jpg'],
    'license': 'LGPL-3'
}
