const axios = require('axios');
const fs = require('fs');

// Indentation function
function indentString(string, indentation) {
  return string.split('\n').map(line => indentation + line).join('\n').trim();
}

let contributors = '<div style="display: flex; flex-wrap: wrap;">';
let index = 0;
let page = 1;

function fetchPage() {
  axios.get(`https://api.github.com/repos/TRaSH-Guides/Guides/contributors?per_page=100&page=${page}`)
    .then((response) => {
      if (response.data.length === 0) {
        // No more contributors, write the file
        contributors += '\n</div>';
        contributors = indentString(contributors, '');

        fs.writeFileSync('CONTRIBUTORS.md', `<!-- editorconfig-checker-disable-file -->\n\n## Contributors\n\n<!-- readme: contributors -start -->\n${contributors}\n<!-- readme: contributors -end -->\n`);
        return;
      }

      response.data.forEach((user, i) => {
        // Exclude bots and actions-user
        if (user.type === 'Bot' || user.login.toLowerCase().includes('bot') || user.login === 'actions-user' || user.login === 'mynameisbogdan') return;

        // Determine row index for background color
        const rowIndex = Math.floor(index / 5);
        const bgColor = (rowIndex % 2 === 0) ? '#1e2129' : '#303850';

        const userHtml = `
<div style="flex: 1 1 20%; background-color: ${bgColor}; border: 1px solid #373a42; padding: 10px; text-align: center;">
  <img src="${user.avatar_url}&v=4" style="width: 50px; border-radius: 50%;" alt="${user.login}">
  <br>
  <b><a href="${user.html_url}" style="color: #ffa500;">${user.login}</a></b>
</div>`;

        contributors += '\n' + indentString(userHtml, '    ');

        index++;
      });

      // Fetch the next page
      page++;
      fetchPage();
    })
    .catch((error) => {
      console.error(`Could not fetch contributors: ${error}`);
    });
}

fetchPage();
