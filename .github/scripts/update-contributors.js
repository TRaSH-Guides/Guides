const axios = require('axios');
const fs = require('fs');

// Indentation function
function indentString(string, indentation) {
  return string.split('\n').map(line => indentation + line).join('\n');
}

axios.get('https://api.github.com/repos/FonduemangVI/Guides/contributors')
  .then((response) => {
    let contributors = '<table>\n';
    let index = 0;

    response.data.forEach((user) => {
      // Exclude bots
      if (user.type === 'Bot') return;

      if (index % 6 === 0) {
        contributors += '<tr>';
      }

      const userHtml = `
<td align="center">
    <a href="${user.html_url}">
        <img src="${user.avatar_url}&v=4" width="100;" alt="${user.login}"/>
        <br />
        <sub><b>${user.login}</b></sub>
    </a>
</td>`;

      contributors += indentString(userHtml, '    ');

      if ((index + 1) % 6 === 0 || index === response.data.length - 1) {
        contributors += '\n</tr>\n';
      }

      index++;
    });

    contributors += '</table>\n';
    contributors = indentString(contributors, '');

    fs.writeFileSync('CONTRIBUTORS.md', `## Contributors\n\n<!-- readme: contributors -start -->\n${contributors}\n<!-- readme: contributors -end -->\n`);
  })
  .catch((error) => {
    console.error(`Could not fetch contributors: ${error}`);
  });
