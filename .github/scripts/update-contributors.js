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
  
      const contributors = response.data.map(user => {
        if (!user.login || !user.html_url) {
          throw new Error('Invalid user data from GitHub API');
        }
        return `- [@${user.login}](${user.html_url})`;
      }).join('\n');
  
      fs.writeFileSync('CONTRIBUTORS.md', `# Contributors\n\n${contributors}\n`);
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
  