# How to setup indexers with limited API

So you have access to a few (unpaid) usenet indexers with limited API calls and you still want to add them as backup for failed downloads, but you're always hitting the API limits in the first hour and can't make fully use of them.

In this Guide i will show you a trick how you can make more use of them without hitting the API limit in the first hour.

!!! info "This is mainly a usenet option but might be useful for a few trackers that have rate limits. I will use for this guide mainly usenet indexers as examples."

## Sync Profiles

This is the same you see in the Starr apps under indexers when you open the specific indexer settings.

A short description what they do, mean and when they are used.

- RSS = The so called search interval.
- Automatic search = When a item is added to the Starr apps and you do a `Add + Search`, if a "usenet" download fails it will search for a replacement, When you click on the `Search All`, `Search Monitored` or on the `magnifying icon`.
- Interactive search = When you select interactive search you get a unsorted/unfiltered list of everything your indexer(s) reports back where you can choose what you want to grab.

### Adding a Sync Profile

For this we're going to create 2 new Sync Profiles

`Settings` => `Apps`

![Settings => Apps => Sync Profiles](images/settings-apps-sync-profiles.png)

#### Automatic Search

Click on the + sign and create a new sync profile with the following options.

1. Name it `Automatic Search`
1. **Disable** Enable RSS
1. Enable Interactive Search
1. Enable Automatic Search
1. If you're using usenet ignore this, if you use public torrent trackers set this somewhere between 20-70, being they often lie about their seeders amount.
1. Click on Save

![Sync Profile Automatic Search](images/sync-profile-automatic-search.png)

#### Interactive Search

Click on the + sign and create a new sync profile with the following options.

1. Name it `Interactive Search`
1. **Disable** Enable RSS
1. Enable Interactive Search
1. **Disable** Enable Automatic Search
1. If you're using usenet ignore this, if you use public torrent trackers set this somewhere between 20-70, being they often lie about their seeders amount.
1. Click on Save

![Sync Profile Automatic Search](images/sync-profile-interactive-search.png)