import textwrap


def render_issue_card(issue: dict) -> str:
    category = issue["category"].upper()
    status = issue["status"].upper()

    return textwrap.dedent(
        f"""
        ID       : {issue["id"]}
        TITLE    : {issue["title"]}
        CATEGORY : {category:<9}
        STATUS   : {status:>9}
        """
    ).strip()


def render_banner(title: str) -> str:
    width = 40
    line = "=" * width

    return f"{line}\n{title}\n{line}"