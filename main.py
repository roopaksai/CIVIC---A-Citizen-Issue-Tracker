from config import APP_NAME, APP_VERSION, DEFAULT_WARDS, SLA_HOURS

def banner() -> str:
    title = APP_NAME
    ver = APP_VERSION
    
    return f"""
    {'=' * 20}
    {title} ({ver})
    {'=' * 20}\n"""


if __name__ == "__main__":
    print(banner())

    print("APP_NAME:", type(APP_NAME))
    print("APP_VERSION:", type(APP_VERSION))
    print("DEFAULT_WARDS:", type(DEFAULT_WARDS))
    print("SLA_HOURS:", type(SLA_HOURS))