// Selection of all tags containing text
const html = document.querySelectorAll("*:not(script):not(style):not(meta):not(title):not(head):not(html):not(body)");

// function to make requests to the Google Translate API
async function translate (text, targetlanguage) {
    const url = `https://translate.googleapis.com/translate_a/single?client=gtx&sl=auto&tl=${targetlanguage}&dt=t&q=${text}`;
    const data = await fetch(url)
    const response = await data.json()
    return response[0][0][0]
}
// function to translate the text using the API
async function translates () {
    html.forEach(async elemento => {
        if (elemento.textContent.trim() !== "" && elemento.childElementCount === 0) {
            elemento.textContent = await translate(elemento.textContent,'hi' )
        }
        console.log(elemento.textContent)
    })
}

// Calling the function to translate the text
translates()