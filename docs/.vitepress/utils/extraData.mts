import fs from "node:fs";
import path from "node:path";

/**
 * Recursively load docs/json into a nested object mirroring the folder tree:
 * directories become nested keys, and each `<name>.json` file becomes a key
 * (`<name>`) holding its parsed content. Mirrors the old markdownextradata plugin.
 */
export function loadExtraData(jsonRoot: string): Record<string, unknown> {
  function walk(dir: string): Record<string, unknown> {
    const result: Record<string, unknown> = {};
    for (const entry of fs.readdirSync(dir, { withFileTypes: true })) {
      const full = path.join(dir, entry.name);
      if (entry.isDirectory()) {
        result[entry.name] = walk(full);
      } else if (entry.isFile() && entry.name.endsWith(".json")) {
        const key = entry.name.slice(0, -".json".length);
        result[key] = JSON.parse(fs.readFileSync(full, "utf-8"));
      }
    }
    return result;
  }
  return walk(jsonRoot);
}
