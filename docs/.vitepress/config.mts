import path from "node:path";
import { fileURLToPath } from "node:url";
import { defineConfig } from "vitepress";
import { withSidebar } from "vitepress-sidebar";
import { tabsMarkdownPlugin } from "vitepress-plugin-tabs";
import { loadExtraData } from "./utils/extraData.mts";
import { extraDataPlugin } from "./utils/extraDataPlugin.mts";
import { cfGroupsPlugin } from "./utils/cfGroupsPlugin.mts";

const __dirname = path.dirname(fileURLToPath(import.meta.url));
const extraData = loadExtraData(path.join(__dirname, "../json"));

export default defineConfig(
  withSidebar(
    // https://vitepress.dev/reference/site-config
    {
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

        sidebar: [
          {
            text: "Examples",
            items: [
              { text: "Markdown Examples", link: "/markdown-examples" },
              { text: "Runtime API Examples", link: "/api-examples" },
            ],
          },
        ],

        socialLinks: [
          { icon: "github", link: "https://github.com/vuejs/vitepress" },
        ],
      },
      cleanUrls: true,
      ignoreDeadLinks: true,
    },
    // https://vitepress-sidebar.cdget.com/advanced-usage/configuration-file
    [
      {
        // VitePress Sidebar's options here...
        documentRootPath: "/docs",
        collapsed: true,
        capitalizeFirst: false,
        useTitleFromFileHeading: true,
        // includeRootIndexFile: true,
        // includeFolderIndexFile: true,
        hyphenToSpace: true,
        underscoreToSpace: true,
        useFolderLinkFromIndexFile: true,
      },
      {
        // VitePress Sidebar's options here...
        documentRootPath: "/docs",
        collapsed: true,
        capitalizeFirst: false,
        useTitleFromFileHeading: true,

        scanStartPath: "3rd-Party-Apps",
        resolvePath: "/3rd-Party-Apps/",
      },
      {
        // VitePress Sidebar's options here...
        documentRootPath: "/docs",
        collapsed: true,
        capitalizeFirst: false,
        useTitleFromFileHeading: true,

        scanStartPath: "Bazarr",
        resolvePath: "/Bazarr/",
      },
      {
        // VitePress Sidebar's options here...
        documentRootPath: "/docs",
        collapsed: true,
        capitalizeFirst: false,
        useTitleFromFileHeading: true,

        scanStartPath: "Downloaders",
        resolvePath: "/Downloaders/",
      },
      {
        // VitePress Sidebar's options here...
        documentRootPath: "/docs",
        collapsed: true,
        capitalizeFirst: false,
        useTitleFromFileHeading: true,

        scanStartPath: "File-and-Folder-Structure",
        resolvePath: "/File-and-Folder-Structure/",
      },
      {
        // VitePress Sidebar's options here...
        documentRootPath: "/docs",
        collapsed: true,
        capitalizeFirst: false,
        useTitleFromFileHeading: true,

        scanStartPath: "Getting-Started",
        resolvePath: "/Getting-Started/",
      },
      {
        // VitePress Sidebar's options here...
        documentRootPath: "/docs",
        collapsed: true,
        capitalizeFirst: false,
        useTitleFromFileHeading: true,

        scanStartPath: "Glossary",
        resolvePath: "/Glossary/",
      },
      {
        // VitePress Sidebar's options here...
        documentRootPath: "/docs",
        collapsed: true,
        capitalizeFirst: false,
        useTitleFromFileHeading: true,

        scanStartPath: "Guide-Sync",
        resolvePath: "/Guide-Sync/",
      },
      {
        // VitePress Sidebar's options here...
        documentRootPath: "/docs",
        collapsed: true,
        capitalizeFirst: false,
        useTitleFromFileHeading: true,

        scanStartPath: "Lidarr",
        resolvePath: "/Lidarr/",
      },
      {
        // VitePress Sidebar's options here...
        documentRootPath: "/docs",
        collapsed: true,
        capitalizeFirst: false,
        useTitleFromFileHeading: true,

        scanStartPath: "Misc",
        resolvePath: "/Misc/",
      },
      {
        // VitePress Sidebar's options here...
        documentRootPath: "/docs",
        collapsed: true,
        capitalizeFirst: false,
        useTitleFromFileHeading: true,

        scanStartPath: "Plex",
        resolvePath: "/Plex/",
      },
      {
        // VitePress Sidebar's options here...
        documentRootPath: "/docs",
        collapsed: true,
        capitalizeFirst: false,
        useTitleFromFileHeading: true,

        scanStartPath: "Prowlarr",
        resolvePath: "/Prowlarr/",
      },
      {
        // VitePress Sidebar's options here...
        documentRootPath: "/docs",
        collapsed: true,
        capitalizeFirst: false,
        useTitleFromFileHeading: true,

        scanStartPath: "Radarr",
        resolvePath: "/Radarr/",
      },
      {
        // VitePress Sidebar's options here...
        documentRootPath: "/docs",
        collapsed: true,
        capitalizeFirst: false,
        useTitleFromFileHeading: true,

        scanStartPath: "Recyclarr",
        resolvePath: "/Recyclarr/",
      },
      {
        // VitePress Sidebar's options here...
        documentRootPath: "/docs",
        collapsed: true,
        capitalizeFirst: false,
        useTitleFromFileHeading: true,

        scanStartPath: "SQP",
        resolvePath: "/SQP/",
      },
      {
        // VitePress Sidebar's options here...
        documentRootPath: "/docs",
        collapsed: true,
        capitalizeFirst: false,
        useTitleFromFileHeading: true,

        scanStartPath: "Sonarr",
        resolvePath: "/Sonarr/",
      },
    ],
  ),
);
