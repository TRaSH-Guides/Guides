import path from "node:path";
import { fileURLToPath } from "node:url";
import { defineConfig } from "vitepress";
import { tabsMarkdownPlugin } from "vitepress-plugin-tabs";
import { loadExtraData } from "./utils/extraData.mts";
import { extraDataPlugin } from "./utils/extraDataPlugin.mts";
import { cfGroupsPlugin } from "./utils/cfGroupsPlugin.mts";
import sidebar from "./sidebar.generated.json" with { type: "json" };

const __dirname = path.dirname(fileURLToPath(import.meta.url));
const extraData = loadExtraData(path.join(__dirname, "../json"));

export default defineConfig({
  // https://vitepress.dev/reference/site-config
  title: "TRaSH Guides",
  description:
    "TRaSH-Guides is a comprehensive collection of guides for Radarr, Sonarr, and related media management tools. These guides answer common questions and provide the best settings for your entire media server setup.",
  markdown: {
    config(md) {
      md.use(tabsMarkdownPlugin);
      extraDataPlugin(md, extraData);
      cfGroupsPlugin(md, extraData);
    },
  },
  themeConfig: {
    // https://vitepress.dev/reference/default-theme-config
    nav: [
      { text: "Home", link: "/" },
      { text: "Examples", link: "/markdown-examples" },
    ],

    // Explicit, human-ordered sidebar generated from docs/**/.pages by
    // scripts/generate-vitepress-sidebar.py (pre-commit hook). Do not
    // hand-edit this file -- edit the relevant .pages instead and let the
    // hook regenerate it. See that script's docstring for the format.
    sidebar,

    socialLinks: [
      { icon: "github", link: "https://github.com/vuejs/vitepress" },
    ],

    search: {
      provider: "local",
    },
  },
  cleanUrls: true,
  ignoreDeadLinks: true,
});
