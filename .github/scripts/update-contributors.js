  const fs = require('fs');
  const axios = require('axios');
  
  const owner = 'FonduemangVI';
  const repo = 'Guides';
  
  async function updateContributors() {
    try {
      const response = await axios.get(`https://api.github.com/repos/${owner}/${repo}/contributors`);
  
      if (!response.data || !Array.isArray(response.data)) {
        throw new Error('Invalid response from GitHub API');
      }
  
      let contributors = '<table>\n<tr>\n';
  
      response.data.forEach((user, index) => {
        if (!user.login || !user.html_url || !user.avatar_url) {
          throw new Error('Invalid user data from GitHub API');
        }
  
        contributors += `
          <td align="center">
            <a href="${user.html_url}">
              <img src="${user.avatar_url}&s=100" width="100;" alt="${user.login}"/>
              <br />
              <sub><b>${user.login}</b></sub>
            </a>
          </td>`;
  
        // Add a new row every 6th user
        if ((index + 1) % 6 === 0) {
          contributors += '\n</tr>\n<tr>\n';
        }
      });
  
      contributors += '</tr>\n</table>';
  
      fs.writeFileSync('CONTRIBUTORS.md', `## Contributors\n\n<!-- readme: contributors -start -->\n${contributors}\n<!-- readme: contributors -end -->\n`);
    } catch (error) {
      console.error('Error updating contributors:', error.message);
  
      if (error.response) {
        console.error('Response status:', error.response.status);
        console.error('Response data:', error.response.data);
      }
  
      process.exit(1);
    }
  }
  
  updateContributors();
  