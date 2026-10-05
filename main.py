from config import APP_NAME, APP_VERSION, DEFAULT_WARDS, SLA_HOURS
import reports


issue = {
    "id": "CIV-001",
    "title": "Streetlight not working",
    "category": "electricity",
    "status": "open",
}


if __name__ == "__main__":

    print(reports.render_banner("Civic Issue Report"))
    print()
    print(reports.render_issue_card(issue))


    print("APP_NAME:", type(APP_NAME))
    print("APP_VERSION:", type(APP_VERSION))
    print("DEFAULT_WARDS:", type(DEFAULT_WARDS))
    print("SLA_HOURS:", type(SLA_HOURS))