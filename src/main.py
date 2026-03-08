from load_data import load_material_data
import checks
from scoring import build_issue_report


def run_data_quality_checks():

    df = load_material_data("data/material_master_raw.csv")

    negative_stock = checks.check_negative_stock(df)
    missing_desc = checks.check_missing_description(df)
    missing_unit = checks.check_missing_base_unit(df)
    missing_lead = checks.check_missing_lead_time(df)
    duplicates = checks.check_duplicates(df)

    print("Negative stock records:", len(negative_stock))
    print("Missing descriptions:", len(missing_desc))
    print("Missing base unit:", len(missing_unit))
    print("Missing lead time:", len(missing_lead))
    print("Duplicate materials:", len(duplicates))

    report_df, summary_df = build_issue_report(
        df,
        negative_stock,
        missing_desc,
        missing_unit,
        missing_lead,
        duplicates
    )

    report_df.to_csv("output/dq_report.csv", index=False)
    summary_df.to_csv("output/dq_summary.csv", index=False)

    print("\nReports written to output folder")


if __name__ == "__main__":
    run_data_quality_checks()
