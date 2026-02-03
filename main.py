import pandas as pd
from browser_agent import BrowserAgent
from ai_agent import get_form_instructions


def main():
    df = pd.read_excel("input.xlsx")

    browser = BrowserAgent()
    browser.start_browser()

    for index, row in df.iterrows():
        print(f"Processing row {index + 1}")

        browser.login(row["Username"], row["Password"])

        row_data = row.to_dict()
        instructions = get_form_instructions(row_data)

        print("AI Instructions:", instructions)

        browser.fill_form(instructions)

    browser.close_browser()


if __name__ == "__main__":
    main()
