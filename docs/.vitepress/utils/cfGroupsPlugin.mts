import type MarkdownIt from "markdown-it";
import { renderCfGroups, type CFGroup } from "./cfGroups.mts";

const MARKER_RE = /<!--\s*@cf-groups:\s*(radarr|sonarr)\s*-->/g;

/** Expands `<!--@cf-groups: radarr|sonarr-->` into the generated Custom Format
 * Groups tables, replacing the old Jinja for-loop template. */
export function cfGroupsPlugin(md: MarkdownIt, data: Record<string, unknown>) {
  md.core.ruler.before("normalize", "cf-groups", (state) => {
    state.src = state.src.replace(MARKER_RE, (_full, app: "radarr" | "sonarr") => {
      const namespace = data[app] as { "cf-groups": Record<string, CFGroup> };
      const cfPageLink =
        app === "radarr"
          ? "../Radarr/Radarr-collection-of-custom-formats.md"
          : "../Sonarr/sonarr-collection-of-custom-formats.md";
      return renderCfGroups(namespace["cf-groups"], cfPageLink);
    });
  });
}
