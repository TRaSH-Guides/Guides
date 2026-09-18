import { defineConfig } from "vitepress";
import { withSidebar } from "vitepress-sidebar";

// https://vitepress.dev/reference/site-config
const vitePressOptions = {
  title: "TRaSH Guides",
  description:
    "TRaSH-Guides is a comprehensive collection of guides for Radarr, Sonarr, and related media management tools. These guides answer common questions and provide the best settings for your entire media server setup.",
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
};

// https://vitepress-sidebar.cdget.com/advanced-usage/configuration-file
const vitePressSidebarOptions = [
  {
    // VitePress Sidebar's options here...
    documentRootPath: "/docs",
    collapsed: true,
    capitalizeFirst: false,
    useTitleFromFileHeading: true,
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
];

export default defineConfig(
  withSidebar(vitePressOptions, vitePressSidebarOptions),
);
