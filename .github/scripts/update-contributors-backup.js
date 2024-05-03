const axios = require('axios');
const fs = require('fs');

let contributors = [];
let page = 1;

function fetchPage() {
  axios.get(`https://api.github.com/repos/FonduemangVI/Guides/contributors?per_page=100&page=${page}`)
    .then((response) => {
      if (response.data.length === 0) {
        // No more contributors, write the file
        fs.writeFileSync('CONTRIBUTORS.json', JSON.stringify(contributors, null, 2));
        return;
      }

      response.data.forEach((user) => {
        // Exclude bots and actions-user
        if (user.type === 'Bot' || user.login.toLowerCase().includes('bot') || user.login === 'actions-user') return;

        const userJson = {
          "title": user.login,
          "image": user.avatar_url,
          "url": user.html_url,
        };

        contributors.push(userJson);
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
