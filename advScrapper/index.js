const axios = require('axios');
const qs = require('qs');
let data = qs.stringify({
  'username': '242042064',
  'password': '24-09-2006' 
});

let config = {
  method: 'post',
  maxBodyLength: Infinity,
  url: 'https://jeeadv.iitm.ac.in/result24/index.php',
  headers: { 
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:126.0) Gecko/20100101 Firefox/126.0', 
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8', 
    'Accept-Language': 'en-US,en;q=0.5', 
    'Accept-Encoding': 'gzip, deflate, br, zstd', 
    'Content-Type': 'application/x-www-form-urlencoded', 
    'Origin': 'https://jeeadv.iitm.ac.in', 
    'Connection': 'keep-alive', 
    'Referer': 'https://jeeadv.iitm.ac.in/result24/index.php', 
    'Cookie': 'PHPSESSID=ru5ulpjsljipuprhruvjflt6a4', 
    'Upgrade-Insecure-Requests': '1', 
    'Sec-Fetch-Dest': 'document', 
    'Sec-Fetch-Mode': 'navigate', 
    'Sec-Fetch-Site': 'same-origin', 
    'Sec-Fetch-User': '?1', 
    'Priority': 'u=1'
  },
  data : data
};

axios.request(config)
.then((response) => {
  console.log(JSON.stringify(response.data));
})
.catch((error) => {
  console.log(error);
});
