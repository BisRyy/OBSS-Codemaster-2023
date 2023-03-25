// web crawler
link = "https://cm2023.obss.io/2165506a-18f1-4322-a260-bd8b6dc2240e?lang=EN";

// request
request(link, function (error, response, html) {
    if (!error && response.statusCode == 200) {
        var $ = cheerio.load(html);
        var title = $("title").text();
        console.log(title);
    }
    else {
        console.log(error);
    }
    console.log(html);
    console.log(response.statusCode);
    console.log(error);
}