import path from "node:path";
import { fileURLToPath } from "node:url";
import { defineConfig, DefaultTheme } from "vitepress";
import { tabsMarkdownPlugin } from "vitepress-plugin-tabs";
import { loadExtraData } from "./utils/extraData.mts";
import { extraDataPlugin } from "./utils/extraDataPlugin.mts";
import { cfGroupsPlugin } from "./utils/cfGroupsPlugin.mts";

const __dirname = path.dirname(fileURLToPath(import.meta.url));
const extraData = loadExtraData(path.join(__dirname, "../json"));

const gettingStartedSidebar: DefaultTheme.SidebarItem = {
  text: "Getting Started",
  link: "/",
  base: "/Getting-Started/",
  collapsed: true,
  items: [{ text: "Home", link: "/" }],
};

const radarrSidebar: DefaultTheme.SidebarItem = {
  text: "Radarr",
  link: "/",
  base: "/Radarr/",
  collapsed: true,
  items: [
    { text: "Home", link: "/" },
    {
      text: "Quality Settings (File Size)",
      link: "Radarr-Quality-Settings-File-Size",
    },
    {
      text: "Recommended naming scheme",
      link: "Radarr-recommended-naming-scheme",
    },
    {
      text: "How to set up Quality Profiles",
      link: "Radarr-how-to-update-custom-formats",
    },
    {
      text: "How to set up Quality Profiles (Anime)",
      link: "radarr-setup-quality-profiles-anime",
    },
    {
      text: "How to set up Quality Profiles (French)",
      link: "radarr-setup-quality-profiles-french-en",
    },
    {
      text: "How to set up Quality Profiles (German)",
      link: "radarr-setup-quality-profiles-german-en",
    },
    {
      text: "How to import Custom Formats",
      link: "Radarr-import-custom-formats",
    },
    {
      text: "How to Update Custom Formats",
      link: "Radarr-how-to-update-custom-formats",
    },
    {
      text: "Collection of Custom Formats",
      link: "Radarr-collection-of-custom-formats",
    },
    {
      text: "Tips",
      base: "/Radarr/Tips/",
      collapsed: true,
      items: [
        {
          text: "How to Merge Quality",
          link: "Merge-quality",
        },
        {
          text: "How to Order Quality Sources",
          link: "How-to-order-Quality-Source",
        },
        {
          text: "How to rename your folders",
          link: "Radarr-rename-your-folders",
        },
        {
          text: "How to set up Language Custom Formats",
          link: "How-to-setup-language-custom-formats",
        },
        {
          text: "How to Sync 2 Radarr or Sonarr with each other",
          link: "Sync-2-radarr-sonarr",
        },
        {
          text: "Remote Path Mappings",
          link: "Radarr-remote-path-mapping",
        },
        {
          text: "Show Unknown Movie Items",
          link: "Radarr-show-unknown-movie-items",
        },
      ],
    },
  ],
};

const sonarrSidebar: DefaultTheme.SidebarItem = {
  text: "Sonarr",
  link: "/",
  base: "/Sonarr/",
  collapsed: true,
  items: [
    { text: "Home", link: "/" },
    {
      text: "Quality Settings (File Size)",
      link: "Sonarr-Quality-Settings-File-Size",
    },
    {
      text: "Recommended naming scheme",
      link: "Sonarr-recommended-naming-scheme",
    },
    {
      text: "How to set up Quality Profiles",
      link: "sonarr-setup-quality-profiles",
    },
    {
      text: "How to set up Quality Profiles (Anime)",
      link: "sonarr-setup-quality-profiles-anime",
    },
    {
      text: "How to set up Quality Profiles (French)",
      link: "sonarr-setup-quality-profiles-french-en",
    },
    {
      text: "How to set up Quality Profiles (German)",
      link: "sonarr-setup-quality-profiles-german-en",
    },
    {
      text: "How to import Custom Formats",
      link: "sonarr-import-custom-formats",
    },
    {
      text: "How to Update Custom Formats",
      link: "sonarr-how-to-update-custom-formats",
    },
    {
      text: "Collection of Custom Formats",
      link: "sonarr-collection-of-custom-formats",
    },
    {
      text: "Tips",
      base: "/Sonarr/Tips/",
      collapsed: true,
      items: [
        {
          text: "How to Merge Quality",
          link: "Merge-quality",
        },
        {
          text: "How to Order Quality Sources",
          link: "How-to-order-Quality-Source",
        },
        {
          text: "How to rename your folders",
          link: "Sonarr-rename-your-folders",
        },
        {
          text: "How to set up Language Custom Formats",
          link: "How-to-setup-language-custom-formats",
        },
        {
          text: "How to Sync 2 Radarr or Sonarr with each other",
          link: "Sync-2-radarr-sonarr",
        },
        {
          text: "Remote Path Mappings",
          link: "Sonarr-remote-path-mapping",
        },
      ],
    },
  ],
};

const prowlarrSidebar: DefaultTheme.SidebarItem = {
  text: "Prowlarr",
  link: "/",
  base: "/Prowlarr/",
  collapsed: true,
  items: [
    { text: "Home", link: "/" },
    {
      text: "How to set up proxy for certain indexers",
      link: "prowlarr-setup-proxy",
    },
    { text: "How to set up FlareSolverr", link: "prowlarr-setup-flaresolverr" },
    {
      text: "How to set up indexers with limited API",
      link: "prowlarr-setup-limited-api",
    },
  ],
};

const fileAndFolderStructureSidebar: DefaultTheme.SidebarItem = {
  text: "File and Folder Structure",
  link: "/",
  base: "/File-and-Folder-Structure/",
  collapsed: true,
  items: [
    { text: "Home", link: "/" },
    {
      text: "Hardlinks and Instant Moves",
      link: "Hardlinks-and-Instant-Moves",
    },
    {
      text: "How To Set Up",
      link: "/",
      base: "/File-and-Folder-Structure/How-to-set-up/",
      collapsed: true,
      items: [
        { text: "Docker", link: "Docker" },
        { text: "Dockstarter", link: "Dockstarter" },
        { text: "Native", link: "Native" },
        { text: "Synology", link: "Synology" },
        { text: "TrueNAS Core", link: "TrueNAS-Core" },
        { text: "unRAID", link: "Unraid" },
        { text: "Windows", link: "Windows" },
      ],
    },
    { text: "Examples", link: "Examples" },
    {
      text: "Check if Hardlinks Are Working",
      link: "Check-if-hardlinks-are-working",
    },
    {
      text: "Replace Copies With Hardlink",
      link: "Replace-copies-with-hardlinks",
    },
  ],
};

const nzbgetSidebar: DefaultTheme.SidebarItem = {
  text: "NZBGet",
  link: "/",
  base: "/Downloaders/NZBGet/",
  collapsed: true,
  items: [
    { text: "Basic-Setup", link: "Basic-Setup" },
    { text: "Path and Categories", link: "Paths-and-Categories" },
    { text: "Scripts", link: "scripts" },
  ],
};

const sabnzbdSidebar: DefaultTheme.SidebarItem = {
  text: "SABnzbd",
  link: "/",
  base: "/Downloaders/SABnzbd/",
  collapsed: true,
  items: [
    { text: "Basic-Setup", link: "Basic-Setup" },
    { text: "Path and Categories", link: "Paths-and-Categories" },
    { text: "Scripts", link: "scripts" },
  ],
};

const qbittorrentSidebar: DefaultTheme.SidebarItem = {
  text: "qBittorrent",
  link: "/",
  base: "/Downloaders/qBittorrent/",
  collapsed: true,
  items: [
    { text: "Basic-Setup", link: "Basic-Setup" },
    { text: "Paths", link: "Paths" },
    { text: "How to add Categories", link: "How-to-add-categories" },
    { text: "Port forwarding", link: "Port-forwarding" },
    {
      text: "Tips",
      base: "/Downloaders/qBittorrent/Tips/",
      collapsed: true,
      items: [
        {
          text: "unRAID Mover and qBittorrent",
          link: "How-to-run-the-unRaid-mover-for-qBittorrent",
        },
        {
          text: "qBittorrent UI Replacements",
          link: "qBit-UI-replacements",
        },
      ],
    },
  ],
};

const delugeSidebar: DefaultTheme.SidebarItem = {
  text: "Deluge",
  link: "/",
  base: "/Downloaders/Deluge/",
  collapsed: true,
  items: [
    { text: "Installing", link: "Installing" },
    { text: "Basic-Setup", link: "Basic-Setup" },
    { text: "Using Labels", link: "Using-Labels" },
    { text: "Port forwarding", link: "Port-Forwarding" },
    {
      text: "Tips",
      base: "/Downloaders/Deluge/Tips/",
      collapsed: true,
      items: [
        { text: "Plugins", link: "Plugins" },
        { text: "Thin Client", link: "Thin-Client" },
        {
          text: "unRAID Mover and Deluge",
          link: "Unraid-Mover",
        },
      ],
    },
  ],
};

const rutorrentSidebar: DefaultTheme.SidebarItem = {
  text: "ruTorrent",
  link: "/",
  base: "/Downloaders/ruTorrent/",
  collapsed: true,
  items: [
    { text: "ruTorrent Placeholder", link: "/" },
    { text: "Basic Setup", link: "ruTorrent-Basic-Setup" },
  ],
};

const downloadersSidebar: DefaultTheme.SidebarItem = {
  text: "Downloaders",
  link: "/",
  base: "/Downloaders/",
  collapsed: true,
  items: [
    { text: "Home", link: "/" },
    { ...nzbgetSidebar },
    { ...sabnzbdSidebar },
    { ...qbittorrentSidebar },
    { ...delugeSidebar },
    { ...rutorrentSidebar },
    {
      text: "Port Forwarding Troubleshooting",
      link: "port-forwarding-troubleshooting",
    },
    { text: "3rd Party tools", link: "3rd-party-tools" },
  ],
};

const plexSidebar: DefaultTheme.SidebarItem = {
  text: "Plex",
  link: "/",
  base: "/Plex/",
  collapsed: true,
  items: [{ text: "Home", link: "/" }],
};

const guideSyncSidebar: DefaultTheme.SidebarItem = {
  text: "Guide Sync",
  link: "/",
  base: "/Guide-Sync/",
  collapsed: true,
  items: [{ text: "Home", link: "/" }],
};

const miscSidebar: DefaultTheme.SidebarItem = {
  text: "Misc",
  link: "/",
  base: "/Misc/",
  collapsed: true,
  items: [{ text: "Home", link: "/" }],
};

const thirdPartyAppsSidebar: DefaultTheme.SidebarItem = {
  text: "3rd Party Apps",
  link: "/",
  base: "/3rd-Party-Apps/",
  collapsed: true,
  items: [{ text: "Home", link: "/" }],
};

const glossarySidebar: DefaultTheme.SidebarItem = {
  text: "Glossary",
  link: "/",
  base: "/Glossary/",
  collapsed: true,
  items: [{ text: "Home", link: "/" }],
};

const sidebar: DefaultTheme.Sidebar = {
  "/": [
    { text: "Home", link: "/" },
    { ...gettingStartedSidebar, collapsed: true },
    { ...radarrSidebar, collapsed: true },
    { ...sonarrSidebar, collapsed: true },
    { ...prowlarrSidebar, collapsed: true },
    { ...fileAndFolderStructureSidebar, collapsed: true },
    { ...downloadersSidebar, collapsed: true },
    { ...plexSidebar, collapsed: true },
    { ...guideSyncSidebar, collapsed: true },
    { ...miscSidebar, collapsed: true },
    { ...thirdPartyAppsSidebar, collapsed: true },
    { ...glossarySidebar, collapsed: true },
  ],
  "/Getting-Started/": [{ ...gettingStartedSidebar, collapsed: false }],
  "/Radarr/": [{ ...radarrSidebar, collapsed: false }],
  "/Sonarr/": [{ ...sonarrSidebar, collapsed: false }],
  "/Prowlarr/": [{ ...prowlarrSidebar, collapsed: false }],
  "/File-and-Folder-Structure/": [
    { ...fileAndFolderStructureSidebar, collapsed: false },
  ],
  "/Downloaders/": [{ ...downloadersSidebar, collapsed: false }],
  "/Downloaders/NZBGet/": [{ ...nzbgetSidebar, collapsed: false }],
  "/Downloaders/SABnzbd/": [{ ...sabnzbdSidebar, collapsed: false }],
  "/Downloaders/qBittorrent/": [{ ...qbittorrentSidebar, collapsed: false }],
  "/Downloaders/Deluge/": [{ ...delugeSidebar, collapsed: false }],
  "/Downloaders/ruTorrent/": [{ ...rutorrentSidebar, collapsed: false }],
  "/Plex/": [{ ...plexSidebar, collapsed: false }],
  "/Guide-Sync/": [{ ...guideSyncSidebar, collapsed: false }],
  "/Misc/": [{ ...miscSidebar, collapsed: false }],
  "/3rd-Party-Apps/": [{ ...thirdPartyAppsSidebar, collapsed: false }],
  "/Glossary/": [{ ...glossarySidebar, collapsed: false }],
};

export default defineConfig({
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
      { text: "Getting Started", link: "/Getting-Started" },
      { text: "Apps", items: [
        { text: "3rd Party Apps", link: "/3rd-Party-Apps" },
        { text: "Deluge", link: "/Downloaders/Deluge" },
        { text: "NZBGet", link: "/Downloaders/NZBGet" },
        { text: "Plex", link: "/Plex" },
        { text: "Prowlarr", link: "/Prowlarr" },
        { text: "qBittorrent", link: "/Downloaders/qBittorrent" },
        { text: "Radarr", link: "/Radarr" },
        { text: "ruTorrent", link: "/Downloaders/ruTorrent" },
        { text: "SABnzbd", link: "/Downloaders/SABnzbd" },
        { text: "Sonarr", link: "/Sonarr" },
      ] },
      { text: "Misc", link: "/Misc" },
      { text: "Glossary", link: "/Glossary" },
    ],

    sidebar: sidebar,

    socialLinks: [
      { icon: "discord", link: "https://trash-guides.info/discord" },
      { icon: "github", link: "https://github.com/TRaSH-Guides/Guides" },
    ],

    editLink: {
      pattern: "https://github.com/TRaSH-Guides/Guides/edit/master/docs/:path",
    },

    search: {
      provider: "local",
    },
  },
  cleanUrls: true,
  ignoreDeadLinks: true,
  lastUpdated: true,
});
