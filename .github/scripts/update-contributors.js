const axios = require('axios');
const fs = require('fs').promises;

class ContributorsFetcher {
  constructor() {
    this.contributors = '<div style="display: flex; flex-wrap: wrap;">';
    this.index = 0;
    this.excludedUsers = new Set(['actions-user', 'mynameisbogdan', 'ImgBotApp']);
    this.excludedTypes = new Set(['Bot']);
  }

  indentString(string, indentation = '    ') {
    return string.split('\n').map(line => indentation + line).join('\n').trim();
  }

  shouldExcludeUser(user) {
    const loginLower = user.login.toLowerCase();
    // Exclude if type matches, login ends with 'bot', or login is in excludedUsers (case-insensitive)
    return (
      this.excludedTypes.has(user.type) ||
      loginLower.endsWith('bot') ||
      Array.from(this.excludedUsers).some(excluded => excluded.toLowerCase() === loginLower)
    );
  }

  createUserHtml(user) {
    const rowIndex = Math.floor(this.index / 5);
    const bgColor = (rowIndex % 2 === 0) ? '#1e2129' : '#303850';

    return `
<div style="flex: 1 1 20%; background-color: ${bgColor}; border: 1px solid #373a42; padding: 10px; text-align: center;">
  <img src="${user.avatar_url}&v=4" style="width: 50px; border-radius: 50%;" alt="${user.login}">
  <br>
  <b><a href="${user.html_url}" style="color: #ffa500;">${user.login}</a></b>
</div>`;
  }

  async fetchPage(page) {
    try {
      const response = await axios.get(
        `https://api.github.com/repos/TRaSH-Guides/Guides/contributors`,
        {
          params: { per_page: 100, page },
          headers: {
            'User-Agent': 'TRaSH-Guides-Contributors-Updater',
            ...(process.env.GITHUB_TOKEN && {
              'Authorization': `token ${process.env.GITHUB_TOKEN}`
            })
          }
        }
      );

      return response.data;
    } catch (error) {
      console.error(`Failed to fetch page ${page}:`, error.message);
      throw error;
    }
  }

  async fetchAllContributors() {
    let page = 1;
    let hasMore = true;

    while (hasMore) {
      const contributors = await this.fetchPage(page);

      if (contributors.length === 0) {
        hasMore = false;
        break;
      }

      for (const user of contributors) {
        if (this.shouldExcludeUser(user)) continue;

        const userHtml = this.createUserHtml(user);
        this.contributors += '\n' + this.indentString(userHtml);
        this.index++;
      }

      page++;

      // Add a small delay to be respectful to the API
      await new Promise(resolve => setTimeout(resolve, 100));
    }
  }

  async generateFile() {
    try {
      await this.fetchAllContributors();

      this.contributors += '\n</div>';
      this.contributors = this.indentString(this.contributors, '');

      const content = [
        '<!-- editorconfig-checker-disable-file -->',
        '',
        '## Contributors',
        '',
        '<!-- readme: contributors -start -->',
        this.contributors,
        '<!-- readme: contributors -end -->',
        ''
      ].join('\n');

      await fs.writeFile('CONTRIBUTORS.md', content);
      console.log(`Successfully updated CONTRIBUTORS.md with ${this.index} contributors`);

    } catch (error) {
      console.error('Failed to generate contributors file:', error);
      process.exit(1);
    }
  }
}

// Run the script
const fetcher = new ContributorsFetcher();
fetcher.generateFile();
