# Copyright 2021 - Dacosys - Miguel Hatrick

from datetime import date, timedelta, datetime

import pytz
from odoo.http import request, route
from odoo.addons.website_event_snippet_calendar.controllers.main import EventCalendar
from tzlocal import get_localzone # $ pip install tzlocal


class EventCalendarExtend(EventCalendar):
    @route("/website_event_snippet_calendar/events_for_day", auth="public", type="json", website=True)
    def events_for_day(self, day=None, limit=None):
        """List events for a given day.

        :param day string:
            Date in a string. If ``None``, we'll search for upcoming events
            from today up to specified limit.

        :param limit int:
            How many results to return.
        """

        _cd = date.today()
        if day:
            _cd = datetime.strptime(day, '%Y-%m-%d')

        # Get current TZ and convert the date to UTC
        _tz = get_localzone()
        _cd = _tz.localize(_cd, is_dst=None).astimezone(pytz.utc)

        domain = [("date_end", "<=", (_cd + timedelta(days=1)).strftime("%Y-%m-%d %H:%M:%S"))]
        domain += [("date_begin", ">=", _cd.strftime("%Y-%m-%d %H:%M:%S"))]

        return request.env["event.event"].search_read(
            domain=domain,
            limit=limit,
            fields=[
                "date_begin_pred_located",
                "name",
                "event_type_id",
                "website_published",
                "website_url",
            ],
        )

