# Copyright 2021 Miguel Hatrick (Dacosys)
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl).

{
    "name": "website_event_snippet_calendar_fix",
    "summary": """
            Fixes the problem with timezones on non UTC events
    """,
    "version": "12.0.1.0.1",
    "author": "Miguel Hatrick",
    "license": "AGPL-3",
    "maintainer": "Dacosys",
    "category": "Extra Tools",
    "website": "https://www.dacosys.com",
    "depends": [
        "website_event_snippet_calendar",
    ],
    "external_dependencies": {
        "python": [
            'tzlocal'
        ]
    },
    "data": [
    ],
    "installable": True,
}
