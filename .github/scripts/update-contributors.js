const fs = require('fs');
const axios = require('axios');

const owner = 'FonduemangVI';
const repo = 'Guides';

axios.get(`https://api.github.com/repos/${owner}/${repo}/contributors`)
  .then(response => {
    const contributors = response.data.map(user => `- [@${user.login}](${user.html_url})`).join('\n');
    fs.writeFileSync('CONTRIBUTORS.md', `# Contributors\n\n${contributors}\n`);
  })
  .catch(error => {
    console.error(error);
    process.exit(1);
  });
