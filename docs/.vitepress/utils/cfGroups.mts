export interface CFGroup {
  name: string;
  trash_id: string;
  trash_description?: string;
  default?: string;
  custom_formats?: { name: string; trash_id: string; required?: boolean }[];
  quality_profiles?: { include?: Record<string, string> };
}

function cfSlug(name: string): string {
  return name
    .toLowerCase()
    .replaceAll("+", "plus")
    .replaceAll("(", "")
    .replaceAll(")", "")
    .replaceAll("/", "")
    .replaceAll(".", "")
    .replaceAll(":", "")
    .replaceAll(",", "")
    .replaceAll(" ", "-")
    .replaceAll("--", "-");
}

/** Re-implements the old Jinja `cf-groups` template (grouped tables of Custom
 * Format Groups) as a static markdown generator driven by docs/json data. */
export function renderCfGroups(groups: Record<string, CFGroup>, cfPageLink: string): string {
  const lines: string[] = [];
  let currentCategory = "";

  for (const key of Object.keys(groups).sort()) {
    if (key.startsWith("sqp-") || key.endsWith("-sqp")) continue;
    const group = groups[key];

    const category = group.name.split("]")[0].slice(1);
    if (category !== currentCategory) {
      currentCategory = category;
      lines.push(`## ${category}`, "", "---", "");
    }

    lines.push(`### ${group.name.split("] ")[1]}`, "");
    lines.push("| Group Name | Trash ID | Default |");
    lines.push("| --- | --- | :---: |");
    const isDefault = group.default !== undefined && String(group.default) === "true";
    lines.push(`| ${group.name} | \`${group.trash_id}\` | ${isDefault ? ":white_check_mark:" : ":x:"} |`, "");

    lines.push("::: details Description - [Click to show/hide]", "");
    lines.push((group.trash_description ?? "").replaceAll("<br>", "\n\n"));
    lines.push(":::", "");

    lines.push("| Custom Format | Trash ID | Required |");
    lines.push("| --- | --- | :---: |");
    for (const cf of group.custom_formats ?? []) {
      lines.push(`| [${cf.name}](${cfPageLink}#${cfSlug(cf.name)}) | \`${cf.trash_id}\` | ${cf.required ? ":white_check_mark:" : ":x:"} |`);
    }
    lines.push("");

    const include = group.quality_profiles?.include ?? {};
    const entries = Object.entries(include)
      .filter(([pname]) => !pname.toLowerCase().includes("[sqp]"))
      .sort(([a], [b]) => a.localeCompare(b));
    if (entries.length > 0) {
      lines.push("::: details Applicable Quality Profiles - [Click to show/hide]", "");
      lines.push("| Quality Profile | Trash ID |");
      lines.push("| --- | --- |");
      for (const [pname, pid] of entries) {
        lines.push(`| ${pname} | \`${pid}\` |`);
      }
      lines.push(":::", "");
    }

    lines.push("---", "");
  }

  return lines.join("\n");
}
