const axios = require('axios');
const fs = require('fs');

// Indentation function
function indentString(string, indentation) {
  return string.split('\n').map(line => indentation + line).join('\n');
}

let contributors = '<table>\n';
let index = 0;
let page = 1;

function fetchPage() {
  axios.get(`https://api.github.com/repos/FonduemangVI/Guides/contributors?per_page=100&page=${page}`)
    .then((response) => {
      if (response.data.length === 0) {
        // No more contributors, write the file
        contributors += '</table>\n';
        contributors = indentString(contributors, '');

        fs.writeFileSync('CONTRIBUTORS.md', `## Contributors\n\n<!-- readme: contributors -start -->\n${contributors}\n<!-- readme: contributors -end -->\n`);
        return;
      }

      response.data.forEach((user) => {
        // Exclude bots and actions-user
        if (user.type === 'Bot' || user.login.toLowerCase().includes('bot') || user.login === 'actions-user') return;

        if (index % 6 === 0) {
          contributors += '<tr>';
        }

        const userHtml = `
<td align="center">
    <a href="${user.html_url}">
        <img src="${user.avatar_url}&v=4" style="width: 50px; border-radius: 50%;" alt="${user.login}"/>
        <br />
        <b><a href="${user.html_url}">${user.login}</a></b>
    </a>
</td>`;

        contributors += indentString(userHtml, '    ');

        if ((index + 1) % 6 === 0 || index === response.data.length - 1) {
          contributors += '\n</tr>\n';
        }

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