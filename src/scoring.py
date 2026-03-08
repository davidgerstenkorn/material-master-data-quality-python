import pandas as pd


def build_issue_report(
    df,
    negative_stock,
    missing_desc,
    missing_unit,
    missing_lead,
    duplicates,
):
    issues = []

    for _, row in negative_stock.iterrows():
        issues.append(
            {
                "material_id": row["material_id"],
                "issue": "negative_stock",
            }
        )

    for _, row in missing_desc.iterrows():
        issues.append(
            {
                "material_id": row["material_id"],
                "issue": "missing_description",
            }
        )

    for _, row in missing_unit.iterrows():
        issues.append(
            {
                "material_id": row["material_id"],
                "issue": "missing_base_unit",
            }
        )

    for _, row in missing_lead.iterrows():
        issues.append(
            {
                "material_id": row["material_id"],
                "issue": "missing_lead_time",
            }
        )

    for _, row in duplicates.iterrows():
        issues.append(
            {
                "material_id": row["material_id"],
                "issue": "duplicate_material",
            }
        )

    report_df = pd.DataFrame(issues)

    summary_df = (
        report_df
        .groupby("issue")
        .size()
        .reset_index(name="count")
    )

    return report_df, summary_df
